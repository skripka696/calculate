from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CurrenciesSerializer
from .models import Currency


def index(request):
    """
    Entry to app
    """
    return render(request, 'mercury/index.html', {'title': 'PricePoint - Pricing Tool'})


class CurrenciesViewSet(viewsets.ModelViewSet):
    """
        A viewsets for viewing all instances and
        for only one instance
    """
    queryset = Currency.objects.all()
    serializer_class = CurrenciesSerializer

