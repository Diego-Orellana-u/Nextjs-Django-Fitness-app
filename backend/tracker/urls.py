from django.urls import path
from . import views

urlpatterns = [
  # Endpoints to retrieve, post, delete and update products. Both as a list and individual
  path('products/search/<str:search_term>/', views.ProductsByNameOrBrand.as_view()),
  path('products/<int:product_id>/', views.ProductById.as_view()),

  # Endpoints to retrieve the nutrition goals list for a specific user and a specific nutrition goal of that user
  path('nutritiongoals/search/<int:user_id>', views.NutritionGoalsListByUserId.as_view()),
  path('nutritiongoals/<int:user_id>/<int:goal_id>', views.NutritionGoalByGoalId.as_view()),

  # Endpoints to the daily logs list of users and a specific daily log. Consumed items have a foreign key with daily logs.
  path('dailyfoodlog/search/<int:user_id>', views.DailyFoodLogByUserId.as_view()),
  path('dailyfoodlog/<int:user_id>/<int:log_id>', views.DailyFoodLogByLogId.as_view()),

  # Endpoints to the list of items associated with a certain log and to an specific consumed item. They show quantities, macros, daily log id associated with, etc.
  path('consumeditems/search/<int:log_id>', views.ConsumedItemsByDailyLogId.as_view()),
  path('consumeditems/<int:id>', views.ConsumedItemById.as_view()),

  # Endpoints to meal templates list and specific meal teamplate.
  path('mealtemplates/search/<int:user_id>', views.MealTemplateByUserId.as_view()),
  path('mealtemplates/<int:user_id>/<int:meal_id>', views.MealTemplateById.as_view()),

  # Endpoints to the list of products (or individual product) related to a meal template
  path('templateproducts/<int:user_id>/<int:meal_template_id>', views.TemplateProductsByMealTemplateId.as_view()),
  path('templateproducts/<int:user_id>/<int:meal_template_id>/<int:id>', views.TemplateProductById.as_view()),
]