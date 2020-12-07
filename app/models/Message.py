from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from app.models import Discussion


class Message(models.Model):
    content = models.TextField()
    message_sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages_sent")
    message_receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="messages_received")
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name="messages")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
