from rest_framework import viewsets

from api.serializers.MessageSerializer import MessageSerializer
from app.models.Message import Message


class MessageViewAPI(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
