from django import forms

from .models import Library
from .models import Floor


class SubmitForm(forms.ModelForm):

    class Meta:
        model = Floor
        fields = (rated_capacity)