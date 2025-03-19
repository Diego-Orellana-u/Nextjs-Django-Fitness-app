from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    

UNITS = [
  ("g", "Grams"),
  ("ml", "Milliliters"),
  ("piece", "Piece"),
  ("cup", "Cup"),
  ("tbsp", "Tablespoon"),
]

class FoodItem(models.Model):
  name = models.CharField(max_length=200, db_index=True, unique=True)
  calories_per_100g = models.DecimalField(max_digits=7, decimal_places=2, help_text="Calories per 100g")
  protein_per_100g = models.DecimalField(max_digits=7, decimal_places=2, help_text="Protein (g) per 100g")
  carbs_per_100g = models.DecimalField(max_digits=7, decimal_places=2, help_text="Carbohydrates (g) per 100g")
  fat_per_100g = models.DecimalField(max_digits=7, decimal_places=2, help_text="Fat (g) per 100g")

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.name

class MacroPlan(models.Model):
  name = models.CharField(max_length=255)
  target_calories = models.DecimalField(max_digits=6, decimal_places=2)
  target_carbs = models.DecimalField(max_digits=6, decimal_places=2)
  target_proteins = models.DecimalField(max_digits=6, decimal_places=2)
  target_fats = models.DecimalField(max_digits=6, decimal_places=2)

  start_date = models.DateTimeField(default=timezone.now, )

  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class DailyFoodLog(models.Model):
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  date  = models.DateField()

  class Meta:
    unique_together = ("user", "date")


MEAL_TIMES = [
  ("B", "Breakfast"),
  ("L", "Lunch"),
  ("D", "Dinner"),
  ("S", "Snack")
]
class ConsumedItem(models.Model):
  #FoodItem
  log = models.ForeignKey(DailyFoodLog, on_delete=models.CASCADE)
  food_item = models.ForeignKey(FoodItem, on_delete=models.PROTECT)
  serving_quantity = models.DecimalField(max_digits=7, decimal_places=2) #To use fractions and not just integers
  serving_unit = models.CharField(max_length=10, choices=UNITS)
  time_of_day = models.CharField(max_length=10, choices=MEAL_TIMES)

class MealPlan(models.Model):
  name = models.CharField(max_length=10)
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  time_of_day = models.CharField(max_length=10, choices=MEAL_TIMES)

class MealItem(models.Model):
  meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE)
  food_item = models.ForeignKey(FoodItem, on_delete=models.PROTECT)
  serving_quantity = models.DecimalField(max_digits=7, decimal_places=2)
  serving_unit = models.CharField(max_length=10, choices=UNITS)