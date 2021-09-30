import django.db.models.deletion
from django.db import models
from datetime import date


class employee(models.Model):
    id_empleado = models.IntegerField(verbose_name='ID', blank=False, primary_key=True, unique=True)
    name = models.CharField(max_length=50, verbose_name='Nombres', null=False)
    lastname = models.CharField(max_length=50, verbose_name='Apellidos', null=False)
    departament = models.CharField(max_length=50, verbose_name='Departamento', null=False)
    city = models.CharField(max_length=30, verbose_name='Ciudad', null=True, blank=True)
    direction = models.CharField(max_length=30, verbose_name='Dirección', null=True, blank=True)
    blood_type = [
        ('A positivo', 'A+'),
        ('A negativo', 'A-'),
        ('O positivo', 'O+'),
        ('O negativo', 'O-' ),
        ('AB positivo', 'AB+'),
        ('AB negativo','AB-'),
        ('B positivo','B+'),
        ('B negativo', 'B-')
    ]
    rh = models.CharField(choices=blood_type, verbose_name='Tipo de sangre', max_length=30, default='A+')
    email = models.CharField(verbose_name='Correo electronico', max_length=50)
    genders = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    gender = models.CharField(choices=genders, default='F',max_length=1)
    charges = [
        ('Secretari@', 'Secretari@'),
        ('Enfermer@', 'Enfermer@'),
        ('Doctor', 'Doctor'),
        ('Cirujano', 'Cirujano'),
        ('Recepcionista', 'Recepcionista'),
        ('Vigilante', 'Vigilante'),
        ('Aseo', 'Aseo')
    ]
    charge = models.CharField(verbose_name='Cargo', choices=charges, default='Recepcionista',  max_length=30)
    #schedule = models.DateTimeField()

    def __str__(self):
        return self.name

    def nombreCompleto(self):
        nameComplete= "{0} {1}"
        return nameComplete.format(self.lastname, self.name)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'Empleados'

