from django.db import models
from users.models import CustomUser
from vehicles.models import Vehicle_Model  # Assuming you have a Vehicle model for your vehicles
from django.utils import timezone


# Sales model to track vehicle sales
class Sales_Model(models.Model):
    buyer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)  # Linked to user if applicable
    buyer_name = models.CharField(max_length=250, blank=True)  # Full name of the buyer
    buyer_contact = models.CharField(max_length=250, blank=True)  # Contact details (e.g., phone number, email)
    buyer_drivers_liscense = models.CharField(max_length=100, null=True, blank=True)  # ID verification (e.g., driver's license)
    
    vehicle_sold = models.ForeignKey(Vehicle_Model, on_delete=models.SET_NULL, null=True)  # Link to the vehicle model
    sale_price = models.FloatField(blank=True)  # Sale price of the vehicle
    sale_date = models.DateTimeField(auto_now_add=timezone.now)  # Automatically add the sale date and time

    payment_method = models.CharField(max_length=100, null=True, blank=True)  # e.g., Credit Card, Cash
    notes = models.TextField(null=True, blank=True)  # Any additional notes about the sale

    def __str__(self):
        return f"Sale: {self.buyer_name} bought {self.vehicle_sold} for ${self.sale_price}"
