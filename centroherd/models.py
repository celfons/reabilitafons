from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

class Paciente(models.Model):
    UNIDADE = (('1', 'Unidade 1'), ('2', 'Unidade 2'))
    CONVENIO = (('senapred', 'SENAPRED'), ('comad', 'COMAD'), ('sem', 'Sem convênio'))
    STATUS = (('ativo', 'Ativo'), ('inativo', 'Inativo'))
    ESTADO = (('solteiro', 'Solteiro'), ('casado', 'Casado'), ('viuvo', 'Viuvo'), ('divorciado', 'Divorciado'))
    ESCOLARIDADE = (('analfabeto', 'Analfabeto'), ('infantil', 'Infantil'), ('primario', 'Primario'), ('fundamental', 'Fundamental'), ('medio', 'Medio'), ('superior', 'Superior'), ('desconhecido', 'Desconhecido'))
    nome = models.CharField(max_length=200)
    cpf = models.BigIntegerField(unique=True)
    rg = models.BigIntegerField(unique=True)
    convenio = models.CharField(max_length=10, choices=CONVENIO)
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
    cartao_sus = models.CharField(max_length=100, blank=True)
    reservista = models.CharField(max_length=100, blank=True)
    titulo_eleitor = models.CharField(max_length=100, blank=True)
    carteira_trabalho = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    unidade = models.CharField(max_length=2, choices=UNIDADE, default=1)
    criado = models.DateField(auto_now_add=True)
    atualizado = models.DateField(auto_now=True)
    status = models.CharField(max_length=15, choices=STATUS)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)

    def __str__(self):
        return self.nome

@receiver(signals.post_save , sender=Paciente)
def paciente_criado(sender, instance, created, **kwargs):
    paciente = instance
    if created is True:
        FilaPsicologia.objects.create(paciente=instance)
        FilaSocial.objects.create(paciente=instance)
        FilaEnfermagem.objects.create(paciente=instance)
        try:          
            User = get_user_model()
            users = User.objects.all()
            for user in users:
                if user.email == '':
                    print("não tem email")
                else:
                    send_mail(
                        '[EMAIL AUTOMATICO] Novo paciente cadastrado',
                        'Novo paciente cadastrado, verifique sua fila para atendimento: https://reabilitafons.herokuapp.com',
                        'reabilitafons@gmail.com',
                        [user.email],
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
    MORADIA = (('so', 'So'), ('pais', 'Pais'), ('familiares', 'Esposa/Filhos'), ('alojamento', 'Alojamento'), ('amigos', 'Amigos'), ('parentes', 'Parentes'), ('outros', 'Outros'))
    DEMANDA = (('propria', 'Propria'), ('familiares', 'Familiares'), ('amigos', 'Amigos'), ('empresa', 'Empresa'))
    DEMANDA_EMPRESA = (('testagem', 'Testagem Positiva'), ('espontanea', 'Demanda Espontanea'), ('servico_saude', 'Demanda Serviço Saúde'))
    SITUACAO = (('excelente', 'Excelente'), ('muito_bom', 'Muito Bom(a)'), ('bom', 'Bom(a)'), ('razoavel', 'Razoavel'), ('ruim', 'Ruim'), ('pessimo', 'Péssimo(a)'))
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    condicoes_moradia = models.CharField(max_length=15, choices=MORADIA, blank=True)
    demanda_atendimento = models.CharField(max_length=20, choices=DEMANDA, blank=True)
    se_empresa = models.CharField(max_length=20, choices=DEMANDA_EMPRESA, blank=True)
    motivo_demanda = models.TextField(blank=True)
    situacao_atual = models.TextField(blank=True)
    usuario_espera_tratamento = models.TextField(blank=True)
    tratamento_anterior = models.BooleanField(null=True, blank=True)
    frequencia_e_locais = models.TextField(blank=True)
    sintoma_ao_chegar = models.BooleanField(null=True, blank=True)
    outros_sintomas = models.TextField(blank=True)
    droga_intravenosa = models.BooleanField(null=True, blank=True)
    overdose_por_essas_drogas = models.BooleanField(null=True, blank=True)
    overdose_droga_e_frequencia = models.TextField(blank=True)
    situacao_que_faz_o_uso = models.TextField(blank=True)
    reacoes_da_droga = models.TextField(blank=True)
    saude = models.TextField(blank=True)
    sono = models.TextField(blank=True)
    alimentacao = models.TextField(blank=True)
    alucinacao_com_droga = models.BooleanField(null=True, blank=True)
    alucinacao_sem_droga = models.BooleanField(null=True, blank=True)
    desmaio_convulcao_com_droga = models.BooleanField(null=True, blank=True)
    desmaio_convulcao_sem_droga = models.BooleanField(null=True, blank=True)
    toma_alguma_medicacao = models.BooleanField(null=True, blank=True)
    quais_medicacoes = models.TextField(blank=True)
    critica_situacao = models.CharField(max_length=20, choices=SITUACAO, blank=True)
    desemprego = models.BooleanField(null=True, blank=True)
    dificuldade_ter_manter_vinculos_sociais = models.BooleanField(null=True, blank=True)
    dificuldade_de_gerir_propria_vida = models.BooleanField(null=True, blank=True)
    problemas_familiares = models.BooleanField(null=True, blank=True)
    agressividade = models.BooleanField(null=True, blank=True)
    problemas_ambiente_trabalho = models.BooleanField(null=True, blank=True)
    problemas_legais_juridicos_existentes_ou_pendentes = models.BooleanField(null=True, blank=True)
    quais_problemas_legais_juridicos = models.TextField(blank=True)
    ultimo_episodio_de_consumo = models.CharField(max_length=100, null=True, blank=True)
    tempo_abstitencia = models.CharField(max_length=100, null=True, blank=True)
    quantidade_consumida = models.CharField(max_length=100, null=True, blank=True)
    via_administracao_escolhida = models.CharField(max_length=100, null=True, blank=True)
    frequencia_consumo_ultimos_meses = models.CharField(max_length=100, null=True, blank=True)
    parecer_tecnico = models.TextField(blank=True)
    hipoteses_diagnosticas = models.TextField(blank=True)
    metas_atividades_terapeuticas = models.TextField(blank=True)
    fatores_de_risco_e_mantenedores_da_dependencia = models.TextField(blank=True)
    fatores_de_protecao_e_prognosticos_da_dependencia = models.TextField(blank=True)
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


class TratamentosAnteriores(models.Model):
    TRATAMENTO = (('psiquiatrico', 'Psiquiatrico'), ('medico_clinico', 'Medico Clinico'), ('psicoterapico', 'Psicoterapico'), ('psicanalitico', 'Psicanalitico'), ('grupo_ajuda_mutua', 'Grupo de Ajuda Mútua'), ('religioso', 'Religioso'), ('comunidade_terapeutica', 'Comunidade Terapeutica'), ('outros', 'Outros'))
    psicologia = models.ForeignKey(Psicologia, on_delete=models.CASCADE)
    tratamento = models.CharField(max_length=100, choices=TRATAMENTO)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado = models.DateField(auto_now_add=True)
    atualizado = models.DateField(auto_now=True)
    class Meta: 
        verbose_name_plural = ("Tratamentos Anteriores")

class Sintomas(models.Model):
    SINTOMAS = (('tosse', 'Tosse'), ('dispneia', 'Dispenia/Falta de ar'), ('dor', 'Dor'), ('febre', 'Febre'), ('emagrecimento', 'Emagrecimento'), ('lesao_da_pele', 'Lesao da Pele'), ('diarreia', 'Diarreia'), ('nausea_vomito', 'Nausea/Vomito'), ('fraqueza', 'Fraqueza Muscular'), ('tremores', 'Tremores'), ('dificuldade_locomocao', 'Dificuldade de locomoção'), ('outros', 'Outros'))
    psicologia = models.ForeignKey(Psicologia, on_delete=models.CASCADE)
    sintomas = models.CharField(max_length=100, choices=SINTOMAS)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado = models.DateField(auto_now_add=True)
    atualizado = models.DateField(auto_now=True)
    class Meta: 
        verbose_name_plural = ("Sintomas")

class AmbientesConsumo(models.Model):
    Ambientes = (('festas', 'Festas'), ('rua', 'Rua'), ('amigos', 'Amigos'), ('casa', 'Casa'), ('trabalho', 'Trabalho'), ('com_desconhecidos', 'Com Desconhecidos'), ('sozinho', 'Sozinho'))
    psicologia = models.ForeignKey(Psicologia, on_delete=models.CASCADE)
    ambientes_consumo = models.CharField(max_length=100, choices=Ambientes)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado = models.DateField(auto_now_add=True)
    atualizado = models.DateField(auto_now=True)
    class Meta: 
        verbose_name_plural = ("Ambientes de Consumo")

class SinalizadoresProblematicosDescorrentes(models.Model):
    SINALIZADORES = (('faltas_frequentes', 'Faltas Frequentes no trabalho'), ('depressao', 'Depressao'), ('historia_de_trauma', 'Historia de Trauma'), ('ansiedade', 'Ansiedade'), ('hipertensao', 'Hipertensao'), ('sintoma_gastro', 'Sintoma GastroIntestinal'), ('disturbio_sono', 'Disturbio do sono'), ('disfuncao_sexual', 'Disfunção Sexual'), ('hemorragias', 'Hemorragias'))
    psicologia = models.ForeignKey(Psicologia, on_delete=models.CASCADE) 
    sinalizadores_problematicos_decorrentes_ao_uso = models.CharField(max_length=100, choices=SINALIZADORES)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado = models.DateField(auto_now_add=True)
    atualizado = models.DateField(auto_now=True)
    class Meta: 
        verbose_name_plural = ("Sinalizadores Problematicos Decorrentes ao uso de alcool e drogas")

class HistoricoDrogaPsicologia(models.Model):
    DROGA = (('alcool', 'Alcool'), ('crack', 'Crack'), ('maconha', 'Maconha/Haxixe'), ('cocaina', 'Cocaina'), ('inalante', 'Inalante/Cola'), ('diazepan', 'Diazepan'), ('anfetamina', 'Anfetamina/Remedio p/ Emagrecer'), ('ecstasy', 'Ecstasy/MDMA'), ('lsd', 'LSD'), ('heroina', 'Heroina'), ('tabaco', 'Tabaco'), ('outros', 'Outros'))
    FREQUENCIA = (('diaria', 'Diaria'), ('semanal', 'Semanal'), ('mensal', 'Mensal'), ('fds', 'Fim de Semana'))
    PERIODO = (('manha', 'Manhã'), ('tarde', 'Tarde'), ('noite', 'Noite'))
    USO = (('oral', 'Oral'), ('inalada', 'Inalada'), ('fumada', 'Fumada'), ('injetada', 'Injetada'))
    psicologia = models.ForeignKey(Psicologia, on_delete=models.CASCADE) 
    droga = models.CharField(max_length=100, choices=DROGA)
    idade_primeiro_uso = models.BigIntegerField()
    idade_ultima_vez = models.BigIntegerField()
    frenquencia = models.CharField(max_length=100, choices=FREQUENCIA)
    quando_usa = models.CharField(max_length=100, choices=PERIODO)
    vias_de_uso = models.CharField(max_length=100, choices=USO)
    quantidade = models.BigIntegerField()
    observacoes = models.TextField(blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado = models.DateField(auto_now_add=True)
    atualizado = models.DateField(auto_now=True)
    class Meta: 
        verbose_name_plural = ("Histórico de Drogas")

class Social(models.Model):
    JUSTICA = (('sim', 'Sim'), ('nao', 'Não'), ('ns', 'N.S'))
    FAMILIAR = (('fortalecidos', 'Fortalecidos'), ('fragilizados', 'Fragilizados'), ('rompidos', 'Rompidos'), ('ns', 'N.S'), ('nr', 'N.R'))
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    modalidade_atencao_orientada = models.CharField(max_length=200, blank=True)
    situacao_profissional = models.CharField(max_length=200, blank=True)
    possui_renda = models.BooleanField(null=True, blank=True)
    problemas_com_justica = models.CharField(max_length=5, choices=JUSTICA, blank=True)
    problemas_com_justica_observacao = models.TextField(blank=True)
    relacao_familiar = models.CharField(max_length=12, choices=FAMILIAR, blank=True)
    relato_caso = models.TextField(blank=True)
    problemas_causados_pela_droga = models.TextField(blank=True)
    familiar_com_historico_de_uso = models.TextField(blank=True)
    observacao = models.TextField(blank=True)
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

class HistoricoDroga(models.Model):
    DROGA = (('alcool', 'Alcool'), ('crack', 'Crack'), ('maconha', 'Maconha/Haxixe'), ('cocaina', 'Cocaina'), ('inalante', 'Inalante/Cola'), ('diazepan', 'Diazepan'), ('anfetamina', 'Anfetamina/Remedio p/ Emagrecer'), ('ecstasy', 'Ecstasy/MDMA'), ('lsd', 'LSD'), ('heroina', 'Heroina'), ('tabaco', 'Tabaco'), ('outros', 'Outros'))
    social = models.ForeignKey(Social, on_delete=models.CASCADE)
    droga = models.CharField(max_length=100, choices=DROGA)
    quantas_vezes_interrompeu_uso = models.BigIntegerField()
    observacoes = models.TextField(blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado = models.DateField(auto_now_add=True)
    atualizado = models.DateField(auto_now=True)
    class Meta: 
        verbose_name_plural = ("Histórico de Drogas")

class PlanoAcao(models.Model):
    social = models.ForeignKey(Social, on_delete=models.CASCADE)
    demandas = models.TextField(blank=True)
    previsao = models.DateField(auto_now_add=False, blank=True, null=True)
    observacao = models.TextField(blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado = models.DateField(auto_now_add=True)
    atualizado = models.DateField(auto_now=True)
    class Meta:
        verbose_name_plural = ("Plano de Ações")

class HistoricoTratamento(models.Model):
    social = models.ForeignKey(Social, on_delete=models.CASCADE)
    instituicao = models.CharField(max_length=200)
    periodo_inicial = models.DateField(blank=True)
    periodo_final = models.DateField(blank=True)
    observacao = models.TextField(blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado = models.DateField(auto_now_add=True)
    atualizado = models.DateField(auto_now=True)
    class Meta:
        verbose_name_plural = ("Histortico de Tratamentos")


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

class Medicina(models.Model):

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    acompanhamento = models.TextField(blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    criado = models.DateField(auto_now_add=True)
    atualizado = models.DateField(auto_now=True)
    class Meta:
        verbose_name = ("Medicina - Prontuario")

@receiver(signals.post_save , sender=Medicina)
def remove_fila_medicina(sender, instance, created, **kwargs):
    try:
        paciente = instance.paciente
        fila = FilaMedicina.objects.get(paciente=paciente)
        fila.delete()
    except:
        print("error")

class FilaMedicina(models.Model):

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, unique=True)
    criado = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name = ("Fila - Medicina")
        verbose_name_plural = ("Fila - Medicina")