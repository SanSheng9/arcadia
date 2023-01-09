from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    email = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True, primary_key=True)
    password = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='photos/%Y/%m/%d', blank=False, default='avatar.svg', verbose_name='avatar')
    about_me = models.CharField(max_length=255, default="I'm new user!", blank=False)
