from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ Custom model user"""
    avatar = models.ImageField(
        upload_to='user/avatar/',
        default='/static/default-avatar.jpg',
        blank=True,
        null=True
    )
