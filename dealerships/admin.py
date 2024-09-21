from django.contrib import admin

# Register your models here.
from .models import Dealership_Model

class DealerShip_Admin(admin.ModelAdmin):
    list_display = ('id','user','name', 'address', 'contact')
    search_fields = ('user','name', 'contact')

admin.site.register(Dealership_Model, DealerShip_Admin)