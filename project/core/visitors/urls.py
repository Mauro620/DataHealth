from django.urls import path
from core.visitors.views import *

urlpatterns = [
    path('visitante/', VisitorListView.as_view(), name='Visitantes'),
]