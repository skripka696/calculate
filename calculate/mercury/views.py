from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *


def index(request):
    """
    Entry to app
    """
    return render(request, 'mercury/index.html', {'title': 'PricePoint - Pricing Tool'})


class CurrenciesViewSet(generics.ListAPIView):
    """
        A viewsets for viewing all instances Currency model and
        for only one instance
    """
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class AssociationViewSet(generics.ListAPIView):
    """
        A viewset for viewing all instances AgentAssociations model
    """
    queryset = Agentassociations.objects.all()
    serializer_class = AssociationSerializer


class CertificationViewSet(generics.ListAPIView):
    """
        A viewset for viewing all instances AgentCertifications model
    """
    queryset = Agentcertifications.objects.all()
    serializer_class = CertificationSerializer


class LocationViewSet(generics.ListAPIView):
    """
        A viewset for viewing all instances Location model
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
