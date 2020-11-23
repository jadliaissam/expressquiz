from django.apps import apps
from rest_framework import serializers

from app.models.Discussion import Discussion


class DiscussionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discussion
        fields = "__all__"


