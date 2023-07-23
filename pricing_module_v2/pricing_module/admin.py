import logging
from django.contrib import admin
from django.utils import timezone
from .models import PricingConfig
from .forms import CustomPricingConfigForm

pricing_logger = logging.getLogger('pricing_module')  # Logger for pricing_module app

def get_fields_diff(obj, form):
    """
    Helper function to get the fields that were changed along with their old and new values.
    """
    changed_fields = {}
    for field in form.fields:
        old_value = getattr(obj, field)
        new_value = form.cleaned_data.get(field)
        if old_value != new_value:
            changed_fields[field] = {
                'old_value': old_value,
                'new_value': new_value,
            }
    return changed_fields

class PricingConfigAdmin(admin.ModelAdmin):
    form = CustomPricingConfigForm

    def save_model(self, request, obj, form, change):
        # Log the change when saving the model in the admin panel
        if change:
            changed_fields = get_fields_diff(obj, form)
            obj.save()
            if changed_fields:
                pricing_logger.info(f"Configuration '{obj.name}' changed by user: {request.user} at {timezone.now()}. Changes: {changed_fields}.")
            else:
                pricing_logger.info(f"Configuration '{obj.name}' saved by user: {request.user} at {timezone.now()}.")

admin.site.register(PricingConfig, PricingConfigAdmin)

