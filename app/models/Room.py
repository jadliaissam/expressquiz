from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Room(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    description = models.TextField()
    users = models.ManyToManyField(User)
