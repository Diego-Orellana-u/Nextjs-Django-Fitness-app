from django.urls import path
from . import views

urlpatterns = [
  path('products/<str:brand>/', views.ProductBrandList.as_view()),
  path('products/<int:id>/', views.product_detail),
  path('goals/<int:user>', views.NutritionGoals.as_view()),
  path('goals/<int:user>/<str:goalName>', views.nutrition_goal_individual),
  path('dailylog/<int:user>', views.DailyFoodLogList.as_view()),
  path('dailylog/<int:user>/<str:date>', views.DailyFoodLogIndividual.as_view()),
  path('consumeditems/<int:logid>', views.ConsumedItemsList.as_view()),
  path('mealtemplates/<int:user>', views.MealTemplateList.as_view()),
  path('mealtemplates/<int:user>/<int:meal_id>', views.MealTemplateIndividual.as_view()),
  path('templateitems/<int:user>/<int:meal_plan_id>', views.TemplateItemsList.as_view()),
]