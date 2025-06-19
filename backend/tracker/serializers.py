from rest_framework import serializers
from .models import FoodItem, NutritionGoal, DailyFoodLog, ConsumedItem, MealTemplate, TemplateItem
class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = FoodItem
    fields = ['name','brand','off_barcode','calories_per_100g', 'protein_per_100g', 'carbs_per_100g', 'fat_per_100g', 'common_serving_size_grams', 'created_at', 'updated_at']


class NutriGoalsSerializer(serializers.ModelSerializer):
  class Meta:
    model = NutritionGoal
    fields = ['name', 'target_calories', 'target_carbs', 'target_proteins', 'target_fats', 'is_active', 'start_date', 'user']


class DailyFoodLogSerializer(serializers.ModelSerializer):

  class Meta:
    model = DailyFoodLog
    fields = ['user', 'date']


class ConsumedItemsSerializer(serializers.ModelSerializer):

  class Meta:
    model = ConsumedItem
    fields = ['log', 'food_item', 'serving_quantity', 'serving_unit', 'time_of_day', 'created_at', 'calories_consumed', 'carbs_consumed', 'proteins_consumed', 'fats_consumed']


class MealTemplatesSerializer(serializers.ModelSerializer):

  class Meta:
    model = MealTemplate
    fields = ['name', 'user', 'time_of_day']

class TemplateItemSerializer(serializers.ModelSerializer):

  class Meta:
    model = TemplateItem
    fields = ['meal_plan', 'food_item', 'serving_quantity', 'serving_unit']