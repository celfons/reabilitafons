from django.contrib import admin
from .models import Paciente, Psicologia, Social, Contato
from django_admin_inline_paginator.admin import TabularInlinePaginated

class PsicologiaInline(TabularInlinePaginated):
    model = Psicologia    
    per_page = 1
    readonly_fields=('usuario',)

class SocialInline(TabularInlinePaginated):
    model = Social    
    per_page = 1
    readonly_fields=('usuario',)

class ContatoInline(TabularInlinePaginated):
    model = Contato    
    per_page = 1
    readonly_fields=('usuario',)

class PacienteAdmin(admin.ModelAdmin):
    list_display  = ('nome','cpf', 'rg', 'telefone', 'nascimento', 'estado_civil', 'cor', 'filhos', 'profissao', 'escolaridade', 'pai', 'mae', 'naturalidade', 'endereco', 'bairro', 'cidade', 'bairro', 'cep', 'encaminhamento', 'inss', 'email', 'criado', 'atualizado', 'status', 'usuario')
    search_fields = ['nome', 'cpf', 'rg', 'status']
    readonly_fields=('usuario',)

    model = Paciente
    inlines = [
        ContatoInline,
        PsicologiaInline,
        SocialInline,
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