# Generated by Django 4.1.7 on 2023-12-20 17:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cake",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("comment", models.TextField(max_length=200)),
                ("image_url", models.URLField()),
                (
                    "yum_factor",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(5),
                            django.core.validators.MinValueValidator(1),
                        ]
                    ),
                ),
            ],
            options={
                "ordering": ["id"],
            },
        ),
    ]
