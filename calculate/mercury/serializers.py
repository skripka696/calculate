from rest_framework import serializers
from models import Port


class PortSerializer(serializers.ModelSerializer):
    """
    Serializer for model 'port'
    """
    class Meta:
        model = Port
