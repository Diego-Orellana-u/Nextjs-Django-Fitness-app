from django.core.management.base import BaseCommand
from tracker.models import FoodItem
import duckdb
import pandas as pd

class Command(BaseCommand):
    help = "Load food items from filtered Chilean OpenFoodFacts Parquet into the DB"

    def handle(self, *args, **kwargs):
        df = duckdb.query("SELECT * FROM '/home/diego/Programacion/nextjs-Django-Fitness-app/backend/filtered_chile_food_data.parquet'").to_df()

        count = 0
        for _, row in df.iterrows():
            # === Strings ===
            name = str(row.get("name") or "").strip()[:200]
            brand = str(row.get("brands") or "").strip()[:150]
            off_barcode = str(row.get("off_barcode") or "").strip()[:50]

            # === Decimals ===
            def safe_decimal(val, precision=2):
                if pd.notnull(val):
                    return round(float(val), precision)
                return None

            calories = safe_decimal(row.get("calories_numeric"), 2)
            protein = safe_decimal(row.get("protein_numeric"), 2)
            carbs = safe_decimal(row.get("carbs_numeric"), 2)
            fat = safe_decimal(row.get("fat_numeric"), 2)

            serving_raw = row.get("serving_size")
            serving_grams = None
            if isinstance(serving_raw, str) and "g" in serving_raw:
                try:
                    serving_grams = float(serving_raw.lower().replace("g", "").strip())
                except ValueError:
                    serving_grams = None

            if not name or any(val is None for val in [calories, protein, carbs, fat]):
                continue

            try:
                FoodItem.objects.create(
                    name=name,
                    brand=brand,
                    off_barcode=off_barcode or None,
                    calories_per_100g=calories,
                    protein_per_100g=protein,
                    carbs_per_100g=carbs,
                    fat_per_100g=fat,
                    common_serving_size_grams=serving_grams
                )
                count += 1
            except Exception as e:
                self.stderr.write(f"Failed to insert: {name} - Error: {e}")

        self.stdout.write(self.style.SUCCESS(f"✅ Inserted {count} food items."))
