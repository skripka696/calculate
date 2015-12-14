from django.shortcuts import render
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User

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


class CorporateaccountList(viewsets.ModelViewSet):

    serializer_class = serializers.AccountSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return self.request.user.corporateaccount_set.all()

