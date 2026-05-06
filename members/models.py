from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='members/', null=True, blank=True)

class Membership(models.Model):
        full_name = models.CharField(max_length=200)
        email = models.EmailField()
        phone = models.CharField(max_length=20)
        city = models.CharField(max_length=100)
        motivation = models.TextField()

        date_joined = models.DateTimeField(auto_now_add=True)


def __str__(self):
     return self.name
