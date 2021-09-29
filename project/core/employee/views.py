from django.shortcuts import render
from django.views.generic import ListView
from core.employee.models import employee

# Create your views here.
#class EmployeeListView(ListView):
 #   model = employee
  #  template_name = 'empleado.html'

class EmpleadoListView(ListView):
    model = employee
    template_name = 'employeeList.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'Listado Empleados'
        return contex