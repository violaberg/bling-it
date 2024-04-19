from django.shortcuts import render, get_object_or_404
from .models import Gemstone

# Create your views here.
def all_gemstones(request):
    """ A view to return all gemstone page """

    gemstones = Gemstone.objects.all()

    context = {
        'gemstones': gemstones,
    }

    return render(request, "gemstones/gemstones.html", context)


def gemstone_detail(request, gemstone_id):
    """ A view to return all individual gemstone page """

    gemstone = get_object_or_404(Gemstone, pk=gemstone_id)

    context = {
        'gemstone': gemstone,
    }

    return render(request, "gemstones/gemstone_detail.html", context)