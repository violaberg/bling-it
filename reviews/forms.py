from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'review_subject', 'review_body', 'rating']
        widgets = {
            'name': forms.TextInput(attrs={'autocomplete': 'name'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'

        css_class = (
            'crispy-btn custom-gemstone-btn btn text-uppercase rounded-0'
        )
        submit_button = Submit('submit', 'Submit', css_class=css_class)
        self.helper.add_input(submit_button)
