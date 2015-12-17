from django.db.models.aggregates import Avg, Count
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
    Ports = serializers.PrimaryKeyRelatedField(source='port_set', read_only=True, many=True)
    symbol = serializers.SerializerMethodField()

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


class AgentSerializer(serializers.ModelSerializer):
    associations = AssociationSerializer(many=True)
    certifications = CertificationSerializer(many=True)
    logo = serializers.StringRelatedField(source='agentlogo.logo')
    ratings = serializers.SerializerMethodField()

    def get_logo(self, agent):
        return models.Agentlogo.objects.get(agent=agent).logo.url

    def get_ratings(self, agent):
        request = self.context['request']
        user = request.user.clientuser.user
        query = models.Agentrating.objects.filter(agent=agent)
        avg_user_rating = query.exclude(user=user).aggregate(average=Avg('user_rating'))['average']
        if not avg_user_rating:
            avg_user_rating = 0
        count_user = query.exclude(user=user).aggregate(users=Count('user'))['users']
        try:
            user_rating = query.filter(user=user)[0].user_rating
        except IndexError:
            user_rating = 0
        return {'average': avg_user_rating,
                'userRating': user_rating,
                'users': count_user}
        # # return request.user

    class Meta:
        model = models.Agent
        fields = ('id', 'name', 'logo', 'associations', 'certifications', 'ratings')


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


class PriceSerializer(serializers.Serializer):
    # Ports =
    agent_details = serializers.DictField()
    chargeable_volume = serializers.IntegerField()
    chargeable_weight = serializers.IntegerField()
    converted_rate = serializers.FloatField()
    currency_id = serializers.IntegerField()
    # market_id = serializers.IntegerField()
    maximum_volume = serializers.FloatField()
    minimum_volume = serializers.IntegerField()
    rate = serializers.FloatField()
    tariff_id = serializers.IntegerField()
    thc = serializers.IntegerField()



