from django.contrib import admin

# Register your models here.
from .models import Vehicle_Model

class Vehicle_Admin(admin.ModelAdmin):
    list_display = ('make', 'model', 'year', 'color', 'vin', 'mileage')
    search_fields = ('make', 'model', 'color', 'mileage')

admin.site.register(Vehicle_Model, Vehicle_Admin)