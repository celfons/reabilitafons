from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Patients
from .forms import PatientsForm

def home(request):
	return render(request, 'centroherd/home.html')

@login_required
def patients_list(request):
    patients_list = Patients.objects.all().order_by('-created_at')
    paginator = Paginator(patients_list, 3)

    page = request.GET.get('page')
    patients = paginator.get_page(page)
    return render(request, 'centroherd/list_patients.html', {'patients':patients})

@login_required
def patients_create(request):
	form = PatientsForm()

	if(request.method == 'POST'):

		form = PatientsForm(request.POST)

		if(form.is_valid()):
			patients_name = form.cleaned_data['name']
			patients_cpf = form.cleaned_data['cpf']
			patients_status = form.cleaned_data['status']
			patients_user = form.cleaned_data['user']

			new_patients = Patients(name=patients_name, cpf=patients_cpf, user=patients_user, status=patients_status)
			new_patients.save()

			return redirect('centroherd:patients_list')

	elif(request.method == 'GET'):
		return render(request, 'centroherd/add_patients.html', {'form': form})
