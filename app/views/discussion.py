from rest_framework import viewsets

from app.models.Discussion import Discussion
from app.serializers.DiscussionSerializer import DiscussionSerializer


class DiscussionViewAPI(viewsets.ModelViewSet):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
