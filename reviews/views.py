from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import ReviewForm
from .models import Review


def reviews(request):
    reviews = Review.objects.all().order_by('-created_on')
    p = Paginator(reviews, 6)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your review!')
            return redirect('reviews')
        else:
            messages.error(request, 'Something went wrong! Please try again.')
    else:
        form = ReviewForm()

    context = {
        'reviews': reviews,
        'page_obj': page_obj,
        'form':form,
    }

    return render(request, 'reviews/reviews.html', context)


def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    review.delete()
    return redirect('reviews')
