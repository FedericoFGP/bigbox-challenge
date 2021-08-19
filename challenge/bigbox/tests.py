from django.test import TestCase
from .models import Box,Activity
from django.urls import reverse

class BoxModelTests(TestCase):
    def test_contador_de_objetos(self):
        self.assertIsNot(Box.objects.all(), None)

class BoxIndexViewTest(TestCase):
    def test_(self):
        response = self.client.get(reverse('bigbox:index'))
        self.assertEqual(response.status_code, 200)

class BoxDetailViewTest(TestCase):
    def test_(self):
        response = self.client.get(reverse('bigbox:box-list'))
        self.assertEqual(response.status_code, 200)

class BoxActivitiesViewTest(TestCase):
    def test_(self):
    # Creando un objeto con ID 1281 para testear ya que la base temporal de test esta vacia.
        box = Box(pk=1281, price=12000)
        box.save()
    # Paso el mismo PK que se uso antes 
        response = self.client.get(reverse('bigbox:box-activities', args=[1281]))
        self.assertEqual(response.status_code, 200)

        response2 = self.client.get(reverse('bigbox:box-activities', args=[9981]))
        self.assertNotEqual(response2.status_code, 200)


