from django.shortcuts import get_object_or_404, render, redirect
from .forms import CamionForm, InformeControlCalidadForm, LugarDestinoForm, BarcoForm
from .models import Barco, Camion, InformeControlCalidad
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def index(request):
    camion_form = CamionForm()
    informe_form = InformeControlCalidadForm()

    if request.method == 'POST':
        camion_form = CamionForm(request.POST)
        informe_form = InformeControlCalidadForm(request.POST)

        if camion_form.is_valid() and informe_form.is_valid():
            camion = camion_form.save()
            informe = informe_form.save()

            # Realizar otras acciones después de guardar los datos si es necesario

            return JsonResponse({'message': 'Datos guardados correctamente'})

    return render(request, 'app/index.html', {'camion_form': camion_form, 'informe_form': informe_form})

def control_calidad(request):
    informes = InformeControlCalidad.objects.all()
    lugar_destino_form = LugarDestinoForm(request.POST or None)
    barco_form = BarcoForm(request.POST or None)

    if request.method == 'POST':
        if lugar_destino_form.is_valid() and barco_form.is_valid():
            lugar_destino = lugar_destino_form.save()
            barco = barco_form.save()
            
            # Puedes realizar otras operaciones o asociar estos datos como desees

            messages.success(request, 'Datos guardados correctamente')
            return redirect('control_calidad')  # Redirige a la página de control de calidad

    return render(
        request,
        'app/control_calidad.html',
        {'informes': informes, 'lugar_destino_form': lugar_destino_form, 'barco_form': barco_form}
    )

def barco(request):
    # Suponiendo que deseas obtener los datos del primer barco en la base de datos
    primer_barco = Barco.objects.first()
    
    context = {
        'barco': primer_barco  # Pasando el primer barco a la plantilla
    }
    
    return render(request, 'app/barco.html', context)

@require_POST
def aprobar_control(request, informe_id):
    informe = get_object_or_404(InformeControlCalidad, pk=informe_id)
    informe.aprobado = True
    informe.save()
    return redirect('control_calidad')


@require_POST
def rechazar_control(request, informe_id):
    informe = get_object_or_404(InformeControlCalidad, pk=informe_id)
    informe.aprobado = False
    informe.save()
    return redirect('control_calidad')
