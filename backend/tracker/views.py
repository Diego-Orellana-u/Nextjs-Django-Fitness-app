from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from .exceptions import NoContentException
from django.shortcuts import get_object_or_404
from .models import FoodItem, NutritionGoal, DailyFoodLog, ConsumedItem, MealTemplate, TemplateItem
from .serializers import ProductSerializer, NutriGoalsSerializer, DailyFoodLogSerializer, ConsumedItemsSerializer, MealTemplatesSerializer, TemplateItemSerializer

class ProductBrandList(ListAPIView):
  def get_queryset(self):
    return FoodItem.objects.filter(brand=self.kwargs['brand'])
  
  serializer_class = ProductSerializer

@api_view(['GET', 'POST', 'DELETE'])
def product_detail(request, id):
  product = get_object_or_404(FoodItem, pk=id)
  if request.method == 'GET':
    serializer = ProductSerializer(product)

  elif request.method == 'POST':
    serializer = ProductSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

  elif request.method == 'DELETE':
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  return Response(serializer.data)


class NutritionGoals(ListCreateAPIView):
  def get_queryset(self):
    nutriGoal = NutritionGoal.objects.filter(user_id=self.kwargs['user'])
    if nutriGoal:
      return nutriGoal
    else:
      raise NoContentException
  
  serializer_class = NutriGoalsSerializer

@api_view(['GET','POST', 'DELETE'])
def nutrition_goal_individual(request, user, goalName):
  goal = get_object_or_404(NutritionGoal,user_id=user, name=goalName)
  if(request.method == 'GET'):
    serializer = NutriGoalsSerializer(goal)
  elif(request.method == 'POST'):
    serializer = NutriGoalsSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
  elif request.method == 'DELETE':
    goal.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  return Response(serializer.data)

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

@api_view(['GET', 'POST'])
def meal_template_list(request,user):
  mealTemplates = MealTemplate.objects.filter(user_id=user)
  if(request.method == 'GET'):
    serializer = MealTemplatesSerializer(mealTemplates, many=True)

  if(request.method == 'POST'):
    print(request.data)
    serializer = MealTemplatesSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
  return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def meal_template_individual(request, user, meal_id):
  mealTemplate = get_object_or_404(MealTemplate, user_id=user, pk=meal_id )
  if(request.method == 'GET'):
    serializer = MealTemplatesSerializer(mealTemplate)

  if(request.method == 'PUT'):
    serializer = MealTemplatesSerializer(mealTemplate, data=request.data)  
    serializer.is_valid(raise_exception=True)
    serializer.save()
  if(request.method == 'DELETE'):
    mealTemplate.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  return Response(serializer.data)


class TemplateItemsList(ListAPIView):
  def get_queryset(self):
    queryset = TemplateItem.objects.filter(meal_plan_id__user_id=self.kwargs['user']).filter(meal_plan_id=self.kwargs['meal_plan_id'])
    if queryset:
      return queryset
    else:
      raise NoContentException()
  
  serializer_class = TemplateItemSerializer
