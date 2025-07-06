from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('products', views.ProductsViewSet)
router.register('nutritiongoals', views.NutritionGoalViewSet)
router.register('dailyfoodlog', views.DailyFoodLogViewSet)
router.register('consumeditems', views.ConsumedItemsViewSet)
router.register('mealtemplates', views.MealTemplatesViewSet)
router.register('templateproducts', views.TemplateProductViewSet)

# Instead of using complex url's like user_id/goal_id, I can use only goal_id and to get the specific goal use the goal_id + the used id permission

urlpatterns = [
  path('', include(router.urls)),
]

