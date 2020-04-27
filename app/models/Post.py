from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    code = models.CharField(max_length=50)
    text = models.CharField(max_length=100)


class Post(models.Model):
    title = models.CharField(max_length=1000)
    body = models.TextField()
    tags = models.ManyToManyField(Tag)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)




