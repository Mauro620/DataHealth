from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from core.patients.forms import PatientsForm
from core.patients.models import *
from django.utils.decorators import method_decorator
# Create your views here.

class PacientesListView(ListView):
    model = patients
    template_name = 'PatientList.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'Listado de pacientes'
        return contex

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = { 'name' : patients.objects.name() }
        return JsonResponse(data)

class PacientesCreateView(CreateView):
    model = patients
    form_class = PatientsForm
    template_name = 'PatientsCreate.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'Registrar un paciente'
        return contex