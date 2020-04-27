from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Message(models.Model):
    title = models.CharField(max_length=1000)
    body = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
