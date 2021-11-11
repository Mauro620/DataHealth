from django.template.context_processors import static
from django.urls import path
from core.base.views import *
from project import settings


urlpatterns = [
    path('', InicioTemplateView.as_view(), name='base'),
    path('contacto/', contactoTemplateView.as_view(), name='contacto'),

]
