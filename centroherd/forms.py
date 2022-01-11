from django.forms import ModelForm
from .models import Patients

class PatientsForm(ModelForm):
    class Meta:
        model = Patients
        fields = ['name', 'cpf', 'status', 'user']