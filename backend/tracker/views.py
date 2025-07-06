from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from .exceptions import NoContentException
from .models import FoodItem, NutritionGoal, DailyFoodLog, ConsumedItem, MealTemplate, TemplateItem
from .serializers import ProductSerializer, NutriGoalsSerializer, DailyFoodLogSerializer, ConsumedItemsSerializer, MealTemplatesSerializer, TemplateItemSerializer
from .filters import ProductFilter, NutritionGoalFilter, ConsumedItemsFilter, MealTemplatesFilter, TemplateProductFilter


class ProductsViewSet(ModelViewSet):
  queryset = FoodItem.objects.all()
  serializer_class = ProductSerializer

  filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
  search_fields = ['name', 'brand']
  filterset_class = ProductFilter
  ordering_fields = ['protein_per_100g', 'calories_per_100g']


class NutritionGoalViewSet(ModelViewSet):
  queryset = NutritionGoal.objects.all()
  serializer_class = NutriGoalsSerializer
  
  filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
  search_fields = ['name']
  filterset_class = NutritionGoalFilter
  ordering_fields = ['target_calories', 'start_date']


class DailyFoodLogViewSet(ModelViewSet):
  queryset = DailyFoodLog.objects.all()
  serializer_class = DailyFoodLogSerializer
  filter_backends = [OrderingFilter]
  ordering_fields = ['date']


class ConsumedItemsViewSet(ModelViewSet):
  queryset = ConsumedItem.objects.all()
  serializer_class = ConsumedItemsSerializer

  filter_backends = [DjangoFilterBackend, OrderingFilter]
  filterset_class = ConsumedItemsFilter
  ordering_fields = ['created_at', 'calories_consumed', 'proteins_consumed']

class MealTemplatesViewSet(ModelViewSet):
  queryset = MealTemplate.objects.all()
  serializer_class = MealTemplatesSerializer
  filter_backends = [DjangoFilterBackend, SearchFilter]
  filterset_class = MealTemplatesFilter


class TemplateProductViewSet(ModelViewSet):
  queryset = TemplateItem.objects.all()
  serializer_class = TemplateItemSerializer

  filter_backends = [DjangoFilterBackend]
  filterset_class = TemplateProductFilter