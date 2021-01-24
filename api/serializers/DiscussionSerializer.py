from django.apps import apps
from rest_framework import serializers

from api.serializers.UserSerializer import UserSerializer
from api.serializers.MessageSerializer import MessageSerializer
from app.models.Discussion import Discussion


class DiscussionSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True)
    users = UserSerializer(many=True)

    class Meta:
        model = Discussion
        fields = "__all__"


