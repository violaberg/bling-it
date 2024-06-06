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
def wishlist(request, pk):
    """ A view to return the wishlist page"""

    profile = get_object_or_404(UserProfile, id=pk)
    wishlist = Wishlist.objects.filter(user=profile).order_by('-created')
    wishlist = gemstones_pagination(request, wishlist, 6)
    context = {
        'wishlist': wishlist,
    }
    return render(request, "profiles/wishlist.html")


@login_required
def add_to_wishlist(request, pk):
    profile = request.user.userprofile
    gemstone = get_object_or_404(Gemstone, pk=gemstone_id)
    redirect_url = request.POST.get('redirect_url')

    wishlist, created = Wishlist.objects.get_or_create(
        user=profile, gemstone=gemstone)
    if created:
        messages.success(request, f'{gemstone.name} was succesfully added to your wishlist!')
    else:
        wishlist.delete()
        messages.success(
            request, f'{gemstone.name} was removed from your wishlist!')

    return redirect(redirect_url)
