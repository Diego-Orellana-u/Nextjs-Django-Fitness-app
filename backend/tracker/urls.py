from django.urls import path
from . import views

urlpatterns = [
  # Endpoints to retrieve, post, delete and update products. Both as a list and individual
  path('products/search/<str:search_term>/', views.ProductsByNameOrBrand.as_view()),
  path('products/<int:id>/', views.ProductById.as_view()),

  # Endpoints to retrieve the nutrition goals list for a specific user and a specific nutrition goal of that user
  path('nutritiongoals/<int:user>', views.NutritionGoalsListByUserId.as_view()),
  path('nutritiongoals/<int:user>/<int:goal_id>', views.NutritionGoalByGoalId.as_view()),

  # Endpoints to 
  path('dailylog/<int:user>', views.DailyFoodLogList.as_view()),
  path('dailylog/<int:user>/<int:log_id>', views.DailyFoodLogIndividual.as_view()),

  path('consumeditems/search/<int:log_id>', views.ConsumedItemsList.as_view()),
  path('consumeditems/<int:id>', views.ConsumedItemIndividual.as_view()),
  path('mealtemplates/<int:user>', views.MealTemplateList.as_view()),
  path('mealtemplates/<int:user>/<int:meal_id>', views.MealTemplateIndividual.as_view()),
  path('templateitems/<int:user>/<int:meal_plan_id>', views.TemplateItemsList.as_view()),
  path('templateitems/<int:user>/<int:meal_plan_id>/<int:id>', views.TemplateItemsIndividual.as_view()),
]