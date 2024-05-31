from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError

from .forms import NewsletterSubscriptionForm
from .models import FAQ


def index(request):
    """A view to return the index page with subscription form"""
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            try:
                # Call the send_subscription_email function
                send_subscription_email(email)
                messages.success(request, 'You have successfully subscribed to the newsletter!')

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            except Exception as e:
                messages.error(request, f'An error occurred: {e}')
        else:
            messages.error(request, 'Please enter a valid email address.')
    return render(request, 'home/index.html')


def about(request):
    """ A view to return the About Us page"""

    return render(request, "home/about_us.html")


def faq(request):
    """ A view to return the FAQ page"""
    faqs = FAQ.objects.all()

    return render(request, "home/faq.html", {'faqs': faqs})


def privacy_policy(request):
    """ A view to return the Privacy Policy page"""

    return render(request, "home/privacy_policy.html")


def subscribe_to_newsletter(request):
    """ A view for newsletter subscription"""
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            form.save()
            # Send confirmation email
            try:
                send_subscription_email(email)
                messages.success(request, 'Thank you for subscribing to our newsletter!')
            except Exception as e:
                messages.error(request, f'Thank you for subscribing, but an error occurred when sending the confirmation email: {e}')
        else:
            messages.error(request, 'There was an error with your submission.')
    else:
        form = NewsletterSubscriptionForm()

    return render(request, 'index.html', {'form': form})


def send_subscription_email(user_email):
    subject = 'Subscription Confirmation'
    message_body = 'Thank you for subscribing to our newsletter!'
    signature = '\n\nSincerely yours,\nBling It!'
    message = f"{message_body}{signature}"
    from_email = 'viola.bergere@gmail.com'
    recipient_list = [user_email]

    try:
        send_mail(subject, message, from_email, recipient_list)
    except BadHeaderError:
        return HttpResponse('Invalid header found.')
    except Exception as e:
        raise Exception(f'An error occurred: {e}')
    