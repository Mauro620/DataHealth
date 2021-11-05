from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from core.employee.forms import EmployeeForm
from core.employee.models import employee
from django.contrib import messages


# Create your views here.
class EmpleadoListView(ListView):
    model = employee
    template_name = 'employeeList.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = employee.objects.get(pk=request.POST['id_empleado']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

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

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class EmpleadoUpdateView(UpdateView):
    model = employee
    form_class = EmployeeForm
    template_name = 'EmployeeCreate.html'
    success_url = reverse_lazy('employee_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'Editar Empleado'
        contex['action'] = 'edit'
        contex['list_url'] = reverse_lazy('employee_list')
        contex['entity'] = 'Empleados'
        return contex


class EmpleadoDeleteView(SuccessMessageMixin, DeleteView):
    model = employee
    template_name = 'EmployeeDelete.html'
    success_url = reverse_lazy('employee_list')
    success_message = "Eliminado con exito"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data
        )

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'Eliminar Empleado'
        contex['list_url'] = reverse_lazy('employee_list')
        contex['entity'] = 'Empleados'
        return contex
