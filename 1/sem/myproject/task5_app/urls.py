from django.urls import path
from . import views

urlpatterns = [
    path('orel/', views.orel, name='orel-reshka'),
    path('kubik/', views.kubik, name='kubik'),
    path('number/', views.number, name='number'),
]