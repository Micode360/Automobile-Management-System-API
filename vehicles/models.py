from django.db import models

# Create your models here.
class Vehicle_Model(models.Model):
    make = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    year = models.IntegerField()
    color = models.CharField(max_length=250)
    vin = models.CharField(max_length=17, unique=True)  # VINs are typically 17 characters long and unique
    mileage = models.CharField(max_length=250)  # Assuming mileage can be a string (e.g., '15000 miles') distance in an hour
    price = models.DecimalField(max_digits=10, decimal_places=2)  # DecimalField for accurate price representation