from django import forms
from .models import CoreValue

class CoreValueForm(forms.ModelForm):
    class Meta:
        model = CoreValue
        fields = ['value']