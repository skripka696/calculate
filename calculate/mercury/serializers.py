from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Agent

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(max_length=100)
    agent = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'agent']

    # def get_agent(self, obj):
    #     return obj.agent