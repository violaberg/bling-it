from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string

from .models import UserProfile, Gemstone, Wishlist
from .forms import UserProfileForm
from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    # Render wishlist template within profile context
    wishlist_template = render_to_string(
        'profiles/wishlist.html', {'wishlist': wishlist}, request=request)

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'wishlist_content': wishlist_template,
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
def wishlist(request):
    """ A view to return the wishlist page"""

    return render(request, "profiles/wishlist.html")


@login_required
def add_to_wishlist(request, gemstone_id):
    if request.method == 'POST':
        gemstone = get_object_or_404(Gemstone, pk=gemstone_id)

        # Ensure the user is authenticated before proceeding
        if not request.user.is_authenticated:
            messages.error(
                request, 'Please login to add this gemstone to your wishlist.')
            return redirect('login')

        # Get or create the wishlist for the user
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        
        # Toggle gemstone addition/removal based on whether it's already in the wishlist
        if gemstone in wishlist.gemstone.all():
            wishlist.gemstone.remove(gemstone)
            messages.success(
                request, f'{gemstone.name} removed from your wishlist')
        else:
            wishlist.gemstone.add(gemstone)
            messages.success(
                request, f'{gemstone.name} added to your wishlist')

        return redirect('gemstone_detail')

    else:
        # Handle invalid request method (GET, PUT, etc.)
        messages.error(request, 'Invalid request method.')
        return redirect('gemstone_detail')
