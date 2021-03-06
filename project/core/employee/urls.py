from django.urls import path
from core.employee.views import *

urlpatterns = [
    path('empleado/list/', EmpleadoListView.as_view(), name='employee_list'),
    path('empleado/register/', EmpleadoCreateView.as_view(), name='employee_create'),
    path('empleado/edit/<int:pk>/', EmpleadoUpdateView.as_view(), name='employee_update'),
    path('empleado/delete/<int:pk>/', EmpleadoDeleteView.as_view(), name='employee_delete'),
    path('empleado/complete/', EmpleadoTemplateView.as_view(), name='employee_complete'),
]