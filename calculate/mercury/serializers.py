from rest_framework import serializers
import models
from time import mktime


class UserSerializer(serializers.ModelSerializer):
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
        fields = ['id', 'username', 'iat', 'agent_id']
