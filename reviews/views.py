from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ReviewForm
from .models import Review


def reviews(request):
    reviews = Review.objects.all().order_by('-created_on')
    return render(request, 'reviews/reviews.html', {'reviews': reviews})


def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your review!')
            return redirect('reviews')
        else:
            messages.error(
                    request, 'Something went wrong! Please try again.'
                )
    else:
        form = ReviewForm()
    return render(request, 'reviews/reviews.html', {'form':form})
