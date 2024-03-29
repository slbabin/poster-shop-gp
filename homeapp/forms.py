from django import forms
from .models import Newsletter, Contact


class NewsletterForm(forms.ModelForm):

    """ A form to render the fields to use in the newsletter form """

    class Meta:
        model = Newsletter
        fields = ['name', 'email']

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'name': 'Name',
            'email': 'E-mail address',
        }

        for field in self.fields:

            placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False

        self.fields['name'].widget.attrs['autofocus'] = True

        if user and user.is_authenticated:
            self.fields['name'].initial = user.get_full_name()
            self.fields['email'].initial = user.email


class ContactForm(forms.ModelForm):

    """ A form to render the fields to use in the contact form. """

    class Meta:
        model = Contact
        fields = ['name', 'email', 'body']

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'name': 'Your Name',
            'email': 'Your email address',
            'body': 'Write your message here',
        }

        for field in self.fields:

            placeholder = f'{placeholders[field]} *'
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False

        self.fields['name'].widget.attrs['autofocus'] = True

        if user and user.is_authenticated:
            self.fields['name'].initial = user.get_full_name()
            self.fields['email'].initial = user.email
