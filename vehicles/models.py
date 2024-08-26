from django.db import models
from users.models import CustomUser

# Create your models here.
class Vehicle_Model(models.Model):
    # one to many relationship oneToOneField is only saying there is relationship between just one model data to another one model data another can't be created.
    user = models.ForeignKey(CustomUser, unique=False, on_delete=models.SET_NULL, null=True) # models.CASCADE with delete the data along with the user but i dont want the data to go
    make = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    year = models.IntegerField()
    color = models.CharField(max_length=250)
    vin = models.CharField(max_length=17, unique=True)  # VINs are typically 17 characters long and unique
    mileage = models.CharField(max_length=250)  # Assuming mileage can be a string (e.g., '15000 miles') distance in an hour
    price = models.DecimalField(max_digits=10, decimal_places=2)  # DecimalField for accurate price representation