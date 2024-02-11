from django.test import TestCase

from .forms import NewsletterForm

class TestNewsletterForm(TestCase):

    def test_name_required(self):
        form = NewsletterForm({'name':''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')


    def test_email_required(self):
        form = NewsletterForm({'email':'Test field'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_fields_explicit_form_metaclass(self):
        form = NewsletterForm({'email':'Test field'})
        self.assertEqual(form.Meta.fields, ['name', 'email'])


