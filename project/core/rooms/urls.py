from django.urls import path
from core.rooms.views import *

urlpatterns = [
    path('salas/',RoomsListView.as_view(), name='salas'),
    path('salas/register/', RoomsCreateView.as_view(), name='Salas_Create'),
    path('salas/edit/<int:pk>/', RoomsUpdateView.as_view(), name='Salas_Update'),
    path('salas/delete/<int:pk>/', RoomsDeleteView.as_view(), name='Salas_Delete')
]
