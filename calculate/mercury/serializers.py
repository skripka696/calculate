from rest_framework import serializers
from .models import *


class CurrencySerializer(serializers.ModelSerializer):
    priceInUSD = serializers.FloatField(source='price_in_usd')

    class Meta:
        model = Currency
        fields = ('id', 'name', 'symbol', 'priceInUSD')


class AssociationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agentassociations
        fields = ('id', 'name')
