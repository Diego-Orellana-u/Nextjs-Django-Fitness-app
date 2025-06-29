from django.db.models import Q
import django_filters
from .models import FoodItem

class ProductFilter(django_filters.FilterSet):
  protein_gte = django_filters.NumberFilter(field_name='protein_per_100g', lookup_expr='gte')

  class Meta:
    model = FoodItem
    fields = []