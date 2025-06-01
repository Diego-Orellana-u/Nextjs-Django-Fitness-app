from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FoodItem
from .serializers import productSerializer

# Create your views here.
@api_view(['GET'])
def product_list(request):
  # if request.method == 'GET':
  #   queryset = FoodItem.objects.
  return Response('ok')

@api_view(['GET'])
def product_detail(request, id):
  if request.method == 'GET':
    product = FoodItem.objects.get(pk=id)
    serializer = productSerializer(product)

  return Response(serializer.data)