from django.urls import path
from  .views import VehicleViews

urlpatterns = [
    path('vehicle/', VehicleViews.as_view(),name="vehicles"),
    path('vehicle/<int:id>/', VehicleViews.as_view(),name="vehicles")
]
