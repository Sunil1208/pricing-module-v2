from django.http import JsonResponse
from .models import PricingConfig

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

