from rest_framework import serializers
from .models import FoodItem
class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = FoodItem
    fields = ['name','brand','off_barcode','calories_per_100g', 'protein_per_100g', 'carbs_per_100g', 'fat_per_100g', 'common_serving_size_grams', 'created_at', 'updated_at']