from django.forms import *
from core.employee.models import employee


# Clase de formulario de empleado para poder llamar a mis modelos por la variable {{ form }}
class EmployeeForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = employee
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Ingrese un nombre'
                }
            ),
            'id_empleado': NumberInput(
                attrs={
                    'placeholder': 'ingrese la cedula del empleado'
                }
            ),
            'lastname': TextInput(
                attrs={
                    'placeholder': 'ingrese el apellido del empleado',
                }
            ),

        }
