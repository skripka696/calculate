from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
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
