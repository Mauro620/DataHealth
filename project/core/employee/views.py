from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from core.employee.forms import EmployeeForm
from core.employee.models import employee

# Create your views here.
class EmpleadoListView(ListView):
    model = employee
    template_name = 'employeeList.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'Listado Empleados'
        return contex

class EmpleadoCreateView(CreateView):
    model = employee
    form_class = EmployeeForm
    template_name = 'EmployeeCreate.html'
    success_url = reverse_lazy('employee_list')

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'Registrar Empleado'
        return contex

class EmpleadoUpdateView(UpdateView):
    model = employee
    form_class = EmployeeForm
    template_name = 'EmployeeCreate.html'
    success_url = reverse_lazy('employee_list')

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'Editar Empleado'
        contex['action'] = 'edit'
        contex['list_url'] = reverse_lazy('employee_list')
        contex['entity'] = 'Empleados'
        return contex
