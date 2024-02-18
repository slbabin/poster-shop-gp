from django.shortcuts import render, redirect
from .forms import NewsletterForm, ContactForm
from django.contrib import messages


def index(request):
    """ A view to return the index page """
    
    return render(request, 'homeapp/index.html')


def terms(request):
    """ A view to return terms page """
    
    return render(request, 'homeapp/terms.html')


def about(request):
    """ A view to return about page  """
    
    return render(request, 'homeapp/about-company.html')


def privacypolicy (request):
    """ A view to return privacy policy page  """
    
    return render(request, 'homeapp/privacy.html')


def contact (request):
    """ A view to return contact page  """
    
    return render(request, 'homeapp/contact.html')    

def shipping (request):
    """ A view to return contact page  """
    
    return render(request, 'homeapp/shipping.html') 


def faq (request):
    """ A view to return contact page  """
    
    return render(request, 'homeapp/faq.html') 

def newsletters(request):
    """ A view to subscribe to site newsletters """

    form = NewsletterForm(request.POST or None, user=request.user)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Thanks for subscribing to our newsletter!'
                )
            return redirect('home')
        messages.error(request, 'An error has occurred. Please try again.')
    template = 'homeapp/newsletters.html'
    context = {
        'form': form,
    }
    return render(request, template, context)



def contact(request):
    """ A view to contact the site admin"""
    form = ContactForm(request.POST or None, user=request.user)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Thanks for contacting us! We will reply you as soon as we can.'
                )
            return redirect('home')
        messages.error(request, 'An error has occurred. Please try again.')
    template = 'homeapp/contact.html'
    context = {
        'form': form,
    }
    return render(request, template, context)    