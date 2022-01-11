from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('criar/', views.patients_create, name='patients_create'),
]