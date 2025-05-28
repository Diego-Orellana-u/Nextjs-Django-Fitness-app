from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FoodItem

# Create your views here.
@api_view(['GET'])
def product_list(request):
  # if request.method == 'GET':
  #   queryset = FoodItem.objects.
  return Response('ok')

@api_view(['GET'])
def product_detail(request):
  return Response('ok')