import django.db.models.deletion
from django.db import models
from datetime import date

# Create your models here.
class rooms(models.Model):
    n_room = models.CharField(max_length=30, verbose_name='Número de sala', primary_key=True, null=False, blank=False)
    capacity = models.IntegerField(verbose_name='Capacidad de sala')
    funtion = models.CharField(verbose_name='Función de la sala', max_length=30)

    def __str__(self):
        return self.n_room

    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'
        db_table = 'Salas'
