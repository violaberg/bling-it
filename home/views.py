from django.shortcuts import render

# Create your views here.
def index(request):
    """ A view to return the index page"""

    return render(request, "home/index.html")


def about(request):
    """ A view to return the About Us page"""

    return render(request, "home/about_us.html")


def faq(request):
    """ A view to return the FAQ page"""

    return render(request, "home/faq.html")


def privacy_policy(request):
    """ A view to return the Privacy Policy page"""

    return render(request, "home/privacy_policy.html")