from django import forms
from .models import booking

class booking(forms.ModelForm):
    class Meta:
        model = booking
        fields = ('name','done')
        