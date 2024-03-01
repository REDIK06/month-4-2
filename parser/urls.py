from django.urls import path
from . import views

urlpatterns = [
    path('film_list/', views.CinematicaListView.as_view(), name='film_list'),
    path('get_parsing/', views.GetParsingForm.as_view(), name='get_parsing'),
]
