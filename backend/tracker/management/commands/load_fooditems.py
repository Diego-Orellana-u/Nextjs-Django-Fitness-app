from django.core.management.base import BaseCommand
from tracker.models import FoodItem  # Your Django model
import duckdb

class Command(BaseCommand):
  help = "Load food items from a Chilean Parquet file into the DB"