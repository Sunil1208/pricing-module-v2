from django.urls import path
from . import views

urlpatterns = [
    path('calculate_pricing/', views.calculate_pricing, name='calculate_pricing'),
    path('pricing_config/', views.pricing_config_view, name='pricing_config_view'),
]
