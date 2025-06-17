from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import FoodItem, NutritionGoal, DailyFoodLog, ConsumedItem, MealTemplate
from .serializers import ProductSerializer, NutriGoalsSerializer, DailyFoodLogSerializer, ConsumedItemsSerializer, MealTemplatesSerializer

# Create your views here.
@api_view(['GET'])
def product_brand_list(request, brand):
  if request.method == 'GET':
    products = FoodItem.objects.filter(brand=brand)
    serializer = ProductSerializer(products, many=True)
  return Response(serializer.data)

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

@api_view(['GET', 'POST'])
def nutrition_goals(request, user):
  goal = NutritionGoal.objects.filter(user_id=user)
  if(request.method == 'GET'):
    serializer = NutriGoalsSerializer(goal, many=True)
  elif request.method == 'POST':
    serializer = NutriGoalsSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

  return Response(serializer.data)

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


@api_view(['GET', 'POST'])
def daily_food_log_list(request, user):
  foodLog = DailyFoodLog.objects.filter(user_id=user )
  if(request.method == 'GET'):
    serializer = DailyFoodLogSerializer(foodLog, many=True)

  if(request.method == 'POST'):
    serializer = DailyFoodLogSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
  return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def daily_food_log_individual(request, user, date):
  foodLog = get_object_or_404(DailyFoodLog, user_id=user, date=date)
  if(request.method == 'GET'):
    serializer = DailyFoodLogSerializer(foodLog)

  if(request.method == 'DELETE'):
    foodLog.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
  if(request.method == 'PUT'):
    serializer = DailyFoodLogSerializer(foodLog, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.data)


@api_view(['GET'])
def consumed_items_list(request, logid):
  consumedItem = ConsumedItem.objects.filter(log_id=logid)
  if(request.method == 'GET'):
    serializer = ConsumedItemsSerializer(consumedItem, many=True)

  return Response(serializer.data)

@api_view(['GET'])
def meal_template_list(request,user):
  mealTemplates = MealTemplate.objects.filter(user_id=user)
  if(request.method == 'GET'):
    serializer = MealTemplatesSerializer(mealTemplates, many=True)

  return Response(serializer.data)