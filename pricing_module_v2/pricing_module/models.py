from django.db import models

class PricingConfig(models.Model):
    name = models.CharField(max_length=100)
    distance_base_price = models.DecimalField(max_digits=8, decimal_places=2)
    distance_additional_price = models.DecimalField(max_digits=8, decimal_places=2)
    time_multiplier_factor = models.DecimalField(max_digits=8, decimal_places=2)
    waiting_charges = models.DecimalField(max_digits=8, decimal_places=2)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
