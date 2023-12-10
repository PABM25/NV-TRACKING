from django.contrib import admin
from .models import InformeControlCalidad, Camion, LugarDestino,Barco
# Register your models here.

admin.site.register(InformeControlCalidad)
admin.site.register(Camion)
admin.site.register(LugarDestino)
admin.site.register(Barco)