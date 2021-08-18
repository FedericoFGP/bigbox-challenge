from django.test import TestCase
from .models import Box
# Create your tests here.

class BoxModelTests(TestCase):
    def test_contador_de_objetos(self):
        self.assertEqual(Box.objects.all.count(), 2)
