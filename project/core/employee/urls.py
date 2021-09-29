from django.urls import path
from core.employee.views import *

urlpatterns = [
    path('empleado/list/', EmpleadoListView.as_view(), name='employee_list')
]