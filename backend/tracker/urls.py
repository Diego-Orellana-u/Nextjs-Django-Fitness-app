from django.urls import path
from . import views

urlpatterns = [
  path('products/<int:id>/', views.product_detail),
  path('products/<str:brand>/', views.product_brand_list)
]