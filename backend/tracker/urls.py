from django.urls import path
from . import views

urlpatterns = [
  path('products/<int:id>/', views.product_detail),
  path('products/<str:brand>/', views.product_brand_list),
  path('goals/<int:user>', views.nutrition_goals),
  path('goals/<int:user>/<str:goalName>', views.nutrition_goal_detail)
]