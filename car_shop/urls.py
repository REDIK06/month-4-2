from django.urls import path
from . import views

urlpatterns = [
    path('', views.CarShopView.as_view(), name='car_shop'),
    path('car_detail/<int:id>/', views.CarShopDetailView.as_view(), name='car_detail'),
    path('car_detail/<int:id>/delete/', views.DeleteCarView.as_view(), name='car_delete'),
    path('car_detail/<int:id>/update/', views.UpdateCarView.as_view(), name='car_update'),
    path('create_car/', views.CreateCarView.as_view(), name='create_car'),

    path('search/', views.SearchView.as_view(), name='search'),
    path('car_detail/<int:id>/add_comment/', views.AddCommentView.as_view(), name='add_comment'),

    path('edit_comment/<int:comment_id>/', views.EditCommentView.as_view(), name='edit_comment'),
    path('delete_comment/<int:comment_id>/', views.DeleteCommentView.as_view(), name='delete_comment'),
]

