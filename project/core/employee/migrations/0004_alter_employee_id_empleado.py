# Generated by Django 3.2.6 on 2021-09-29 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20210929_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id_empleado',
            field=models.IntegerField(default=0, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID'),
        ),
    ]