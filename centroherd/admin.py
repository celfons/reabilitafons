from django.contrib import admin
from .models import Paciente, Psicologia, Social, Contato, Enfermagem, Doenca_Cronica, Medicacao_Continua, Alergia_Medicamento, DST, FilaPsicologia, FilaSocial, FilaEnfermagem, HistoricoDroga, PlanoAcao, HistoricoTratamento, Medicina, FilaMedicina, TratamentosAnteriores, Sintomas, AmbientesConsumo, SinalizadoresProblematicosDescorrentes, HistoricoDrogaPsicologia
from django_admin_inline_paginator.admin import TabularInlinePaginated

class PsicologiaInline(TabularInlinePaginated):
    model = Psicologia    
    per_page = 1
    readonly_fields=('usuario',)
    ordering = ('-criado',)

class MedicinaInline(TabularInlinePaginated):
    model = Medicina    
    per_page = 1
    readonly_fields=('usuario',)
    ordering = ('-criado',)

class SocialInline(TabularInlinePaginated):
    model = Social    
    per_page = 1
    readonly_fields=('usuario',)
    ordering = ('-criado',)

class ContatoInline(TabularInlinePaginated):
    model = Contato    
    per_page = 1
    readonly_fields=('usuario',)
    ordering = ('-criado',)

class EnfermagemInline(TabularInlinePaginated):
    model = Enfermagem    
    per_page = 1
    readonly_fields=('usuario',)
    ordering = ('-criado',)

class PacienteAdmin(admin.ModelAdmin):
    list_display  = ('nome','cpf', 'rg', 'convenio', 'telefone', 'nascimento', 'estado_civil', 'cor', 'filhos', 'profissao', 'escolaridade', 'pai', 'mae', 'naturalidade', 'endereco', 'bairro', 'cidade', 'bairro', 'cep', 'encaminhamento', 'inss', 'email', 'unidade','criado', 'atualizado', 'status', 'usuario')
    search_fields = ['nome', 'cpf', 'rg']
    readonly_fields=('usuario',)

    model = Paciente
    inlines = [
        ContatoInline,
        PsicologiaInline,
        MedicinaInline,
        SocialInline,
        EnfermagemInline,
    ]

    def save_model(self, request, obj, form, change): 
        obj.usuario = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        for form in formset.forms:
            form.instance.usuario = request.user
        formset.save()

admin.site.register(Paciente, PacienteAdmin)


class TratamentosAnterioresInline(TabularInlinePaginated):
    model = TratamentosAnteriores    
    per_page = 1
    readonly_fields=('usuario',)
    ordering = ('-criado',)

class SintomasInline(TabularInlinePaginated):
    model = Sintomas    
    per_page = 1
    readonly_fields=('usuario',)
    ordering = ('-criado',)

class AmbientesConsumoInline(TabularInlinePaginated):
    model = AmbientesConsumo    
    per_page = 1
    readonly_fields=('usuario',)
    ordering = ('-criado',)

class SinalizadoresProblematicosDescorrentesInline(TabularInlinePaginated):
    model = SinalizadoresProblematicosDescorrentes    
    per_page = 1
    readonly_fields=('usuario',)
    ordering = ('-criado',)

class HistoricoDrogaPsicologiaInline(TabularInlinePaginated):
    model = HistoricoDrogaPsicologia    
    per_page = 1
    readonly_fields=('usuario',)
    ordering = ('-criado',)

class PsicologiaAdmin(admin.ModelAdmin):
    list_display  = ('nome', 'condicoes_moradia','demanda_atendimento','se_empresa','motivo_demanda','situacao_atual','usuario_espera_tratamento','tratamento_anterior','frequencia_e_locais','sintoma_ao_chegar','outros_sintomas','droga_intravenosa','overdose_por_essas_drogas','overdose_droga_e_frequencia','situacao_que_faz_o_uso','reacoes_da_droga','saude','sono','alimentacao','alucinacao_com_droga','alucinacao_sem_droga','desmaio_convulcao_com_droga','desmaio_convulcao_sem_droga','toma_alguma_medicacao','quais_medicacoes','critica_situacao','desemprego','dificuldade_ter_manter_vinculos_sociais','dificuldade_de_gerir_propria_vida','problemas_familiares','agressividade','problemas_ambiente_trabalho','problemas_legais_juridicos_existentes_ou_pendentes','quais_problemas_legais_juridicos','ultimo_episodio_de_consumo','tempo_abstitencia','quantidade_consumida','via_administracao_escolhida','frequencia_consumo_ultimos_meses','parecer_tecnico','hipoteses_diagnosticas','metas_atividades_terapeuticas','fatores_de_risco_e_mantenedores_da_dependencia','fatores_de_protecao_e_prognosticos_da_dependencia', 'criado', 'atualizado', 'usuario')
    search_fields = ['paciente__nome']
    autocomplete_fields = ['paciente']
    readonly_fields=('usuario',)

    model = Psicologia
    inlines = [
        TratamentosAnterioresInline,
        SintomasInline,
        AmbientesConsumoInline,
        SinalizadoresProblematicosDescorrentesInline,
        HistoricoDrogaPsicologiaInline,
    ]

    @admin.display
    def nome(self, obj):
        return obj.paciente.nome

    def save_model(self, request, obj, form, change): 
        obj.usuario = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        for form in formset.forms:
            form.instance.usuario = request.user
        formset.save()

admin.site.register(Psicologia, PsicologiaAdmin)

class FilaPsicologiaAdmin(admin.ModelAdmin):
    list_display  = ('nome', 'criado')
    search_fields = ['paciente__nome']
    autocomplete_fields = ['paciente']
    ordering = ('-criado',)

    @admin.display
    def nome(self, obj):
        return obj.paciente.nome

admin.site.register(FilaPsicologia, FilaPsicologiaAdmin)

class HistoricoDrogaInline(TabularInlinePaginated):
    model = HistoricoDroga    
    per_page = 1
    readonly_fields=('usuario',)
    ordering = ('-criado',)

class PlanoAcaoInline(TabularInlinePaginated):
    model = PlanoAcao    
    per_page = 1
    readonly_fields=('usuario',)
    ordering = ('-criado',)

class HistoricoTratamentoInline(TabularInlinePaginated):
    model = HistoricoTratamento    
    per_page = 1
    readonly_fields=('usuario',)
    ordering = ('-criado',)

class SocialAdmin(admin.ModelAdmin):
    list_display  = ('nome', 'modalidade_atencao_orientada', 'situacao_profissional', 'possui_renda', 'problemas_com_justica', 'problemas_com_justica_observacao', 'relacao_familiar', 'relato_caso', 'problemas_causados_pela_droga', 'familiar_com_historico_de_uso', 'observacao', 'criado', 'atualizado', 'usuario')
    search_fields = ['paciente__nome']
    autocomplete_fields = ['paciente']
    readonly_fields=('usuario',)

    model = Social
    inlines = [
        HistoricoDrogaInline,
        PlanoAcaoInline,
        HistoricoTratamentoInline,
    ]

    @admin.display
    def nome(self, obj):
        return obj.paciente.nome

    def save_model(self, request, obj, form, change): 
        obj.usuario = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        for form in formset.forms:
            form.instance.usuario = request.user
        formset.save()

admin.site.register(Social, SocialAdmin)

class FilaSocialAdmin(admin.ModelAdmin):
    list_display  = ('nome', 'criado')
    search_fields = ['paciente__nome']
    autocomplete_fields = ['paciente']
    ordering = ('-criado',)

    @admin.display
    def nome(self, obj):
        return obj.paciente.nome

admin.site.register(FilaSocial, FilaSocialAdmin)

class DoencaCronicaInline(TabularInlinePaginated):
    model = Doenca_Cronica    
    per_page = 1
    readonly_fields=('usuario',)
    ordering = ('-criado',)

class MedicacaoContinuaInline(TabularInlinePaginated):
    model = Medicacao_Continua    
    per_page = 1
    readonly_fields=('usuario',)
    ordering = ('-criado',)

class AlergiaMedicamentoInline(TabularInlinePaginated):
    model = Alergia_Medicamento    
    per_page = 1
    readonly_fields=('usuario',)
    ordering = ('-criado',)

class DSTInline(TabularInlinePaginated):
    model = DST    
    per_page = 1
    readonly_fields=('usuario',)    
    ordering = ('-criado',)

class EnfermagemAdmin(admin.ModelAdmin):
    list_display  = ('nome','possui_doenca_cronica', 'uso_medicacao_continua', 'possui_alergia_medicacao', 'tabagismo', 'etilismo', 'drogas', 'familia_diabetes', 'familia_hipertensao', 'exame_dst', 'acompanhamento')
    search_fields = ['paciente__nome']
    autocomplete_fields = ['paciente']
    readonly_fields=('usuario',)

    model = Enfermagem
    inlines = [
        DoencaCronicaInline,
        MedicacaoContinuaInline,
        AlergiaMedicamentoInline,
        DSTInline,
    ]

    @admin.display
    def nome(self, obj):
        return obj.paciente.nome
        
    def save_model(self, request, obj, form, change): 
        obj.usuario = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        for form in formset.forms:
            form.instance.usuario = request.user
        formset.save()

admin.site.register(Enfermagem, EnfermagemAdmin)

class FilaEnfermagemAdmin(admin.ModelAdmin):
    list_display  = ('nome', 'criado')
    search_fields = ['paciente__nome']
    autocomplete_fields = ['paciente']
    ordering = ('-criado',)

    @admin.display
    def nome(self, obj):
        return obj.paciente.nome

admin.site.register(FilaEnfermagem, FilaEnfermagemAdmin)

class MedicinaAdmin(admin.ModelAdmin):
    list_display  = ('nome', 'acompanhamento', 'criado', 'atualizado', 'usuario')
    search_fields = ['paciente__nome']
    autocomplete_fields = ['paciente']
    readonly_fields=('usuario',)

    @admin.display
    def nome(self, obj):
        return obj.paciente.nome

    def save_model(self, request, obj, form, change): 
        obj.usuario = request.user
        obj.save()

admin.site.register(Medicina, MedicinaAdmin)

class FilaMedicinaAdmin(admin.ModelAdmin):
    list_display  = ('nome', 'criado')
    search_fields = ['paciente__nome']
    autocomplete_fields = ['paciente']
    ordering = ('-criado',)

    @admin.display
    def nome(self, obj):
        return obj.paciente.nome

admin.site.register(FilaMedicina, FilaMedicinaAdmin)