from django.test import TestCase
from .models import Newsletter

# Create your tests here.
class TestFormModels(TestCase):

    def test_insert_data(self):
        item = Newsletter.objects.create(name='Test insert')
        self.assertTrue(item.name)

    def test_item_string_method_returns_name(self):
        item = Newsletter.objects.create(name='Test insert')
        self.assertEqual(str(item), 'Test insert')    
