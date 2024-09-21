from django.contrib import admin
from .models import Maintenance_Model

class MaintenanceModelAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'maintenance_type', 'maintenance_date', 'service_provider', 'cost')
    search_fields = ('vehicle__make', 'maintenance_type', 'service_provider')
    list_filter = ('maintenance_type', 'maintenance_date')

admin.site.register(Maintenance_Model, MaintenanceModelAdmin)
