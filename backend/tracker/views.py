from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FoodItem

# Create your views here.
@api_view(['GET'])
def get_food(request):
  # if request.method == 'GET':
    # queryset = FoodItem.objects.
  return Response('ok')