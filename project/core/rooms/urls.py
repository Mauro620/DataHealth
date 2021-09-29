from django.urls import path
from core.rooms.views import *

urlpatterns = [
    path('salas/',RoomsListView.as_view() , name='salas'),
]
