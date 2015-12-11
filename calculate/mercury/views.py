from django.shortcuts import render
from rest_framework import viewsets, permissions

import models
import serializers


def index(request):
    """
    Entry to app
    """
    return render(request, 'mercury/index.html', {'title': 'PricePoint - Pricing Tool'})


class PortList(viewsets.ModelViewSet):
    """
    ModelViewset for request to model 'port' (read only)
    """
    queryset = models.Port.objects.all()
    serializer_class = serializers.PortSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

