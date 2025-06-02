from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FoodItem
from .serializers import productSerializer

# Create your views here.
@api_view(['GET'])
def product_brand_list(request, brand):
  if request.method == 'GET':
    products = FoodItem.objects.filter(brand=brand)
    serializer = productSerializer(products, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def product_detail(request, id):
  if request.method == 'GET':
    product = FoodItem.objects.get(pk=id)
    serializer = productSerializer(product)

  return Response(serializer.data)