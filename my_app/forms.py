# from django import forms
# from .models import Star

# class StarForm(forms.ModelForm):
#     class Meta:
#         model = Star
#         fields = ['star', 'rating']

from django import forms
from .models import Vacation, Star

class VacationForm(forms.ModelForm):
    class Meta:
        model = Vacation
        fields = ['name', 'location', 'description', 'weather_conditions']  # Include all vacation fields

class StarForm(forms.ModelForm):
    class Meta:
        model = Star
        fields = ['star', 'rating']
