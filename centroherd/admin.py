from django.contrib import admin
from .models import Patients

class PatientsAdmin(admin.ModelAdmin):
    list_display  = ('name','cpf', 'created_at', 'updated_at', 'status', 'user')
    search_fields = ['name', 'cpf']

admin.site.register(Patients, PatientsAdmin)