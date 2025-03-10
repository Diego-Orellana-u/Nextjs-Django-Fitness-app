from django.db import models


class MacroPlan(models.Model):
  name = models.CharField(max_length=255)
  target_calories = models.DecimalField(max_digits=6, decimal_places=2)
  target_carbs = models.DecimalField(max_digits=6, decimal_places=2)
  target_proteins = models.DecimalField(max_digits=6, decimal_places=2)
  target_fats = models.DecimalField(max_digits=6, decimal_places=2)