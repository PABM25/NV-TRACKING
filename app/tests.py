from django.test import TestCase
from django.urls import reverse

from .models import InformeControlCalidad


class ControlCalidadTests(TestCase):
    def setUp(self):
        self.informe = InformeControlCalidad.objects.create(temperatura_almacenamiento='4')

    def test_informe_nuevo_queda_pendiente(self):
        self.assertIsNone(self.informe.aprobado)

    def test_aprobar_guarda_el_estado(self):
        respuesta = self.client.post(reverse('aprobar_control', args=[self.informe.id]))
        self.assertRedirects(respuesta, reverse('control_calidad'))
        self.informe.refresh_from_db()
        self.assertTrue(self.informe.aprobado)

    def test_rechazar_guarda_el_estado(self):
        respuesta = self.client.post(reverse('rechazar_control', args=[self.informe.id]))
        self.assertRedirects(respuesta, reverse('control_calidad'))
        self.informe.refresh_from_db()
        self.assertFalse(self.informe.aprobado)

    def test_informe_inexistente_da_404(self):
        respuesta = self.client.post(reverse('rechazar_control', args=[9999]))
        self.assertEqual(respuesta.status_code, 404)

    def test_get_no_cambia_el_estado(self):
        respuesta = self.client.get(reverse('aprobar_control', args=[self.informe.id]))
        self.assertEqual(respuesta.status_code, 405)
        self.informe.refresh_from_db()
        self.assertIsNone(self.informe.aprobado)

    def test_control_calidad_muestra_estados(self):
        InformeControlCalidad.objects.create(temperatura_almacenamiento='5', aprobado=False)
        respuesta = self.client.get(reverse('control_calidad'))
        self.assertContains(respuesta, 'Rechazado')
