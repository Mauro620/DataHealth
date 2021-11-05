from django.urls import path
from core.patients.views import *
urlpatterns = [
    path('pacientes/list/', PacientesListView.as_view(), name='Patients'),
    path('pacientes/create/', PacientesCreateView.as_view(), name='Patients_Create'),
    path('pacientes/edit/<int:pk>/', PacientesUpdateView.as_view(), name='Pacientes_Update'),
    path('pacientes/delete/<int:pk>/', PacientesDeleteView.as_view(), name='Pacientes_Delete'),

]

