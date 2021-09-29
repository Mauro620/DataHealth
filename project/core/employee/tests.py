from django.test import TestCase
from project.wsgi import *
from core.employee.models import *


#listar

query = employee.objects.all()
print(query)

#insersion

e = employee()
e.name = str(input('Inserte el nombre del empleado: \n'))
e.charge = str(input('Inserte el cargo del empleado: \n'))
e.save()

# Create your tests here.
#eliminacion

f = employee.objects.get()
