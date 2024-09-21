from django.contrib import admin

# Register your models here.
from .models import Sales_Model

class Sales_Admin(admin.ModelAdmin):
    list_display = ('id', 'buyer_name', 'buyer_contact', 'vehicle_sold', 'sale_price', 'sale_date')
    search_fields = ('buyer_name', 'buyer_contact', 'vehicle_sold__make', 'vehicle_sold__model', 'vehicle_sold__vin')
    list_filter = ('sale_date', 'sale_price')
    ordering = ('-sale_date',)

admin.site.register(Sales_Model, Sales_Admin)