from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from core.rooms.form import RoomsForm
from core.rooms.models import *
# Create your views here.

class RoomsListView(ListView):
    model = rooms
    template_name = 'rooms.html'

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'Salas'
        return contex
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class RoomsCreateView(CreateView):
    model = rooms
    template_name = 'RoomCreate.html'
    form_class = RoomsForm
    success_url = reverse_lazy('salas')

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'Nueva Sala'
        contex['list_url'] = reverse_lazy('salas')
        return contex
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class RoomsUpdateView(UpdateView):
    model = rooms
    form_class = RoomsForm
    template_name = 'RoomCreate.html'
    success_url = reverse_lazy('salas')

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'Editar Sala'
        contex['action'] = 'edit'
        contex['list_url'] = reverse_lazy('salas')
        contex['entity'] = 'Salas'
        return contex
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class RoomsDeleteView(DeleteView):
    model = rooms
    template_name = 'RoomCreate.html'
    success_url = reverse_lazy('salas')

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'Eliminar Sala'
        contex['list_url'] = reverse_lazy('salas')
        contex['entity'] = 'salas'
        return contex
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)