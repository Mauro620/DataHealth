from django.urls import path
from core.patients.views import *

urlpatterns = [
    path('pacientes/list/', PacientesListView.as_view(), name='Patients'),
    path('pacientes/create/', PacientesCreateView.as_view(), name='Patients_Create'),

]
