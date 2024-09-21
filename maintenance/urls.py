from django.urls import path
from  .views import MaintenanceViews

urlpatterns = [
    path('logs/', MaintenanceViews.as_view(),name="logs"),
    path('logs/<int:id>/', MaintenanceViews.as_view(),name="logs")
]
