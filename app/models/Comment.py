from django.contrib.auth.models import User
from django.db import models
from app.models import Post


class Comment(models.Model):
    title = models.CharField(max_length=1000)
    body = models.TextField()
    comment_user = models.ForeignKey(User)
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)

