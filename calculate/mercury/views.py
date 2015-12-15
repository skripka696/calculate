from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
import serializers
import models
import json


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


class UserAccount(APIView):

    def get(self, request):
        return Response(json.loads('[{"id": null, "name": "None"}]'))


class GetDetails(APIView):
    """
        Take details about agent
    """
    # model = models.Agent


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
                    'FCL_C': models.Fclfreighttariff,
                    'FCL_L': models.Fclfreighttariff,
                    'LCL': models.Lclfreighttariff,
                    'Air': models.Airfreighttariff,
                    'Road': models.Roadfreighttariff,
                }

                current_tarrif = tarifftype.get(self.request.query_params.get('tariffType'))
                agent_ids = set()
                for lane in lanes:
                    if current_tarrif:
                        if current_tarrif.objects.filter(lane=lane).exists():
                            agent_ids.add(lane.agent_id)

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












