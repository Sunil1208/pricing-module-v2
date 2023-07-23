import logging
from django import forms
from django.utils import timezone
from .models import PricingConfig

logger = logging.getLogger('pricing_module')

class CustomPricingConfigForm(forms.ModelForm):
    class Meta:
        model = PricingConfig
        fields = '__all__'

    def save(self, commit=True):
        instance = super().save(commit=commit)
        if commit:
            logger.info(f"Configuration '{instance.name}' changed at {timezone.now()}.")
        return instance
