from rest_framework import serializers
from .models import FoodItem
class ProductSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  name = serializers.CharField(max_length=200)
  brand = serializers.CharField(max_length=150)
  off_barcode = serializers.CharField(max_length=50, help_text="Unique barcode from Open Food Facts")
  calories_per_100g = serializers.DecimalField(max_digits=7, decimal_places=2,)
  protein_per_100g = serializers.DecimalField(max_digits=7, decimal_places=2,)
  carbs_per_100g = serializers.DecimalField(max_digits=7, decimal_places=2,)
  fat_per_100g = serializers.DecimalField(max_digits=7, decimal_places=2,)
  common_serving_size_grams = serializers.DecimalField(max_digits=7, decimal_places=2, help_text="Weight in grams for the common serving size (if applicable)")
  created_at = serializers.DateTimeField(read_only=True)
  updated_at = serializers.DateTimeField(read_only=True)

  
  def create(self, validated_data):
    return FoodItem.objects.create(**validated_data)