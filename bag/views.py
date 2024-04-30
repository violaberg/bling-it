from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from gemstones.models import Gemstone

# Create your views here.
def view_bag(request):
    """ A view that renders the shopping bag contents page"""

    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):
    """ Add a specified product to the shopping bag """

    gemstone = get_object_or_404(Gemstone, pk=item_id)
    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})
    if item_id in bag:
        # If gemstone already exists in the bag, display error message
        messages.error(request, 'This gemstone is already in your shopping bag.')
        return redirect('gemstone_detail', gemstone_id=item_id)

    bag[item_id] = 1
    messages.success(request, f'Added {gemstone.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        gemstone = get_object_or_404(Gemstone, pk=item_id)
        bag = request.session.get('bag', {})

        if item_id in bag:
            bag.pop(item_id)
            messages.success(request, f'Removed {gemstone.name} from your bag')

        request.session['bag'] = bag

        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)