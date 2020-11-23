from django.db import models
from .Language import Language
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    avatar = models.ImageField(null=True)
    bio = models.TextField(null=True, blank=True)
    following = models.ManyToManyField(User, blank=True, related_name="followed_by")
    followers = models.ManyToManyField(User, blank=True, related_name="following")
    native_languages = models.ManyToManyField(Language, related_name="native_users")
    fluent_languages = models.ManyToManyField(Language, related_name="fluent_users")
    learning_languages = models.ManyToManyField(Language, related_name="learning_users")
    profile_user = models.ForeignKey(User, on_delete=models.CASCADE)
