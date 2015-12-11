from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *


def index(request):
    """
    Entry to app
    """
    return render(request, 'mercury/index.html', {'title': 'PricePoint - Pricing Tool'})


class CurrenciesViewSet(viewsets.ModelViewSet):
    """
        A viewsets for viewing all instances Currency and
        for only one instance
    """
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class AssociationViewSet(viewsets.ModelViewSet):
    """
        A viewset for viewing all instances AgentAssociations
    """
    queryset = Agentassociations.objects.all()
    serializer_class = AssociationSerializer
