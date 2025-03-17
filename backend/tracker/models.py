from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
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


UNITS = [
  ("g", "Grams"),
  ("ml", "Milliliters"),
  ("piece", "Piece"),
  ("cup", "Cup"),
  ("tbsp", "Tablespoon"),
]

MEAL_TIMES = [
  ("B", "Breakfast"),
  ("L", "Lunch"),
  ("D", "Dinner"),
  ("S", "Snack")
]
class ConsumedItem(models.Model):
  #FoodItem
  log = models.ForeignKey(DailyFoodLog, on_delete=models.CASCADE)
  quantity = models.DecimalField(max_digits=7, decimal_places=2) #To use fractions and not just integers
  unit = models.CharField(max_length=10, choices=UNITS)
  time_of_day = models.CharField(max_length=10, choices=MEAL_TIMES)


class MealPlan(models.Model):
  name = models.CharField(max_length=10)
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)