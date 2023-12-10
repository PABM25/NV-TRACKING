from django.db import models

# Create your models here.
class InformeControlCalidad(models.Model):
    TIPO_ALIMENTO_CHOICES = [
        ('1', 'Detrito'),
        ('2', 'Bacterias'),
        ('3', 'Plancton'),
        ('4', 'Gusanos'),
        ('5', 'Insectos'),
    ]
    TIPO_ALMACENAMIETO_CHOICES = [
        ('1', 'Congelados'),
        ('2', 'Temperatura ambiente'),
        ('3', 'Helado'),
    ]
    tipo_alimento = models.CharField(max_length=50, choices=TIPO_ALIMENTO_CHOICES, default='1')
    tipo_almacenamiento = models.CharField(max_length=50, choices=TIPO_ALMACENAMIETO_CHOICES, default='1')
    temperatura_almacenamiento = models.CharField(max_length=10)


class Camion(models.Model):
    patente = models.CharField(max_length=6)
    nombre_completo_chofer = models.CharField(max_length=50)
    rut_chofer = models.CharField(max_length=10, default='0')
    tipo_carga = models.CharField(max_length=100)
    peso_carga = models.CharField(max_length=3, default='0')
    hora_ingreso = models.DateTimeField()
    hora_salida = models.DateTimeField()
    
    
class LugarDestino(models.Model):
    
    DESTINO_CHOICES = [
        ('1', 'Criadero 1'),
        ('2', 'Criadero 2'),
        ('3', 'Criadero 3'),
        ('4', 'Criadero 4'),
        ('5', 'Criadero 5'),
    ]
    lugar = models.CharField(max_length=100, choices=DESTINO_CHOICES, default='1')
    fecha_despacho = models.DateTimeField()
    
class Barco(models.Model):
    
    numero_barco = models.CharField(max_length=6)
    nombre_completo_capitan = models.CharField(max_length=50)
    rut_capitan = models.CharField(max_length=10, default='0')
    cantidad_tripulacion = models.IntegerField()
    peso_carga = models.CharField(max_length=3, default='0')
    hora_salida = models.DateTimeField()
    hora_regreso = models.DateTimeField()