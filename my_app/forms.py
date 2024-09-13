from django import forms
from .models import Star

class StarForm(forms.ModelForm):
    class Meta:
        model = Star
        fields = ['star', 'rating']