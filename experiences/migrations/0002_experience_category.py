# Generated by Django 5.1.1 on 2024-10-02 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0001_initial"),
        ("experiences", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="experience",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="categories.category",
            ),
        ),
    ]
