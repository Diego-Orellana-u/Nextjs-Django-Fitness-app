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
    

class UserProfile(models.Model):
  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
  first_name = models.CharField(max_length=100, blank=True)
  last_name = models.CharField(max_length=100, blank=True)
  date_of_birth = models.DateField(null=True, blank=True)
  height = models.DecimalField(max_digits=3, decimal_places=2)
  weight = models.DecimalField(max_digits=3, decimal_places=2)

UNITS = [
  ("g", "Grams"),
  ("ml", "Milliliters"),
  ("piece", "Piece"),
  ("cup", "Cup"),
  ("tbsp", "Tablespoon"),
]

class FoodItem(models.Model):
  name = models.CharField(max_length=200, db_index=True)
  brand = models.CharField(max_length=150, blank=True, null=True, db_index=True)
  off_barcode = models.CharField(max_length=50, unique=True, help_text="Unique barcode from Open Food Facts", null=True, blank=True)

  calories_per_100g = models.DecimalField(max_digits=7, decimal_places=2, help_text="Calories per 100g")
  protein_per_100g = models.DecimalField(max_digits=7, decimal_places=2, help_text="Protein (g) per 100g")
  carbs_per_100g = models.DecimalField(max_digits=7, decimal_places=2, help_text="Carbohydrates (g) per 100g")
  fat_per_100g = models.DecimalField(max_digits=7, decimal_places=2, help_text="Fat (g) per 100g")

  # common_serving_size_unit = models.CharField(max_length=10, choices=UNITS, blank=True, null=True, help_text="e.g., 'cup', 'slice'")
  common_serving_size_grams = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True, help_text="Weight in grams for the common serving size (if applicable)")

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.name

class NutritionGoal(models.Model):
  name = models.CharField(max_length=255)
  target_calories = models.PositiveIntegerField()
  target_carbs = models.PositiveIntegerField()
  target_proteins = models.PositiveIntegerField()
  target_fats = models.PositiveIntegerField()

  is_active = models.BooleanField(default=True)

  start_date = models.DateField()

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
  created_at = models.DateTimeField(default=timezone.now)

  calories_consumed = models.DecimalField(max_digits=7, decimal_places=2)
  carbs_consumed = models.DecimalField(max_digits=7, decimal_places=2)
  proteins_consumed = models.DecimalField(max_digits=7, decimal_places=2)
  fats_consumed = models.DecimalField(max_digits=7, decimal_places=2)

class MealTemplate(models.Model):
  name = models.CharField(max_length=100)
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  time_of_day = models.CharField(max_length=10, choices=MEAL_TIMES)

class TemplateItem(models.Model):
  meal_plan = models.ForeignKey(MealTemplate, on_delete=models.CASCADE)
  food_item = models.ForeignKey(FoodItem, on_delete=models.PROTECT)
  serving_quantity = models.DecimalField(max_digits=7, decimal_places=2)
  serving_unit = models.CharField(max_length=10, choices=UNITS)