from django.urls import path
from django.contrib.auth.views import LogoutView
from core.login.views import *

urlpatterns = [
    path('', LoginFormView.as_view(), name='login'),
    #path('logout/', LogoutView.as_view(next_page='login'), name='logout')
    path('logout/', LogoutRedirectView.as_view(), name='logout')
]