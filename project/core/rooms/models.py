import django.db.models.deletion
from django.db import models
from datetime import date

# Create your models here.
class rooms(models.Model):
    n_room = models.IntegerField(verbose_name='Número de sala', primary_key=True, blank=False, auto_created=True)
    capacity = models.IntegerField(verbose_name='Capacidad de sala')
    funtion_room = [
        ('Sala de espera', 'Sala de espera'),
        ('Quirófano', 'Quirófano'),
        ('Quirófano Hibrido', 'Quirófano Hibrido'),
        ('Sala de preparación','Sala de preparación'),
        ('Sala de espera', 'Sala de espera'),
        ('Laboratorio', 'Laboratorio'),
        ('Consultorio', 'Consultorio'),


    ]
    funtion = models.CharField(verbose_name='Función de la sala', max_length=30, choices=funtion_room)

    def __str__(self):
        return self.n_room

    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'
        db_table = 'Salas'
