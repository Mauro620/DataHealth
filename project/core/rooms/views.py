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
        context = super().get_context_data(**kwargs)
        context['title'] = 'Salas'
        return context
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class RoomsCreateView(CreateView):
    model = rooms
    template_name = 'RoomCreate.html'
    form_class = RoomsForm
    success_url = reverse_lazy('salas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nueva Sala'
        context['list_url'] = reverse_lazy('salas')
        return context
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class RoomsUpdateView(UpdateView):
    model = rooms
    form_class = RoomsForm
    template_name = 'RoomCreate.html'
    success_url = reverse_lazy('salas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Sala'
        context['action'] = 'edit'
        context['list_url'] = reverse_lazy('salas')
        context['entity'] = 'Salas'
        return context
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class RoomsDeleteView(DeleteView):
    model = rooms
    template_name = 'EliminarSala.html'
    success_url = reverse_lazy('salas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Sala'
        context['list_url'] = reverse_lazy('salas')
        context['entity'] = 'salas'
        context['action'] = 'delete'
        return context
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)