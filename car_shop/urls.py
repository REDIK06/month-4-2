from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_shop_view, name='car_shop'),
    path('car_detail/<int:id>/', views.car_shop_detail_view, name='car_detail'),
    path('car_detail/<int:id>/delete/', views.delete_car_view, name='car_delete'),
    path('car_detail/<int:id>/update/', views.update_car_view, name='car_update'),
    path('create_car/', views.create_car_view, name='create_car'),
    path('car_detail/<int:id>/add_comment/', views.add_comment_view, name='add_comment'),

]
