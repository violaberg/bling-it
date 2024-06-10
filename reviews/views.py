from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import ReviewForm
from .models import Review


def reviews(request):
    """
    A view to display all reviews, paginated, and handle review submission.

    Retrieves all reviews from the database, orders them by creation date in descending order,
    and paginates them to display six reviews per page. If the request method is POST,
    it validates the submitted review form. If the form is valid, it saves the review,
    displays a success message, and redirects to the reviews page. If the form is invalid,
    it displays an error message. If the request method is GET, it renders the reviews template
    with the review form and paginated reviews.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML template displaying reviews.
    """
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
    """
    A view to delete a review.

    Deletes the review with the specified ID from the database.
    Displays a success message upon successful deletion and redirects to the reviews page.

    Args:
        request (HttpRequest): The HTTP request object.
        review_id (int): The ID of the review to be deleted.

    Returns:
        HttpResponseRedirect: Redirects to the reviews page.
    """
    review = get_object_or_404(Review, id=review_id)
    review.delete()
    messages.success(request, 'Review deleted succesfully!')
    return redirect('reviews')
