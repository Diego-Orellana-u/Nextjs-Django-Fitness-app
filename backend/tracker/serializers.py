from rest_framework import serializers

class product_serializer(serializers.serializer):
  id = serializers.IntegerField()
  name = serializers.CharField()
  brand = serializers.CharField()
  off_barcode = serializers.CharField()
  calories_per_100g = serializers.DecimalField()
  protein_per_100g = serializers.DecimalField()
  carbs_per_100g = serializers.DecimalField()
  fat_per_100g = serializers.DecimalField()
  common_serving_size_grams = serializers.DecimalField()
  created_at = serializers.DateTimeField()
  updated_at = serializers.DateTimeField()