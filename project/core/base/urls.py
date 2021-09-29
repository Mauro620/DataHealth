from django.template.context_processors import static
from django.urls import path
from core.base.views import *
from project import settings

urlpatterns = [
    path('', inicio, name='base'),
]
