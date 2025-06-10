from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import FoodItem, NutritionGoal
from .serializers import ProductSerializer, NutriGoalsSerializer

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

@api_view(['GET', 'POST', 'DELETE'])
def nutrition_goals(request, user):
  goal = NutritionGoal.objects.filter(user_id=user)
  if(request.method == 'GET'):
    serializer = NutriGoalsSerializer(goal, many=True)
  elif request.method == 'POST':
    serializer = NutriGoalsSerializer(data=request.data)
    print(request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
  # elif request.method = 'DELETE':
  return Response(serializer.data)
