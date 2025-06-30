import django_filters
from .models import FoodItem, NutritionGoal

class ProductFilter(django_filters.FilterSet):
  protein_gte = django_filters.NumberFilter(field_name='protein_per_100g', lookup_expr='gte')

  class Meta:
    model = FoodItem
    fields = []

class NutritionGoalFilter(django_filters.FilterSet):
  is_active = django_filters.BooleanFilter()
  class Meta:
    model = NutritionGoal
    fields = []