from rest_framework import serializers
import models
from time import mktime


class CurrencySerializer(serializers.ModelSerializer):
    """
        Create serializer for instance Currency model to represent in json
        format
    """
    priceInUSD = serializers.FloatField(source='price_in_usd')

    class Meta:
        model = models.Currency
        fields = ('id', 'name', 'symbol', 'priceInUSD')


class AssociationSerializer(serializers.ModelSerializer):
    """
        Create serializer for instance Association model to represent in json
        format
    """
    class Meta:
        model = models.Agentassociations


class CertificationSerializer(serializers.ModelSerializer):
    """
        Create serializer for instance Certification model to represent in json
        format
    """
    class Meta:
        model = models.Agentcertifications


class LocationSerializer(serializers.ModelSerializer):
    """
        Create serializer for instance Location model to represent in json
        format
    """
    Ports = serializers.SerializerMethodField()
    symbol = serializers.SerializerMethodField()

    def get_Ports(self, obj):
        return obj.port_set.all().values_list('pk', flat=True)

    def get_symbol(self, obj):
        if obj:
            return obj.name[:3].upper()
        return None

    class Meta:
        model = models.Location
        fields = ('Ports', 'id', 'name', 'symbol')


class UserSerializer(serializers.ModelSerializer):

    """
        Create serializer for instance User model to represent in json
        format
    """

    agent_id = serializers.SerializerMethodField()
    iat = serializers.SerializerMethodField()

    def get_iat(self, obj):
        return mktime(obj.last_login.timetuple())

    def get_agent_id(self, obj):
        agent_id = obj.agent_set.all()
        if agent_id.exists():
            return agent_id[0].pk
        else:
            return 0

    class Meta:
        model = models.User
        fields = ('id', 'username', 'iat', 'agent_id')



class PortSerializer(serializers.ModelSerializer):
    """
    Serializer for model 'port'
    """
    class Meta:
        model = models.Port
        fields = ('id', 'name')


class CorporateAccountSerializer(serializers.ModelSerializer):
    """
    Serializer for corporate account
    """
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        user = obj.account
        if user.first_name or user.last_name:
            return ' '.join([user.first_name, user.last_name])
        else:
            return user.username

    class Meta:
        model = models.Corporateaccount
        fields = ('id', 'name')


