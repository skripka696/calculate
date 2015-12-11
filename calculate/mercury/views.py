from django.shortcuts import render
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from .serializers import  AgentSerializer
from rest_framework import permissions
from .models import Agent

def index(request):
    """
    Entry to app
    """
    return render(request, 'mercury/index.html', {'title': 'PricePoint - Pricing Tool'})


class UserViewSet(viewsets.ModelViewSet):

    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)