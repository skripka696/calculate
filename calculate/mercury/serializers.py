from rest_framework import serializers
from models import Port, Corporateaccount


class PortSerializer(serializers.ModelSerializer):
    """
    Serializer for model 'port'
    """
    class Meta:
        model = Port


class AccountSerializer(serializers.Serializer):
    """
    Serializer for corporate account
    """
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)

