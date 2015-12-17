from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from converter import Converter
import serializers
import models


def index(request):
    """
    Entry to app
    """
    return render(request, 'mercury/index.html', {'title': 'PricePoint - Pricing Tool'})


class CurrenciesView(generics.ListAPIView):
    """
        A viewsets for viewing all instances Currency model and
        for only one instance
    """
    queryset = models.Currency.objects.all()
    serializer_class = serializers.CurrencySerializer


class AssociationView(generics.ListAPIView):
    """
        A viewset for viewing all instances AgentAssociations model
    """
    queryset = models.Agentassociations.objects.all()
    serializer_class = serializers.AssociationSerializer


class CertificationView(generics.ListAPIView):
    """
        A viewset for viewing all instances AgentCertifications model
    """
    queryset = models.Agentcertifications.objects.all()
    serializer_class = serializers.CertificationSerializer


class LocationView(generics.ListAPIView):
    """
        A viewset for viewing all instances Location model
    """
    queryset = models.Location.objects.all().order_by('name')
    serializer_class = serializers.LocationSerializer


class MeView(APIView):

    def get(self, request, format=None):
        user = request.user
        serializer = serializers.UserSerializer(user)
        return Response(serializer.data)


class PortView(generics.ListAPIView):
    """
    ModelView for request to model 'port' (read only)
    """
    queryset = models.Port.objects.all()
    serializer_class = serializers.PortSerializer


class GetDetails(APIView):
    """
        Take details about agent
    """
    def get(self, request, format=None):
        try:
            agent_id = request.user.agent_set.first().pk
        except Exception:
            agent_id = 0
        if self.request.query_params.get('serviceType') == 'Freight':
            if agent_id:
                agent_ids = [agent_id]
            else:
                lanes = models.Lane.objects.filter(
                    origin_port__in=self.request.query_params.getlist('originPorts'),
                    destination_port__in=self.request.query_params.getlist('destinationPorts'))

                tarifftype = {
                    'FCL_C': 'fclfreighttariff',
                    'FCL_L': 'fclfreighttariff',
                    'LCL': 'lclfreighttariff',
                    'Air': 'airfreighttariff',
                    'Road': 'roadfreighttariff',
                }

                current_tarrif = tarifftype.get(self.request.query_params.get('tariffType'))
                tarif_option_name = '%s__isnull' % current_tarrif
                lanes = lanes.filter(**{tarif_option_name: False})
                agent_ids = lanes.values_list('agent_id', flat=True)

            discounts = models.Discount.objects.filter(agent_id__in=agent_ids, user=request.user)
            discount_map = {}
            for discount in discounts:
                discount_map[discount.agent_id] = discount.multiplier

            for agent in agent_ids:
                if agent not in discount_map:
                    discount_map[agent] = 1

            result = []
            for k, v in discount_map.iteritems():
                if v >= 0:
                    result.append(k)

            agents = models.Agent.objects.filter(id__in=result)

            serializer = serializers.AgentSerializer(agents, many=True,
                                                     context={'request':request})
            return Response(serializer.data)

        else:
            if agent_id:
                agent_ids = [agent_id]
            else:
                location_id = self.request.query_params.get('locationId')
                if self.request.query_params.get('serviceType') == 'Origin':

                    markets = models.Location.objects.get(pk=location_id).markets.filter(
                        port__in=self.request.query_params.getlist('originPorts'))
                else:
                    markets = models.Location.objects.get(pk=location_id).markets.filter(
                        port__in=self.request.query_params.getlist('destinationPorts'))
                agent_ids = set(models.Tariff.objects.filter(market__in=markets).values_list('agent_id', flat=True))

            discounts = models.Discount.objects.filter(agent_id__in=agent_ids, user=request.user)
            discount_map = {}
            for discount in discounts:
                discount_map[discount.agent_id] = discount.multiplier

            for agent in agent_ids:
                if agent not in discount_map:
                    discount_map[agent] = 1

            result = []
            for k, v in discount_map.iteritems():
                if v >= 0:
                    result.append(k)

            agents = models.Agent.objects.filter(id__in=result)

            serializer = serializers.AgentSerializer(agents, many=True,
                                                     context={'request':request})
            return Response(serializer.data)


class CorporateaccountList(APIView):

    def get(self, request, format=None):
        query = request.user.named_user.all()
        # query = User.objects.get(pk=315).named_user.all()
        corp_account_list = serializers.CorporateAccountSerializer(query, many=True)
        data = corp_account_list.data
        data.append({'id': None, 'name': 'None'})
        return Response(data)


class GetPrice(APIView):
    """
    APIView for price list
    """

    def get_convert_currency(self, value, src_currency_id, dest_currency_id, timestamp):


    def get_freight_contact(self, agent, contact_details):
        if agent.freight_contact:
            contact_details['contact'] = agent.freight_contact
        if agent.freight_phone:
            contact_details['phone'] = agent.freight_phone
        if agent.freight_email:
            contact_details['email'] = agent.freight_email
        return contact_details

    def get_service_details(self, agent, contact_details, service_type):
        if hasattr(models.agent, service_type+'_contact'):
            contact_details.contact = hasattr(models.agent, service_type+'_contact')
        if hasattr(models.agent, service_type+'_phone'):
            contact_details.phone = hasattr(models.agent, service_type+'_phone')
        if hasattr(models.agent, service_type+'_email'):
            contact_details.email = hasattr(models.agent, service_type+'_email')
        return contact_details

    def get_phone(self, agent):
        if agent.phone:
            return agent.phone
        else:
            return agent.manager_phone

    def get_email(self, agent):
        if agent.email:
            return agent.email
        else:
            return agent.manager_email

    def get_contact_details(self, service_type, agent):
        contact_details = {
           'contact': agent.manager_contact,
            'phone': self.get_phone(agent),
            'email': self.get_email(agent),
        }

        if service_type == 'Freight':
            contact_details = self.get_freight_contact(agent, contact_details)

        service_type = service_type.lower()
        contact_details = self.get_service_details(agent, contact_details, service_type)

    def get_freight_tarriff_price_properties(self, tariff, weight, volume, price=0):
        price = price | {
            'minimum_volume': volume,
            'chargeable_volume': volume,
            'chargeable_weight': weight,
            'maximum_volume': volume,
            'rate': 0,
        }
        price['currency_id'] = tariff.currency.id
        price['tariff_id'] = tariff.id
        price['lane_id'] = tariff.lane.id
        price['dthc'] = tariff.dthc
        price['addon'] = tariff.addon
        price['comment'] = tariff.comment
        price['expiry'] = tariff.expiry
        return price

    def get(self, request, format=None):

        # convert to int
        currency_id = int(self.request.query_params.get('currencyId'))
        weight = int(self.request.query_params.get('weight'))
        volume = int(self.request.query_params.get('volume'))
        location_id = int(self.request.query_params.get('locationId', 0))
        shipment_type = self.request.query_params.get('tariffType')
        service_type = self.request.query_params.get('serviceType')
        container_size = self.request.query_params.get('containerSize')
        include_thc = self.request.query_params.get('includeTHC')

        discount_fields = {
            'fclLooseOriginDiscount': 'flc_l_o',
            'fclCasedOriginDiscount': 'flc_c_o',
            'lclOriginDiscount': 'lcl_o',
            'airOriginDiscount': 'air_o',
            'permStorageOriginDiscount': 'perm_o',
            'fclLooseDestinationDiscount': 'flc_l_d',
            'fclCasedDestinationDiscount': 'flc_c_d',
            'lclDestinationDiscount': 'lcl_d',
            'airDestinationDiscount': 'air_d',
            'permStorageDestinationDiscount': 'perm_d',
            'fclFreightDiscount': 'fcl_f',
            'fclLooseFreightDiscount': 'fcl_f',
            'lclFreightDiscount': 'lcl_f',
            'airFreightDiscount': 'air_f',
            'roadFreightDiscount': 'road_f',
        }

        origin_ports = [int(item) for item in self.request.query_params.getlist('originPorts', [])]
        dest_ports = [int(item) for item in self.request.query_params.getlist('destinationPorts', [])]
        try:
            agent = request.user.agent_set.first()
        except Exception:
            agent.id = 0
        converted_volume = Converter().converter_volume(volume,
                                           self.request.query_params.get('volumeUnits'))
        converted_weight = Converter().convert_weight(weight,
                                         self.request.query_params.get('weightUnits'))
        shipment_type = Converter().get_shipment_type(shipment_type)
        if self.request.query_params.get('serviceType') == 'Freight':
            client = self.request.user.clientuser
            lanes = models.Lane.objects.filter(
                    origin_port__in=dest_ports,
                    destination_port__in=origin_ports)
            if agent.id:
                lanes = lanes.filter(agent=agent)

            tarifftype = {
                'FCL_C': 'fclfreighttariff',
                'FCL_L': 'fclfreighttariff',
                'LCL': 'lclfreighttariff',
                'Air': 'airfreighttariff',
                'Road': 'roadfreighttariff',
            }

            for lane in lanes:
                lane_tariff = getattr(lane, tarifftype.get(self.request.query_params.get('tariffType'))).all()
                lane_agent = lane.agent
                for tariff in lane_tariff:
                    discount = models.Discount.objects.filter(agent=lane_agent)[0]
                    # account_id = models.Corporateaccount.account.first()
                    # if discount:
                    #     discount = discount.first()
                        # if account_id:
                        #     pass
                        # else:

                    percentage_key = shipment_type + service_type + 'Discount'
                    percentage = discount_fields.get(percentage_key)
                    discount_type_multiplier = getattr(discount, percentage)
                    if discount.multiplier > 1:
                        discount_type_multiplier = (100 + discount_type_multiplier) / 100
                    else:
                        discount_type_multiplier = (100 - discount_type_multiplier) / 100
                    if discount_type_multiplier:
                        discount_type_multiplier = discount_type_multiplier
                    else:
                        discount_type_multiplier = discount.multiplier
                    if container_size:
                        container_size = container_size
                    elif converted_volume >= 2200:
                        container_size = '40HC'
                    elif converted_volume >= 1100:
                        container_size = '40'
                    else:
                        container_size = '20'
                    container_size = container_size.upper()
                    price = self.getFreightTarriffPriceProperties(tariff, converted_weight,
                                                             converted_volume)
                    price_key = 'fcl' + container_size + 'Rate'
                    price['rate'] = getattr(tariff, price_key)
                    agent_details = self.get_contact_details(self, service_type, agent)
                    agent_details['name'] = agent.name
                    agent_details['id'] = agent['id']
                    price['agent_details'] = agent_details
                    price['rate'] = price['rate'] * discount_type_multiplier
                    # ?? price['dthc']
                    if include_thc and service_type == 'Destination' and price['thc']:
                        price['rate'] += price['thc']
                    if price.addon:
                        price['rate'] += price['addon']
                    currency = get_convert_currency(price['rate'], )



        else:
            pass

        return Response({})
