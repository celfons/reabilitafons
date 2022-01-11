from django.contrib import admin
from .models import Patients, Psychology, Social
from django_admin_inline_paginator.admin import TabularInlinePaginated

class PsychologyInline(TabularInlinePaginated):
    model = Psychology    
    per_page = 1

class SocialInline(TabularInlinePaginated):
    model = Social    
    per_page = 1

class PatientsAdmin(admin.ModelAdmin):
    list_display  = ('name','cpf', 'created_at', 'updated_at', 'status', 'user')
    search_fields = ['name', 'cpf']

    model = Patients
    inlines = [
        PsychologyInline,
        SocialInline,
    ]

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()

admin.site.register(Patients, PatientsAdmin)

class PsychologyAdmin(admin.ModelAdmin):
    list_display  = ('name', 'text', 'created_at', 'updated_at', 'user')
    search_fields = ['patients__name']
    autocomplete_fields = ['patients']
    readonly_fields=('user',)

    @admin.display
    def name(self, obj):
        return obj.patients.name

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()

admin.site.register(Psychology, PsychologyAdmin)

class SocialAdmin(admin.ModelAdmin):
    list_display  = ('name', 'text', 'created_at', 'updated_at')
    search_fields = ['patients__name']
    autocomplete_fields = ['patients']
    readonly_fields=('user',)

    @admin.display
    def name(self, obj):
        return obj.patients.name

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.save()

admin.site.register(Social, SocialAdmin)