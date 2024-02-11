from django.test import TestCase
from .models import Newsletter


class TestHomeappViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homeapp/index.html',)
    
    def test_get_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homeapp/about-company.html',)

    def test_get_contact_page(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homeapp/contact.html',)

    def test_get_shipping_page(self):
        response = self.client.get('/shipping/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homeapp/shipping.html',)

    def test_newsletters_form(self):        
        response = self.client.post('/newsletter',{'name': 'Test name','email': 'Test email'})
        self.assertRedirects(response, '/')
                   

