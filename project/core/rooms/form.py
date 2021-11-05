from django.forms import *
from core.rooms.models import rooms


# Clase de formulario de empleado para poder llamar a mis modelos por la variable {{ form }}
class RoomsForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = rooms
        fields = '__all__'