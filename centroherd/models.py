from django.db import models

class Patients(models.Model):
 STATUS = (
   ('active', 'Ativo'),
   ('inactive', 'Inativo')
  )
  name = models.CharField(max_length=200)
  cpf = models.IntegerField()
  birthday = models.DateField(auto_now_add=False)
  created_at = models.DateField(auto_now_add=True)
  updated_at = models.DateField(auto_now=True)
  status = models.CharField(max_length=15, choices=STATUS)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
