from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, 'Your bag is empty at the moment!')
        return redirect(reverse('gemstones'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51P4hPhP3ln5OI6anroWXx3lX10EhjvljhvYMRpvejAFs5pZjUoCk1bxuIkPeLVpZQR4xF2iZHhL099u1ESFVQ87R00zPgrNm74',
        'client_secret': 'test client secret',
    }

    return render (request, template, context)