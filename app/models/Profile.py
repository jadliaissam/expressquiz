from django.db import models
from .Language import Language
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    avatar = models.ImageField(null=True)
    bio = models.TextField()
    following = models.ManyToManyField(User)
    followed_by = models.ManyToManyField(User)
    native_languages = models.ManyToManyField(Language)
    learning_languages = models.ManyToManyField(Language)
    profile_user = models.ForeignKey(User, on_delete=models.CASCADE)
