# Generated by Django 4.2.7 on 2023-11-19 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_informecontrolcalidad_tipo_alimento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camion',
            name='fecha_ingreso',
        ),
    ]
