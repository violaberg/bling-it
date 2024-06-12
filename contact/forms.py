from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form class for the contact model.

    This form class is used to create a form for the Contact model. \
    It specifies the fields to include and \
    any additional widgets for those fields.
    """

    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'email': forms.EmailInput(attrs={'autocomplete': 'email'}),
            'name': forms.TextInput(attrs={'autocomplete': 'name'})
        }
