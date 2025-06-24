from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView,RetrieveDestroyAPIView ,RetrieveUpdateDestroyAPIView
from rest_framework import permissions, status
from rest_framework.viewsets import ModelViewSet
from .exceptions import NoContentException
from django.shortcuts import get_object_or_404
from .models import FoodItem, NutritionGoal, DailyFoodLog, ConsumedItem, MealTemplate, TemplateItem
from .serializers import ProductSerializer, NutriGoalsSerializer, DailyFoodLogSerializer, ConsumedItemsSerializer, MealTemplatesSerializer, TemplateItemSerializer



class ProductsByNameOrBrand(ListCreateAPIView):
  def get_queryset(self):
    productList = FoodItem.objects.filter(Q(name__icontains=self.kwargs['search_term']) | Q(brand__icontains=self.kwargs['search_term']))
    if productList:
      return productList
    else:
      raise NoContentException
  
  serializer_class = ProductSerializer

class ProductById(RetrieveUpdateDestroyAPIView):
  lookup_url_kwarg = 'product_id'
  def get_queryset(self):
    product = FoodItem.objects.filter(pk=self.kwargs['product_id'])
    if product:
      return product
    else: 
      raise NoContentException

  serializer_class = ProductSerializer

class NutritionGoalViewSet(ModelViewSet):
  queryset = NutritionGoal.objects.all()
  serializer_class = NutriGoalsSerializer


class DailyFoodLogViewSet(ModelViewSet):
  queryset = DailyFoodLog.objects.all()
  serializer_class = DailyFoodLogSerializer

class ConsumedItemsByDailyLogId(ListCreateAPIView):
  def get_queryset(self):
    return ConsumedItem.objects.filter(log_id=self.kwargs['log_id'])

  serializer_class = ConsumedItemsSerializer


class ConsumedItemById(RetrieveUpdateDestroyAPIView):
  lookup_field = 'id'
  def get_queryset(self):
    consumed_item = ConsumedItem.objects.filter(id=self.kwargs['id'])
    if consumed_item:
      return consumed_item
    else: 
      raise NoContentException
  
  serializer_class = ConsumedItemsSerializer

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
    queryset = TemplateItem.objects.filter(meal_plan_id__user_id=self.kwargs['user']).filter(meal_plan_id=self.kwargs['meal_template_id'])
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
