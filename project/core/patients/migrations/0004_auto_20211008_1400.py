# Generated by Django 3.2.6 on 2021-10-08 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_alter_patients_rh'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='document_type',
            field=models.CharField(choices=[('T.I.', 'Tarjeta de identidad'), ('C.C', 'Cedula de Ciudadanía'), ('C.E', 'Cedula de extrangería')], default='Cedula de Ciudadanía', max_length=30, verbose_name='Tipo de documento'),
        ),
        migrations.AlterField(
            model_name='patients',
            name='id_patient',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='documento de identidad'),
        ),
    ]
