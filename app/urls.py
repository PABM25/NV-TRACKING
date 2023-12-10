from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('barco/', barco, name='barco'),
    path('control_calidad/', views.control_calidad, name='control_calidad'),
    path('aprobar/<int:informe_id>/', views.aprobar_control, name='aprobar_control'),
    path('rechazar/<int:informe_id>/', views.rechazar_control, name='rechazar_control'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)