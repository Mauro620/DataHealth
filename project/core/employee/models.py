from django.db import models
from datetime import date, datetime

from django.forms import model_to_dict


class employee(models.Model):
    document_type = models.CharField(choices=[
        ('T.I.', 'Tarjeta de identidad'),
        ('C.C', 'Cedula de Ciudadanía'),
        ('C.E', 'Cedula de extrangería')
    ], max_length=30, verbose_name='Tipo de documento', null=False, blank=False, default='Cedula de Ciudadanía')
    id_empleado = models.IntegerField(verbose_name='Documento de identidad', blank=False, primary_key=True, unique=True)
    name = models.CharField(max_length=50, verbose_name='Nombre(s)', null=False)
    lastname = models.CharField(max_length=50, verbose_name='Apellidos', null=False)
    #date_birth = models.DateField( verbose_name='Fecha de nacimiento',null=False, auto_now=False, auto_now_add=False, blank=False)
    departament = models.CharField( choices=[
    ('Leticia','Amazonas' ),
    ('Medellín','Antioquía' ),
    ('Arauca','Arauca' ),
    ('Barranquilla','Atlántico' ),
    ('Cartagena de Indias','Bolívar' ),
    ('Tunja','Boyacá' ),
    ('Manizales','Caldas' ),
    ('Florencia','Caquetá' ),
    ('Yopal','Casanare' ),
    ('Popayán','Cauca' ),
    ('Valledupar','Cesar' ),
    ('Quibdó','Chocó' ),
    ('Montería','Córdoba' ),
    ('Bogotá','Cundinamarca' ),
    ('Inírida','Guainía' ),
    ('San José del Guaviare','Guaviare' ),
    ('Neiva','Huila' ),
    ('Riohacha','La Guajira'),
    ('Santa Marta','Magdalena' ),
    ('Villavicencio','Meta' ),
    ('San Juan de Pasto','Nariño' ),
    ('San José de Cúcuta','Norte de Santander'),
    ('Mocoa','Putumayo' ),
    ('Armenia','Quindío' ),
    ('Pereira','Risaralda' ),
    ('San Andrés','San Andrés y Providencia'),
    ('Bucaramanga','Santander' ),
    ('Sincelejo','Sucre' ),
    ('Ibagué','Tolima' ),
    ('Cali','Valle del Cauca'),
    ('Mitú','Vaupés'),
    ('Puerto Carreño','Vichada'),
    ],max_length=50, verbose_name='Departamento', null=False)
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
        return self.name + " " + self.lastname

    def toJSON(self):
        item = model_to_dict(self)
        return item

    def nombreCompleto(self):
        nameComplete= "{0} {1}"
        return nameComplete.format(self.lastname, self.name)

    class Meta:
        verbose_name = 'Empleado/a'
        verbose_name_plural = 'Empleados'
        db_table = 'Empleados'


