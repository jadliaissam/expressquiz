from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Call(models.Model):
    call_sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="calls_sent")
    call_receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="calls_received")
    duration = models.DurationField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

