from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Gemstone, Category
from profiles.views import add_to_wishlist
from profiles.forms import WishlistForm
from .forms import GemstoneForm

# Create your views here.
def all_gemstones(request):
    """ A view to return all gemstone page """
    if request.method == 'POST':
        # Process the form submission
        form = WishlistForm(request.POST)
        if form.is_valid():
            gemstone_id = form.cleaned_data['gemstone_id']

            return redirect('gemstones')

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
        'form': WishlistForm(),
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, "gemstones/gemstones.html", context)


def gemstone_detail(request, gemstone_id):
    """ A view to return all individual gemstone page """
    gemstone = get_object_or_404(Gemstone, pk=gemstone_id)
    wishlist = False

    if request.method == 'POST':
        # Process the form submission
        if request.user.is_authenticated:
            profile = request.user.userprofile
            form = WishlistForm(request.POST)
            if form.is_valid():
                gemstone_id = form.cleaned_data['gemstone_id']
                if not Wishlist.objects.filter(user=profile, gemstone=gemstone).exists():
                    wishlist = True
                    # Add gemstone to the wishlist
                    wishlist, created = Wishlist.objects.get_or_create(user=profile)
                    wishlist.gemstone.add(gemstone)

                    # Add a success message
                    messages.success(request, f'{gemstone.name} added to your wishlist')
                    # Redirect to the same page
                    return redirect('gemstone_detail', gemstone_id=gemstone_id)
            else:
                # Optionally, you can add an error message here
                messages.error(request, 'Invalid form submission')

    else:
        # Initialize the form for rendering
        form = WishlistForm(initial={'gemstone_id': gemstone_id})

    context = {
        'gemstone': gemstone,
        'form': form,
        'wishlist': wishlist,
    }

    return render(request, "gemstones/gemstone_detail.html", context)


def add_gemstone(request):
    """ Add a gemstone to the store """
    if request.method == 'POST':
        form = GemstoneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gemstone added successfully!')
            return redirect(reverse('add_gemstone'))
        else:
            messages.error(request, 'Failed to add gemstone. Please ensure the form is valid.')
    else:
        form = GemstoneForm()

    template = 'gemstones/add_gemstone.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_gemstone(request, gemstone_id):
    """ Edit a gemstone in the store """
    gemstone = get_object_or_404(Gemstone, pk=gemstone_id)
    if request.method == 'POST':
        form = GemstoneForm(request.POST, request.FILES, instance=gemstone)
        if form.is_valid():
            gemstone = form.save()
            messages.success(request, 'Gemstone updated successfully!')
            return redirect(reverse('gemstone_detail', args=[gemstone.id]))
        else:
            messages.error(request, 'Failed to update gemstone. Please ensure the form is valid.')
    else:
        form = GemstoneForm(instance=gemstone)
        messages.info(request, f'You are editing {gemstone.name}')

    template = 'gemstones/edit_gemstone.html'
    context = {
        'form': form,
        'gemstone': gemstone,
    }

    return render(request, template, context)


def delete_gemstone(request, gemstone_id):
    """ Delete a gemstone from the store """
    gemstone = get_object_or_404(Gemstone, pk=gemstone_id)
    gemstone.delete()
    messages.success(request, 'Gemstone deleted!')
    return redirect(reverse('gemstones'))