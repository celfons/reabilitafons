from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from django.dispatch import receiver
from django.core.mail import send_mail

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

@receiver(signals.post_save , sender=Paciente)
def paciente_criado(sender, instance, created, **kwargs):
    paciente = instance
    FilaPsicologia.objects.create(paciente=instance)
    FilaSocial.objects.create(paciente=instance)
    FilaEnfermagem.objects.create(paciente=instance)
    try:
        send_mail(
            '[EMAIL AUTOMATICO] Novo paciente cadastrado',
            'Novo paciente cadastrado, verifique sua fila para atendimento: https://reabilitafons.herokuapp.com',
            'reabilitafons@gmail.com',
            [paciente.usuario.email],
            fail_silently=False,
        )
    except:
        print("error")

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

@receiver(signals.post_save , sender=Psicologia)
def remove_fila_psicologia(sender, instance, created, **kwargs):
    try:
        paciente = instance.paciente
        fila = FilaPsicologia.objects.get(paciente=paciente)
        fila.delete()
    except:
        print("error")

class FilaPsicologia(models.Model):

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, unique=True)
    criado = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = ("Fila - Psicologia")
        verbose_name_plural = ("Fila - Psicologia")

class Social(models.Model):

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    acompanhamento = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado = models.DateField(auto_now_add=True)
    atualizado = models.DateField(auto_now=True)
    class Meta:
        verbose_name = ("Serviço Social - Prontuario")

@receiver(signals.post_save , sender=Social)
def remove_fila_social(sender, instance, created, **kwargs):
    try:
        paciente = instance.paciente
        fila = FilaSocial.objects.get(paciente=paciente)
        fila.delete()
    except:
        print("error")

class FilaSocial(models.Model):

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, unique=True)
    criado = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = ("Fila - Serviço Social")
        verbose_name_plural = ("Fila - Serviço Social")

class Enfermagem(models.Model):

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    possui_doenca_cronica = models.BooleanField(null=True)
    uso_medicacao_continua = models.BooleanField(null=True)
    possui_alergia_medicacao = models.BooleanField(null=True)
    tabagismo = models.BooleanField(null=True)
    etilismo = models.BooleanField(null=True)
    drogas = models.BooleanField(null=True)
    familia_diabetes = models.BooleanField(null=True)
    familia_hipertensao = models.BooleanField(null=True)
    exame_dst = models.BooleanField(null=True)
    acompanhamento = models.TextField(blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado = models.DateField(auto_now_add=True)
    atualizado = models.DateField(auto_now=True)
    class Meta:
        verbose_name = ("Enfermagem - Prontuario")

@receiver(signals.post_save , sender=Enfermagem)
def remove_fila_enfermagem(sender, instance, created, **kwargs):
    try:
        paciente = instance.paciente
        fila = FilaEnfermagem.objects.get(paciente=paciente)
        fila.delete()
    except:
        print("error")

class FilaEnfermagem(models.Model):

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, unique=True)
    criado = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = ("Fila - Enfermagem")
        verbose_name_plural = ("Fila - Enfermagem")

class Doenca_Cronica(models.Model):

    enfermagem = models.ForeignKey(Enfermagem, on_delete=models.CASCADE)
    DOENCA = (('hiv', 'HIV'), ('hipertensao', 'Hipertensao'), ('diabetes', 'Diabetes'), ('outra', 'Outra'))
    doenca = models.CharField(max_length=20, choices=DOENCA)
    outra = models.CharField(max_length=200, blank=True)
    constatada = models.DateField(auto_now_add=False, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado = models.DateField(auto_now_add=True)
    atualizado = models.DateField(auto_now=True)
    class Meta:
        verbose_name = ("Doença(s) Cronica")
        verbose_name_plural = ("Doença Cronica")

class Medicacao_Continua(models.Model):

    enfermagem = models.ForeignKey(Enfermagem, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado = models.DateField(auto_now_add=True)
    atualizado = models.DateField(auto_now=True)
    class Meta:
        verbose_name = ("Medicação Continua")
        verbose_name_plural = ("Medicação Continua")

class Alergia_Medicamento(models.Model):

    enfermagem = models.ForeignKey(Enfermagem, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado = models.DateField(auto_now_add=True)
    atualizado = models.DateField(auto_now=True)
    class Meta:
        verbose_name = ("Alergia Medicamento")
        verbose_name_plural = ("Alergia Medicamento")

class DST(models.Model):

    enfermagem = models.ForeignKey(Enfermagem, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    tratamento = models.BooleanField(null=True)
    constatada = models.DateField(auto_now_add=False, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado = models.DateField(auto_now_add=True)
    atualizado = models.DateField(auto_now=True)
    class Meta:
        verbose_name = ("DST")
        verbose_name_plural = ("DST")

