from django import forms
from django.core.validators import EmailValidator

from .models import NewsletterSubscriber


class NewsletterSubscriptionForm(forms.ModelForm):
    email = forms.EmailField(
        validators=[EmailValidator(
            message="Please enter a valid email address.")])

    class Meta:
        model = NewsletterSubscriber
        fields = ['email']
