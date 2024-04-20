from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Gemstone

# Create your views here.
def all_gemstones(request):
    """ A view to return all gemstone page """

    gemstones = Gemstone.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('gemstones'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            gemstones = gemstones.filter(queries)

    context = {
        'gemstones': gemstones,
        'search_term': query,
    }

    return render(request, "gemstones/gemstones.html", context)


def gemstone_detail(request, gemstone_id):
    """ A view to return all individual gemstone page """

    gemstone = get_object_or_404(Gemstone, pk=gemstone_id)

    context = {
        'gemstone': gemstone,
    }

    return render(request, "gemstones/gemstone_detail.html", context)