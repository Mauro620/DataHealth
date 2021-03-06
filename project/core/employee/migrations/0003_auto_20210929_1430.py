# Generated by Django 3.2.6 on 2021-09-29 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_remove_employee_schedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AddField(
            model_name='employee',
            name='id_empleado',
            field=models.CharField(default=0, editable=False, max_length=15, primary_key=True, serialize=False, unique=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='rh',
            field=models.CharField(choices=[('A positivo', 'A+'), ('A negativo', 'A-'), ('O positivo', 'O+'), ('O negativo', 'O-'), ('AB positivo', 'AB+'), ('AB negativo', 'AB-'), ('B positivo', 'B+'), ('B negativo', 'B-')], default='A+', max_length=30, verbose_name='Tipo de sangre'),
        ),
    ]
