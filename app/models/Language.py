from django.db import models

# Create your models here.


class Language(models.Model):
    english_name = models.CharField(max_length=1000, null=True, blank=True)
    native_name = models.CharField(max_length=1000, null=True, blank=True)
    code = models.CharField(max_length=255, null=True, blank=True)

