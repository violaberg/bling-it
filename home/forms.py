from django import forms
from django.core.validators import EmailValidator

from .models import NewsletterSubscriber


class NewsletterSubscriptionForm(forms.ModelForm):
    """
    Form for subscribing to the newsletter.

    This form allows users to subscribe to the newsletter \
    by providing their email address.
    """
    email = forms.EmailField(
        validators=[EmailValidator(
            message="Please enter a valid email address.")])

    class Meta:
        model = NewsletterSubscriber
        fields = ['email']
