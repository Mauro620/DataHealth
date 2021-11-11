from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
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
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de pacientes'
        return context

    @method_decorator(csrf_exempt)
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {'name': patients.objects.name()}
        return JsonResponse(data)


class PacientesCreateView(CreateView):
    model = patients
    form_class = PatientsForm
    template_name = 'PatientsCreate.html'
    success_url = reverse_lazy('Patients')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registrar un paciente'
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class PacientesUpdateView(UpdateView):
    model = patients
    form_class = PatientsForm
    template_name = 'PatientsCreate.html'
    success_url = reverse_lazy('Patients')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar un paciente'
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('Patients')
        context['entity'] = 'Pacientes'
        return context


class PacientesDeleteView(DeleteView):
    model = patients
    template_name = 'PatientsDelete.html'
    success_url = reverse_lazy('Patients')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar paciente'
        context['list_url'] = reverse_lazy('Patients')
        context['entity'] = 'Pacientes'
        return context
