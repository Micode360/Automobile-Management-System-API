from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=False, null=False)
    username = models.CharField(max_length=30, blank=True, null=True) # I had to create this username key here in other to make it null
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()
