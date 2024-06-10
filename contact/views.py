from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError

from .forms import ContactForm


def contact(request):
    """
    Render the contact form page and handle form submission.

    When a POST request is received, validate the submitted form data.
    If the form is valid, save the form data, send a confirmation email to the user,
    and redirect to the contact_success page. If the form is invalid, display
    an error message to the user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object rendering the contact form page.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            send_contact_success_email(form.cleaned_data['email'])
            return redirect('contact_success')
        else:
            messages.error(request, 'There was an error with your submission. Please try again.')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})


def contact_success(request):
    """
    Render the contact success page.

    Returns:
        HttpResponse: The HTTP response object rendering the contact success page.
    """
    return render(request, 'contact/contact_success.html')


def send_contact_success_email(user_email):
    """
    Send a confirmation email to the user upon successful contact form submission.

    Args:
        user_email (str): The email address of the user who submitted the contact form.
    """
    subject = 'Contact Form Received'
    message_body = 'Thank you for contacting us! We will get back to you as soon as possible!'
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
