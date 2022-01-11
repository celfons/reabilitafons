from django.urls import path
from . import views

app_name = 'centroherd'

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastrar-pacientes/', views.patients_create, name='patients_create'),
    path('listar-pacientes/', views.patients_list, name='patients_list'),
]