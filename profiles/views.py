from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string

from .models import UserProfile, Gemstone, Wishlist
from .forms import UserProfileForm
from checkout.models import Order
from gemstones.models import Gemstone


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

     # Retrieve the wishlist for the current user
    wishlist_items = []
    try:
        wishlist = Wishlist.objects.get(user=request.user)
        wishlist_items = wishlist.gemstones.all()
    except Wishlist.DoesNotExist:
        pass

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'wishlist_items': wishlist_items,
        'on_profile_page': True,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def wishlist(request, pk):
    """ A view to return the wishlist page"""
    profile = get_object_or_404(UserProfile, id=pk)
    wishlist_items = Wishlist.objects.filter(user=profile).order_by('-created')
    wishlist_items = gemstones_pagination(request, wishlist_items, 6)
    
    context = {
        'wishlist': wishlist_items,
    }
    return render(request, "profile.html", context)


@login_required
def add_to_wishlist(request, gemstone_id):
    gemstone = get_object_or_404(Gemstone, pk=gemstone_id)
    profile = request.user.userprofile
    wishlist, created = Wishlist.objects.get_or_create(user=profile.user)
    if gemstone in wishlist.gemstones.all():
        wishlist.gemstones.remove(gemstone)
        messages.success(request, f"{gemstone.name} removed from your wishlist")
    else:
        wishlist.gemstones.add(gemstone)
        messages.success(request, "Gemstone added to your wishlist.")

    return redirect('gemstone_detail', gemstone_id=gemstone.id)

