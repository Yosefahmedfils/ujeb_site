from email.policy import default

from django.db import models

class Activity(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='activities/', null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    participants = models.IntegerField(default=0)
    date = models.DateField(blank=True, null=True)

