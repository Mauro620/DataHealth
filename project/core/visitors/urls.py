from django.urls import path
from core.visitors.views import *

urlpatterns = [
    path('pacientes/list/visitor/', VisitorListView.as_view(), name='Visitantes'),
]