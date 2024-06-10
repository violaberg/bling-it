from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from gemstones.models import Gemstone


def view_bag(request):
    """
    Render the shopping bag contents page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered shopping bag page.
    """
    return render(request, "bag/bag.html")


def add_to_bag(request, item_id):
    """
    Add a specified gemstone to the shopping bag.

    Args:
        request (HttpRequest): The HTTP request object.
        item_id (int): The ID of the gemstone to be added to the bag.

    Returns:
        HttpResponse: A redirect to the specified URL or gemstone detail page.
    """

    gemstone = get_object_or_404(Gemstone, pk=item_id)
    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})
    if item_id in bag:
        # If gemstone already exists in the bag, display error message
        messages.error(
            request, 'This gemstone is already in your shopping bag.'
            )
        return redirect('gemstone_detail', gemstone_id=item_id)

    bag[item_id] = 1
    messages.success(request, f'Added {gemstone.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """
    Remove the specified gemstone from the shopping bag.

    Args:
        request (HttpRequest): The HTTP request object.
        item_id (int): The ID of the gemstone to be removed from the bag.

    Returns:
        HttpResponse: A status response indicating success or failure.
    """

    try:
        gemstone = get_object_or_404(Gemstone, pk=item_id)
        bag = request.session.get('bag', {})

        if item_id in bag:
            bag.pop(item_id)
            messages.success(request, f'Removed {gemstone.name} from your bag')

        request.session['bag'] = bag

        return HttpResponse(status=200)

    except Exception as e:

        messages.error(request, f'Error removing item: {e}')

        return HttpResponse(status=500)
