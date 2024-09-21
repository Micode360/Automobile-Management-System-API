from django.urls import path
from  .views import SalesViews

urlpatterns = [
    path('sale/', SalesViews.as_view(),name="sale"),
    path('sale/<int:id>/', SalesViews.as_view(),name="sale")
]
