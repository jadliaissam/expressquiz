from rest_framework import viewsets

from app.models.Discussion import Discussion
from api.serializers.DiscussionSerializer import DiscussionSerializer


class DiscussionViewAPI(viewsets.ModelViewSet):
    serializer_class = DiscussionSerializer

    def get_queryset(self):
        return Discussion.objects.filter(users__pk=self.request.user.pk)
