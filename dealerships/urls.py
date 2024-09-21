from django.urls import path
from  .views import DealershipViews

urlpatterns = [
    path('dealership/', DealershipViews.as_view(),name="dealership"),
    path('dealership/<int:id>/', DealershipViews.as_view(),name="dealership")
]
