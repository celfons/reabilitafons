from django.forms import ModelForm
from .models import Patients

class PatientsForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'cpf', 'birthday', 'status']