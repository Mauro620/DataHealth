# Generated by Django 3.2.6 on 2021-10-08 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_auto_20211008_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='document_type',
            field=models.CharField(choices=[('T.I.', 'Tarjeta de identidad'), ('C.C', 'Cedula de Ciudadanía'), ('C.E', 'Cedula de extrangería')], default='Cedula de Ciudadanía', max_length=30, verbose_name='Tipo de documento'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='departament',
            field=models.CharField(choices=[('Leticia', 'Amazonas'), ('Medellín', 'Antioquía'), ('Arauca', 'Arauca'), ('Barranquilla', 'Atlántico'), ('Cartagena de Indias', 'Bolívar'), ('Tunja', 'Boyacá'), ('Manizales', 'Caldas'), ('Florencia', 'Caquetá'), ('Yopal', 'Casanare'), ('Popayán', 'Cauca'), ('Valledupar', 'Cesar'), ('Quibdó', 'Chocó'), ('Montería', 'Córdoba'), ('Bogotá', 'Cundinamarca'), ('Inírida', 'Guainía'), ('San José del Guaviare', 'Guaviare'), ('Neiva', 'Huila'), ('Riohacha', 'La Guajira'), ('Santa Marta', 'Magdalena'), ('Villavicencio', 'Meta'), ('San Juan de Pasto', 'Nariño'), ('San José de Cúcuta', 'Norte de Santander'), ('Mocoa', 'Putumayo'), ('Armenia', 'Quindío'), ('Pereira', 'Risaralda'), ('San Andrés', 'San Andrés y Providencia'), ('Bucaramanga', 'Santander'), ('Sincelejo', 'Sucre'), ('Ibagué', 'Tolima'), ('Cali', 'Valle del Cauca'), ('Mitú', 'Vaupés'), ('Puerto Carreño', 'Vichada')], max_length=50, verbose_name='Departamento'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='id_empleado',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Documento de identidad'),
        ),
    ]
