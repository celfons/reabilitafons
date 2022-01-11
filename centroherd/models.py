from django.db import models
from django.contrib.auth.models import User

class Patients(models.Model):

    STATUS = (('active', 'Ativo'), ('inactive', 'Inativo'))
    name = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    status = models.CharField(max_length=15, choices=STATUS)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
