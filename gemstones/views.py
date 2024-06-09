from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Gemstone, Category
from profiles.views import add_to_wishlist
from profiles.models import Wishlist
from .forms import GemstoneForm


def all_gemstones(request):
    """ A view to return all gemstone page """
    gemstones = Gemstone.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    new_arrivals = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                gemstones = gemstones.annotate(lower_name=Lower('name'))
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

        if 'new_arrivals' in request.GET:
            new_arrivals = True
            one_month_ago = timezone.now() - timedelta(days=30)
            gemstones = gemstones.filter(created_at__gte=one_month_ago)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(
                    reverse('gemstones'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            gemstones = gemstones.filter(queries)

    current_sorting = f'{sort}_{direction}'

    # Pagination
    paginator = Paginator(gemstones, 6)
    page_number = request.GET.get('page')
    try:
        gemstones = paginator.page(page_number)
    except PageNotAnInteger:
        gemstones = paginator.page(1)
    except EmptyPage:
        gemstones = paginator.page(paginator.num_pages)

    context = {
        'gemstones': gemstones,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'new_arrivals': new_arrivals,
    }

    return render(request, "gemstones/gemstones.html", context)


def gemstone_detail(request, gemstone_id):
    """ A view to return all individual gemstone page """
    gemstone = get_object_or_404(Gemstone, pk=gemstone_id)
    wishlist = False
    if request.user.is_authenticated:
        profile = request.user.userprofile
        if Wishlist.objects.filter(
            user=profile.user, gemstones=gemstone).exists():
            wishlist = True

    context = {
        'gemstone': gemstone,
        'wishlist': wishlist,
    }

    return render(request, "gemstones/gemstone_detail.html", context)


@login_required
def add_gemstone(request):
    """ Add a gemstone to the store """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store owners have permission to do that.'
            )
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = GemstoneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gemstone added successfully!')
            return redirect(reverse('add_gemstone'))
        else:
            messages.error(
                request, 'Failed to add gemstone. Please ensure the form is valid.'
                )
    else:
        form = GemstoneForm()

    template = 'gemstones/add_gemstone.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_gemstone(request, gemstone_id):
    """ Edit a gemstone in the store """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store owners have permission to do that.'
            )
        return redirect(reverse('home'))

    gemstone = get_object_or_404(Gemstone, pk=gemstone_id)
    if request.method == 'POST':
        form = GemstoneForm(request.POST, request.FILES, instance=gemstone)
        if form.is_valid():
            gemstone = form.save()
            messages.success(request, 'Gemstone updated successfully!')
            return redirect(reverse('gemstone_detail', args=[gemstone.id]))
        else:
            messages.error(
                request, 'Failed to update gemstone. Please ensure the form is valid.'
                )
    else:
        form = GemstoneForm(instance=gemstone)
        messages.info(request, f'You are editing {gemstone.name}')

    template = 'gemstones/edit_gemstone.html'
    context = {
        'form': form,
        'gemstone': gemstone,
    }

    return render(request, template, context)


@login_required
def delete_gemstone(request, gemstone_id):
    """ Delete a gemstone from the store """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store owners have permission to do that.')
        return redirect(reverse('home'))

    gemstone = get_object_or_404(Gemstone, pk=gemstone_id)
    gemstone.delete()
    messages.success(request, 'Gemstone deleted!')
    return redirect(reverse('gemstones'))
