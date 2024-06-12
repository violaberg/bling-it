from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    """
    A customized clearable file input widget.

    This widget extends the default ClearableFileInput widget \
    provided by Django to customize labels and template paths.

    Attributes:
        clear_checkbox_label (str): The label for the clear checkbox.
        initial_text (str): The label for the initial file display.
        input_text (str): The label for the input field.
        template_name (str): The path to the custom template \
        for rendering the widget.
    """
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = (
        'gemstones/custom_widget_templates/custom_clearable_file_input.html'
    )
