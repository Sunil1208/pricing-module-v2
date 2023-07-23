from django.urls import path
from . import views

urlpatterns = [
    path('calculate_pricing/', views.calculate_pricing, name='calculate_pricing'),
]
