from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_shop_view, name='car_shop'),
    path('car_detail/<int:id>/', views.car_shop_detail_view, name='car_detail'),
]
