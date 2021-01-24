from django.apps import apps
from django.contrib.auth.models import User
from rest_framework import serializers

from app.models.Discussion import Discussion


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


