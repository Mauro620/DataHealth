from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, _get_queryset
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
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
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado Empleados'
        return context

    def seleccionEmpleado(self, selected, deselected):
        indexes = selected.indexes()
        if len(indexes)>0:
            item = self.request.employee.model().itemFromIndex(index[0])




class EmpleadoCreateView(CreateView):
    model = employee
    form_class = EmployeeForm
    template_name = 'EmployeeCreate.html'
    success_url = reverse_lazy('employee_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registrar Empleado'
        return context

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
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Empleado'
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('employee_list')
        context['entity'] = 'Empleados'
        return context

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
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Empleado'
        context['list_url'] = reverse_lazy('employee_list')
        context['entity'] = 'Empleados'
        return context

class EmpleadoTemplateView(ListView):
    template_name = 'empleado_completo.html'
    model = employee

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Empleado'
        return context

    def get_queryset(self):
        qs = employee.objects.all()
        employeeModel = self.request.GET.get("ident")
        if employeeModel:
            qs = qs.filter(gender = employeeModel)
        return qs



