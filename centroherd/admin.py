from django.contrib import admin
from .models import Patients
from .models import Record
from django.contrib.auth.models import Group

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

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        obj.medical = Group.objects.filter(user = request.user)[0]
        obj.save()

admin.site.register(Record, RecordAdmin)