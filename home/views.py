from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import NewsletterSubscriptionForm
from .models import FAQ


def index(request):
    """ A view to return the index page"""

    return render(request, "home/index.html")


def about(request):
    """ A view to return the About Us page"""

    return render(request, "home/about_us.html")


def faq(request):
    """ A view to return the FAQ page"""
    faqs = FAQ.objects.all()

    return render(request, "home/faq.html", {'faqs': faqs})


def privacy_policy(request):
    """ A view to return the Privacy Policy page"""

    return render(request, "home/privacy_policy.html")


def subscribe_to_newsletter(request):
    """ A view for newsletter subscription"""
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Thank you for subscribing to our newsletter!')
            return redirect('home')
        else:
            messages.error(request, 'There was an error with your submission.')
    else:
        form = NewsletterSubscriptionForm()

    return render(request, 'index.html', {'form': form})
    