from django.shortcuts import get_object_or_404, render, redirect
from .forms import CamionForm, InformeControlCalidadForm, LugarDestinoForm, BarcoForm
from .models import Barco, Camion, InformeControlCalidad
from django.contrib import messages
from django.http import JsonResponse

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

def aprobar_control(request, informe_id):
    informe = InformeControlCalidad.objects.get(pk=informe_id)
    # Aquí manejas la lógica para aprobar o rechazar el informe
    informe.aprobado = True  # Por ejemplo, marcamos el informe como aprobado
    informe.save()
    return redirect('control_calidad')  # Redirige de vuelta a la página de control de calidad

def rechazar_control(request, informe_id):
    informe = get_object_or_404(informe, pk=informe_id)
    
    # Aquí podrías realizar la lógica para marcar el informe como rechazado
    informe.aprobado = False
    informe.save()

    # Redirige a una página o a la vista de control de calidad
    return redirect('control_calidad')  # Reemplaza 'control_calidad' con el nombre de tu vista actual