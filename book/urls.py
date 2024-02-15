from django.urls import path
from . import views

urlpatterns = [
    path('book_store/', views.book_store, name='book'),
]
