from django.forms import ModelForm
from core.patients.models import patients


class PatientsForm(ModelForm):
    class Meta:
        model = patients
        fields = '__all__'
