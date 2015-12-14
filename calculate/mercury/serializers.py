from rest_framework import serializers
from .models import *


class CurrencySerializer(serializers.ModelSerializer):
    """
        Create serializer for instance Currency model to represent in json
        format
    """
    priceInUSD = serializers.FloatField(source='price_in_usd')

    class Meta:
        model = Currency
        fields = ('id', 'name', 'symbol', 'priceInUSD')


class AssociationSerializer(serializers.ModelSerializer):
    """
        Create serializer for instance Association model to represent in json
        format
    """
    class Meta:
        model = Agentassociations


class CertificationSerializer(serializers.ModelSerializer):
    """
        Create serializer for instance Certification model to represent in json
        format
    """
    class Meta:
        model = Agentcertifications


class LocationSerializer(serializers.ModelSerializer):
    """
        Create serializer for instance Location model to represent in json
        format
    """
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
