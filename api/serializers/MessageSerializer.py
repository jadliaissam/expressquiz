from django.apps import apps
from rest_framework import serializers

from app.models import Message
from app.models.Discussion import Discussion


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
