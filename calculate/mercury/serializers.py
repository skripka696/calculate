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


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agentcertifications
        

class LocationSerializer(serializers.ModelSerializer):
    Ports = serializers.SerializerMethodField()
    symbol = serializers.SerializerMethodField()

    def get_Ports(self, obj):
        return obj.ports_set.all().values_list('pk', flat=True)

    def get_symbol(self, obj):
        if obj:
            return obj.name[:3].upper()
        return None

    class Meta:
        model = Location
        fields = ('Ports', 'id', 'name', 'symbol')