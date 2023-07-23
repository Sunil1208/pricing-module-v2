import logging
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone
from .models import PricingConfig
from .forms import PricingConfigForm

http_logger = logging.getLogger('django')  # Logger for HTTP requests
pricing_logger = logging.getLogger('pricing_module')  # Logger for pricing_module app

def calculate_pricing(request, additional_distance, ride_time, waiting_time):
    try:
        # Fetch the active pricing configuration (you can define the logic for this)
        active_config = PricingConfig.objects.filter(is_active=True).latest('created_at')
        
        # Perform the pricing calculation using the provided formula
        price = (active_config.distance_base_price + (additional_distance * active_config.distance_additional_price)) \
                + (ride_time * active_config.time_multiplier_factor) \
                + (waiting_time * active_config.waiting_charges)
        
        return JsonResponse({'price': price})
    except PricingConfig.DoesNotExist:
        return JsonResponse({'error': 'No active pricing configuration found.'}, status=404)


def pricing_config_view(request):
    if request.method == 'POST':
        form = PricingConfigForm(request.POST)
        if form.is_valid():
            instance = form.save()
            pricing_logger.info(f"Configuration '{instance.name}' changed by user: {request.user} at {timezone.now()}.")
            return redirect('.')  # Redirect back to the same page

    else:
        form = PricingConfigForm()
    
    # Log HTTP request when accessing the pricing configuration form
    http_logger.info(f"Accessed pricing configuration form at: {timezone.now()}")

    return render(request, 'pricing_module/config_form.html', {'form': form})
