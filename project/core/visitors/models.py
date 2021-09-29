from django.db import models


class visitors(models.Model):
    name = models.CharField(verbose_name='Nombre de visitante', max_length=50)
    lastname = models.CharField(verbose_name='Apellido', max_length=50)
    ID_visitor = models.CharField(verbose_name='Número de documento', max_length=50, unique=True, blank=False, null=False)
    cel_number = models.IntegerField(verbose_name='Número de celular')
    email = models.CharField(verbose_name='Correo Electronico', max_length=50, unique=True)
    relation = models.CharField(verbose_name='Relación con el paciente', max_length=30)
    # ID_patient = models.ForeignKey(verbose_name='documento de paciente', to='patients.models', on_delete=False)
    # name_patient = models.ForeignKey(verbose_name='nombre del paciente', to='patients.models', on_delete=False)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Visitante'
        verbose_name_plural = 'Visitantes'
        db_table = 'Visitante'