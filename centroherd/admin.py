from django.contrib import admin
from .models import Paciente, Psicologia, Social, Contato, Enfermagem, Doenca_Cronica, Medicacao_Continua, Alergia_Medicamento, DST, FilaPsicologia, FilaSocial, FilaEnfermagem
from django_admin_inline_paginator.admin import TabularInlinePaginated

class PsicologiaInline(TabularInlinePaginated):
    model = Psicologia    
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
    list_display  = ('nome','cpf', 'rg', 'telefone', 'nascimento', 'estado_civil', 'cor', 'filhos', 'profissao', 'escolaridade', 'pai', 'mae', 'naturalidade', 'endereco', 'bairro', 'cidade', 'bairro', 'cep', 'encaminhamento', 'inss', 'email', 'criado', 'atualizado', 'status', 'usuario')
    search_fields = ['nome', 'cpf', 'rg']
    readonly_fields=('usuario',)

    model = Paciente
    inlines = [
        ContatoInline,
        PsicologiaInline,
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

class PsicologiaAdmin(admin.ModelAdmin):
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

class SocialAdmin(admin.ModelAdmin):
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