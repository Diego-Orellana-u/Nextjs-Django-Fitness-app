from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView,RetrieveDestroyAPIView ,RetrieveUpdateDestroyAPIView
from rest_framework import status
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
  lookup_field = 'id'
  lookup_url_kwarg = 'id'
  def get_queryset(self):
    product = FoodItem.objects.filter(id=self.kwargs['id'])
    if product:
      return product
    else: 
      raise NoContentException

  serializer_class = ProductSerializer

class NutritionGoals(ListCreateAPIView):
  def get_queryset(self):
    nutriGoal = NutritionGoal.objects.filter(user_id=self.kwargs['user'])
    if nutriGoal:
      return nutriGoal
    else:
      raise NoContentException
  
  serializer_class = NutriGoalsSerializer

class NutritionGoalIndividual(RetrieveUpdateDestroyAPIView):
  lookup_field = 'user'
  lookup_url_kwarg = 'user'
  def get_queryset(self):
    nutritionGoal = NutritionGoal.objects.filter(user_id=self.kwargs['user'], name=self.kwargs['goalName'])
    if nutritionGoal:
      return nutritionGoal
    else: 
      raise NoContentException
    
  serializer_class = NutriGoalsSerializer

class DailyFoodLogList(ListCreateAPIView):
  def get_queryset(self):
    dailyLog = DailyFoodLog.objects.filter(user_id=self.kwargs['user'])
    if dailyLog:
      return dailyLog
    else: 
      raise NoContentException
  
  serializer_class = DailyFoodLogSerializer

class DailyFoodLogIndividual(RetrieveUpdateDestroyAPIView):
  lookup_url_kwarg = 'user'
  lookup_field = 'user'
  def get_queryset(self):
    dailyLog = DailyFoodLog.objects.filter(user_id=self.kwargs['user'], date=self.kwargs['date'])
    if dailyLog:
      return dailyLog
    else: 
      raise NoContentException
  serializer_class = DailyFoodLogSerializer

class ConsumedItemsList(ListAPIView):
  def get_queryset(self):
    return ConsumedItem.objects.filter(log_id=self.kwargs['logid'])

  serializer_class = ConsumedItemsSerializer

class MealTemplateList(ListCreateAPIView):
  def get_queryset(self):
    mealTemplates = MealTemplate.objects.filter(user_id=self.kwargs['user'])
    if mealTemplates:
      return mealTemplates
    else:
      raise NoContentException
    
  serializer_class = MealTemplatesSerializer

class MealTemplateIndividual(RetrieveUpdateDestroyAPIView):
  lookup_field = 'user'
  lookup_url_kwarg = 'user'

  def get_queryset(self):
    mealTemplate = MealTemplate.objects.filter(user_id=self.kwargs['user'], pk=self.kwargs['meal_id'])
    if MealTemplate:
      return mealTemplate
    else:
      raise NoContentException
  
  serializer_class = MealTemplatesSerializer

class TemplateItemsList(ListAPIView):
  def get_queryset(self):
    queryset = TemplateItem.objects.filter(meal_plan_id__user_id=self.kwargs['user']).filter(meal_plan_id=self.kwargs['meal_plan_id'])
    if queryset:
      return queryset
    else:
      raise NoContentException()
  
  serializer_class = TemplateItemSerializer
