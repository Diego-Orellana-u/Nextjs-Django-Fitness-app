from django.urls import path
from . import views

urlpatterns = [
  path('products/<str:brand>/', views.ProductBrandList.as_view()),
  path('products/<int:id>/', views.product_detail),
  path('goals/<int:user>', views.nutrition_goals),
  path('goals/<int:user>/<str:goalName>', views.nutrition_goal_individual),
  path('dailylog/<int:user>', views.daily_food_log_list),
  path('dailylog/<int:user>/<str:date>', views.daily_food_log_individual),
  path('consumeditems/<int:logid>', views.ConsumedItemsList.as_view()),
  path('mealtemplates/<int:user>', views.meal_template_list),
  path('mealtemplates/<int:user>/<int:meal_id>', views.meal_template_individual),
  path('templateitems/<int:user>/<int:meal_plan_id>', views.template_items_list),
]