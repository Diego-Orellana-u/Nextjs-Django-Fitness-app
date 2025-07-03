from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from .exceptions import NoContentException
from .models import FoodItem, NutritionGoal, DailyFoodLog, ConsumedItem, MealTemplate, TemplateItem
from .serializers import ProductSerializer, NutriGoalsSerializer, DailyFoodLogSerializer, ConsumedItemsSerializer, MealTemplatesSerializer, TemplateItemSerializer
from .filters import ProductFilter, NutritionGoalFilter, ConsumedItemsFilter


class ProductsViewSet(ModelViewSet):
  queryset = FoodItem.objects.all()
  serializer_class = ProductSerializer

  filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
  search_fields = ['name', 'brand']
  filterset_class = ProductFilter
  ordering_fields = ['protein_per_100g', 'calories_per_100g']


class NutritionGoalViewSet(ModelViewSet):
  queryset = NutritionGoal.objects.all()
  serializer_class = NutriGoalsSerializer
  
  filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
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

  filter_backends = [DjangoFilterBackend]
  filterset_class = ConsumedItemsFilter

class MealTemplateByUserId(ListCreateAPIView):
  def get_queryset(self):
    mealTemplates = MealTemplate.objects.filter(user_id=self.kwargs['user_id'])
    if mealTemplates:
      return mealTemplates
    else:
      raise NoContentException
    
  serializer_class = MealTemplatesSerializer

class MealTemplateById(RetrieveUpdateDestroyAPIView):
  lookup_field = 'user_id'

  def get_queryset(self):
    mealTemplate = MealTemplate.objects.filter(user_id=self.kwargs['user_id'], pk=self.kwargs['meal_id'])
    if MealTemplate:
      return mealTemplate
    else:
      raise NoContentException
  
  serializer_class = MealTemplatesSerializer

class TemplateProductsByMealTemplateId(ListCreateAPIView):
  def get_queryset(self):
    queryset = TemplateItem.objects.filter(meal_plan_id__user_id=self.kwargs['user_id']).filter(meal_plan_id=self.kwargs['meal_template_id'])
    if queryset:
      return queryset
    else:
      raise NoContentException()
  
  serializer_class = TemplateItemSerializer

class TemplateProductById(RetrieveUpdateDestroyAPIView):
  lookup_field = 'id'
  def get_queryset(self):
    queryset = TemplateItem.objects.filter(meal_plan_id__user_id=self.kwargs['user_id']).filter(meal_plan_id=self.kwargs['meal_template_id'])
    if queryset:
      return queryset
    else:
      raise NoContentException()
  
  serializer_class = TemplateItemSerializer
