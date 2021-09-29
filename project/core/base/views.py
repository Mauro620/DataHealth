from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.

def inicio(request):
    data = {
        'title': 'Incio',
    }
    return render(request, 'index.html', data)
