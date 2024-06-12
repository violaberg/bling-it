from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Form class for capturing and validating order information.

    This form is designed to capture data related to placing an order,
    including details such as the customer's full name, email address,
    phone number, shipping address, and other relevant contact information.
    It ensures that the provided data is valid according to the constraints
    specified in the associated Order model.

    Attributes:
    model (Order): The model associated with this form, providing the
                    structure and validation rules for the captured data.
    fields (tuple): A tuple specifying the fields to include in the form,
                    including 'full_name', 'email', 'phone_number',
                    'street_address1', 'street_address2', 'town_or_city',
                    'postcode', 'country', and 'county'.

    Methods:
    __init__(self, *args, **kwargs): Initializes the form instance with
                                    custom placeholders, classes, and
                                    autofocus settings for improved user
                                    experience.
    """
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State or Locality',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
