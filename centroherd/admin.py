from django.contrib import admin
from .models import Patients
from .models import Record

class PatientsAdmin(admin.ModelAdmin):
    list_display  = ('name','cpf', 'created_at', 'updated_at', 'status', 'user')
    search_fields = ['name', 'cpf']

admin.site.register(Patients, PatientsAdmin)

class RecordAdmin(admin.ModelAdmin):
    list_display  = ('name', 'medical', 'text', 'created_at', 'updated_at', 'user')
    search_fields = ['patients__name', 'medical__name']

    @admin.display
    def name(self, obj):
        return obj.patients.name

admin.site.register(Record, RecordAdmin)