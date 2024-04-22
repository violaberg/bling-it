from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Gemstone, Category

# Create your views here.
def all_gemstones(request):
    """ A view to return all gemstone page """

    gemstones = Gemstone.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                gemstones = gemstones.annotate(lower_name=lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            gemstones = gemstones.order_by(sortkey)


        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            gemstones = gemstones.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('gemstones'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            gemstones = gemstones.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'gemstones': gemstones,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, "gemstones/gemstones.html", context)


def gemstone_detail(request, gemstone_id):
    """ A view to return all individual gemstone page """

    gemstone = get_object_or_404(Gemstone, pk=gemstone_id)

    context = {
        'gemstone': gemstone,
    }

    return render(request, "gemstones/gemstone_detail.html", context)