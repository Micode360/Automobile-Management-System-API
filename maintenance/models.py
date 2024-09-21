from django.db import models
from vehicles.models import Vehicle_Model
from django.utils import timezone


class Maintenance_Model(models.Model):
    vehicle = models.ForeignKey(Vehicle_Model, on_delete=models.CASCADE)
    maintenance_type = models.CharField(max_length=100)
    maintenance_date = models.DateTimeField(default=timezone.now)
    service_provider = models.CharField(max_length=250)
    cost = models.FloatField()
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.vehicle} - {self.maintenance_type} on {self.maintenance_date}"

