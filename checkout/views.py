from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "You bag is empty!")
        return redirect(reverse('posters'))


    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OIzlALQubLimFj0XbqJIUUD8Am6V2rXpRgu9It8E0t2xB1KHWpbtnsZop8uS6hSA0piAB819tAE3DAsDMFWLuUE008j15E3si',
        'client_secret': 'test client secret ',
    }

    return render(request, template, context)    