from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from gemstones.models import Gemstone

# Create your views here.
def view_bag(request):
    """ A view that renders the shopping bag contents page"""

    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):
    """ Add a specified product to the shopping bag """

    gemstone = Gemstone.objects.get(pk=item_id)
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    bag[item_id] = quantity
    messages.success(request, f'Added {gemstone.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        bag = request.session.get('bag', {})

        if item_id in bag:
            bag.pop(item_id)

        request.session['bag'] = bag

        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)