from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Cake(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    comment = models.TextField(max_length=200, null=False, blank=False)
    image_url = models.URLField(max_length=200, null=False, blank=False)
    yum_factor = models.PositiveIntegerField(
        null=False, blank=False, validators=[MaxValueValidator(5), MinValueValidator(1)]
    )

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.name}"
