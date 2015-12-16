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
    def get(self, request, format=None):

        # convert to int
        currency_id = int(self.request.query_params.get('currencyId'))
        weight = int(self.request.query_params.get('weight'))
        volume = int(self.request.query_params.get('volume'))
        location_id = int(self.request.query_params.get('locationId', 0))
        shipment_type = self.request.query_params.get('tariffType')
        service_type = {
            'flc_l_o': 'flc_l_o',
            'flc_c_o': 'flc_c_o',
            'lcl_o': 'lcl_o',
            'air_o': 'air_o',
            'perm_o': 'perm_o',
            'flc_l_d': 'flc_l_d',
            'flc_c_d': 'flc_c_d',
            'lcl_d': 'lcl_d',
            'air_d': 'air_d',
            'perm_d': 'perm_d',
            'fcl_f': 'fcl_f',
            'lcl_f': 'lcl_f',
            'air_f': 'air_f',
            'road_f': 'road_f',
            'road_o': 'road_o',
            'road_d': 'road_d',
        }

        origin_ports = [int(item) for item in self.request.query_params.getlist('originPorts', [])]
        dest_ports = [int(item) for item in self.request.query_params.getlist('destinationPorts', [])]
        try:
            agent_id = request.user.agent_set.first().pk
        except Exception:
            agent_id = 0
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
            if agent_id:
                lanes = lanes.filter(agent_id=agent_id)

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
                    percentage = shipment_type[3] +'_'+service_type[0]
                    percentage_key = getattr(models.Discount, service_type)
                    discount_type_percentage = discount.percentage_key
                    if discount.multiplier > 1:
                        discount_type_multiplier = (100 + discount_type_percentage) / 100
                    else:
                        discount_type_multiplier = (100 - discount_type_percentage) / 100
        else:
            pass

        return Response({})
