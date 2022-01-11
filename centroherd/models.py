from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class Patients(models.Model):

    STATUS = (('active', 'Ativo'), ('inactive', 'Inativo'))
    name = models.CharField(max_length=200)
    cpf = models.IntegerField(unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    status = models.CharField(max_length=15, choices=STATUS)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    class Meta:
        verbose_name = ("Paciente")
    def __str__(self):
        return self.name

class Psychology(models.Model):

    patients = models.ForeignKey(Patients, on_delete=models.CASCADE)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    class Meta:
        verbose_name = ("Psicologia - Prontuario")

class Social(models.Model):

    patients = models.ForeignKey(Patients, on_delete=models.CASCADE)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    class Meta:
        verbose_name = ("Serviço Social - Prontuario")