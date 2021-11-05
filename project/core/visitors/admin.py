from django.contrib import admin

# Register your models here.
from core.visitors.models import visitors

admin.site.register(visitors)