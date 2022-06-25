from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    username = None

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []


class LinkDetails(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    icon_url = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title


class UserLinks(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    link_id = models.ForeignKey(LinkDetails, on_delete=models.CASCADE)
    link_url = models.CharField(max_length=255)

    def __str__(self):
        return self.id
