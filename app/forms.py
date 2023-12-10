from django import forms
from .models import InformeControlCalidad, Camion, LugarDestino, Barco

class InformeControlCalidadForm(forms.ModelForm):
    class Meta:
        model = InformeControlCalidad
        fields = '__all__'
        widgets = {
            'fecha_ingreso': forms.DateInput(attrs={'type': 'date'})
            # Puedes personalizar más widgets aquí para otros campos de fecha si lo necesitas
        }

class CamionForm(forms.ModelForm):
    class Meta:
        model = Camion
        fields = '__all__'
        widgets = {
            'hora_ingreso': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'hora_salida': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            # Puedes personalizar más widgets aquí para otros campos de fecha si lo necesitas
        }

class LugarDestinoForm(forms.ModelForm):
    class Meta:
        model = LugarDestino
        fields = ['lugar', 'fecha_despacho']
        widgets = {
            'fecha_despacho': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class BarcoForm(forms.ModelForm):
    class Meta:
        model = Barco
        fields = ['numero_barco', 'nombre_completo_capitan', 'rut_capitan', 'cantidad_tripulacion', 'peso_carga', 'hora_salida', 'hora_regreso']
        widgets = {
        'hora_salida': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        'hora_regreso': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }