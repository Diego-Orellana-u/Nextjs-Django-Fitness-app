import django_filters
from .models import FoodItem, NutritionGoal, ConsumedItem, MealTemplate, TemplateItem, MEAL_TIMES

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

class ConsumedItemsFilter(django_filters.FilterSet):
  log = django_filters.NumberFilter()
  time_of_day = django_filters.ChoiceFilter(choices=MEAL_TIMES)

  class Meta:
    model = ConsumedItem
    fields = []

class MealTemplatesFilter(django_filters.FilterSet):
  time_of_day = django_filters.ChoiceFilter(choices=MEAL_TIMES)

  class Meta:
    model = MealTemplate
    fields = []

class TemplateProductFilter(django_filters.FilterSet):
  meal_plan = django_filters.NumberFilter()

  class Meta:
    model = TemplateItem
    fields = []