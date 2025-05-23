# Generated by Django 5.2 on 2025-05-13 15:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_consumeditem_dailyfoodlog_fooditem_mealitem_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditem',
            name='common_serving_size_unit',
        ),
        migrations.CreateModel(
            name='TemplateItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serving_quantity', models.DecimalField(decimal_places=2, max_digits=7)),
                ('serving_unit', models.CharField(choices=[('g', 'Grams'), ('ml', 'Milliliters'), ('piece', 'Piece'), ('cup', 'Cup'), ('tbsp', 'Tablespoon')], max_length=10)),
                ('food_item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tracker.fooditem')),
                ('meal_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.mealtemplate')),
            ],
        ),
        migrations.DeleteModel(
            name='MealItem',
        ),
    ]
