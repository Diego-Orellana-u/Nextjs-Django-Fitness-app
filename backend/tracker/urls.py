from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('products', views.ProductsViewSet)
router.register('nutritiongoals', views.NutritionGoalViewSet)
router.register('dailyfoodlog', views.DailyFoodLogViewSet)
router.register('consumeditems', views.ConsumedItemsViewSet)

# Instead of using complex url's like user_id/goal_id, I can use only goal_id and to get the specific goal use the goal_id + the used id permission

urlpatterns = [
  path('', include(router.urls)),

  # Endpoints to the list of items associated with a certain log and to an specific consumed item. They show quantities, macros, daily log id associated with, etc.
  # path('consumeditems/search/<int:log_id>', views.ConsumedItemsByDailyLogId.as_view()),
  # path('consumeditems/<int:id>', views.ConsumedItemById.as_view()),

  # Endpoints to meal templates list and specific meal teamplate.
  path('mealtemplates/search/<int:user_id>', views.MealTemplateByUserId.as_view()),
  path('mealtemplates/<int:user_id>/<int:meal_id>', views.MealTemplateById.as_view()),

  # Endpoints to the list of products (or individual product) related to a meal template
  path('templateproducts/<int:user_id>/<int:meal_template_id>', views.TemplateProductsByMealTemplateId.as_view()),
  path('templateproducts/<int:user_id>/<int:meal_template_id>/<int:id>', views.TemplateProductById.as_view()),
]