from django.shortcuts import render
from .models import Gemstone

# Create your views here.
def all_gemstones(request):
    """ A view to return all gemstone page """

    gemstones = Gemstone.objects.all()

    context = {
        'gemstones': gemstones,
    }

    return render(request, "gemstones/gemstones.html", context)