from django import forms
from .widgets import CustomClearableFileInput
from .models import Gemstone, Category


class GemstoneForm(forms.ModelForm):
    """
    Form for creating and updating gemstones.

    This form extends the ModelForm class to provide a form interface
    for creating and updating gemstones. It includes all fields from the
    Gemstone model and customizes the image field with a custom clearable
    file input widget.
    """

    class Meta:
        model = Gemstone
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput
        )

    def __init__(self, *args, **kwargs):
        """
        Initialize the GemstoneForm.

        This method customizes the form's fields by setting the choices
        for the category field to friendly names retrieved from the Category
        model. It also adds CSS classes to the form fields for styling.
        """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-blue rounded-0'
