# Generated by Django 3.2.6 on 2021-10-04 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_alter_employee_id_empleado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='lastname',
            field=models.CharField(editable=False, max_length=50, verbose_name='Apellidos'),
        ),
    ]
