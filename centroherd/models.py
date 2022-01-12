from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class Paciente(models.Model):

    STATUS = (('ativo', 'Ativo'), ('inativo', 'Inativo'))
    ESTADO = (('solteiro', 'Solteiro'), ('casado', 'Casado'), ('viuvo', 'Viuvo'), ('divorciado', 'Divorciado'))
    ESCOLARIDADE = (('analfabeto', 'Analfabeto'), ('infantil', 'Infantil'), ('primario', 'Primario'), ('fundamental', 'Fundamental'), ('medio', 'Medio'), ('superior', 'Superior'), ('desconhecido', 'Desconhecido'))
    nome = models.CharField(max_length=200)
    cpf = models.BigIntegerField(unique=True)
    rg = models.BigIntegerField(unique=True)
    telefone = models.BigIntegerField(blank=True, null=True)
    nascimento = models.DateField(auto_now_add=False, blank=True, null=True)
    estado_civil = models.CharField(max_length=15, choices=ESTADO, blank=True)
    cor = models.CharField(max_length=20, blank=True)
    filhos = models.BooleanField(null=True)
    profissao = models.CharField(max_length=100, blank=True)
    escolaridade = models.CharField(max_length=15, choices=ESCOLARIDADE, blank=True)
    pai = models.CharField(max_length=200, blank=True)
    mae = models.CharField(max_length=200, blank=True)
    naturalidade = models.CharField(max_length=50, blank=True)
    endereco = models.CharField(max_length=50, blank=True)
    bairro = models.CharField(max_length=50, blank=True)
    cidade = models.CharField(max_length=50, blank=True)
    cep = models.BigIntegerField(blank=True, null=True)
    encaminhamento = models.CharField(max_length=200, blank=True)
    inss = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    criado = models.DateField(auto_now_add=True)
    atualizado = models.DateField(auto_now=True)
    status = models.CharField(max_length=15, choices=STATUS)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)

    def __str__(self):
        return self.nome

class Contato(models.Model):

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    parentesco = models.CharField(max_length=100)
    telefone = models.BigIntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado = models.DateField(auto_now_add=True)
    atualizado = models.DateField(auto_now=True)
    class Meta:
        verbose_name = ("Telefones de Contato")

class Psicologia(models.Model):

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    acompanhamento = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado = models.DateField(auto_now_add=True)
    atualizado = models.DateField(auto_now=True)
    class Meta:
        verbose_name = ("Psicologia - Prontuario")

class Social(models.Model):

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    acompanhamento = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado = models.DateField(auto_now_add=True)
    atualizado = models.DateField(auto_now=True)
    class Meta:
        verbose_name = ("Serviço Social - Prontuario")