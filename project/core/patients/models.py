import django.db.models.deletion
from django.db import models
from datetime import date

class patients(models.Model):
    document_type = models.CharField(choices=[
        ('T.I.', 'Tarjeta de identidad'),
        ('C.C', 'Cedula de Ciudadanía'),
        ('C.E', 'Cedula de extrangería')
    ], max_length=30, verbose_name='Tipo de documento', null=False, blank=False, default='Cedula de Ciudadanía')
    id_patient = models.IntegerField(verbose_name='documento de identidad', unique=True, primary_key=True, null=False)
    name = models.CharField(max_length=50, verbose_name='Nombres', null=False)
    lastname = models.CharField(max_length=50, verbose_name='Apellidos', null=False)
    #bday = models.DateField(auto_now=False, auto_now_add=False, null=True)
    departament = models.CharField(choices=[
        ('Leticia', 'Amazonas'),
        ('Medellín', 'Antioquía'),
        ('Arauca', 'Arauca'),
        ('Barranquilla', 'Atlántico'),
        ('Cartagena de Indias', 'Bolívar'),
        ('Tunja', 'Boyacá'),
        ('Manizales', 'Caldas'),
        ('Florencia', 'Caquetá'),
        ('Yopal', 'Casanare'),
        ('Popayán', 'Cauca'),
        ('Valledupar', 'Cesar'),
        ('Quibdó', 'Chocó'),
        ('Montería', 'Córdoba'),
        ('Bogotá', 'Cundinamarca'),
        ('Inírida', 'Guainía'),
        ('San José del Guaviare', 'Guaviare'),
        ('Neiva', 'Huila'),
        ('Riohacha', 'La Guajira'),
        ('Santa Marta', 'Magdalena'),
        ('Villavicencio', 'Meta'),
        ('San Juan de Pasto', 'Nariño'),
        ('San José de Cúcuta', 'Norte de Santander'),
        ('Mocoa', 'Putumayo'),
        ('Armenia', 'Quindío'),
        ('Pereira', 'Risaralda'),
        ('San Andrés', 'San Andrés y Providencia'),
        ('Bucaramanga', 'Santander'),
        ('Sincelejo', 'Sucre'),
        ('Ibagué', 'Tolima'),
        ('Cali', 'Valle del Cauca'),
        ('Mitú', 'Vaupés'),
        ('Puerto Carreño', 'Vichada'),
    ], max_length=50, verbose_name='Departamento', null=False)
    city = models.CharField(max_length=30, verbose_name='Ciudad')
    direccion = models.CharField(max_length=30, verbose_name='Dirección', null=True, blank=True)
    rh = models.CharField(choices=[
        ('A positivo', 'A+'),
        ('A negativo', 'A-'),
        ('O positivo', 'O+'),
        ('O negativo', 'O-' ),
        ('AB positivo', 'AB+'),
        ('AB negativo','AB-'),
        ( 'B positivo','B+'),
        ('B negativo', 'B-')
    ], verbose_name='Tipo de sangre', max_length=15, default='A+')
    email = models.CharField(verbose_name='Correo electronico', max_length=50, null=True, blank=True)
    gender = models.CharField(choices=[
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ], max_length=1, default='F')
    state = models.CharField(choices=[
        ('Interno', 'Interno'),
        ('Alta', 'Alta'),
        ('Recuperación', 'Recuperación'),
        ('Sano', 'Sano'),
        ('requiere cirugia', 'requiere cirugia' )
    ], max_length=30, default='Sano')
    notas= models.CharField(max_length=1000, null= True, blank=True, unique=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        db_table = 'Pacientes'