from django import forms
from .models import PricingConfig

class PricingConfigForm(forms.ModelForm):
    class Meta:
        model = PricingConfig
        fields = '__all__'
