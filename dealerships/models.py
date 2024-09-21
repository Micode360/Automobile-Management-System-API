from django.db import models
from users.models import CustomUser


# Create your models here.
class Dealership_Model(models.Model):
    user = models.ForeignKey(CustomUser, unique=False, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    contact = models.CharField(max_length=250)