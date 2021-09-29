from django.shortcuts import render
from django.views.generic import ListView
from core.visitors.models import *

# Create your views here.
class VisitorListView(ListView):
    model = 'visitor'
    template_name = 'visitante.html'