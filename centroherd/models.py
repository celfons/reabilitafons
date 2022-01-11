from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class Patients(models.Model):

    STATUS = (('active', 'Ativo'), ('inactive', 'Inativo'))
    name = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    status = models.CharField(max_length=15, choices=STATUS)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name = ("Paciente")
    def __str__(self):
        return self.name

class Record(models.Model):

    patients = models.ForeignKey(Patients, on_delete=models.CASCADE)
    medical = models.ForeignKey(Group, on_delete=models.CASCADE)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    class Meta:
        verbose_name = ("Prontuario")
