# Generated by Django 4.2.7 on 2023-11-19 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_informecontrolcalidad_tipo_almacenamiento'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_barco', models.CharField(max_length=6)),
                ('nombre_completo_capitan', models.CharField(max_length=50)),
                ('rut_capitan', models.CharField(default='0', max_length=10)),
                ('cantidad_tripulacion', models.IntegerField()),
                ('peso_carga', models.CharField(default='0', max_length=3)),
                ('hora_salida', models.DateTimeField()),
                ('hora_regreso', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='LugarDestino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar', models.CharField(choices=[('1', 'Criadero 1'), ('2', 'Criadero 2'), ('3', 'Criadero 3'), ('4', 'Criadero 4'), ('5', 'Criadero 5')], default='1', max_length=100)),
                ('fecha_despacho', models.DateTimeField()),
            ],
        ),
    ]
