from django.db import models

class Partner(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='partners/', null=True, blank=True)
    def __str__(self):
        return self.name
