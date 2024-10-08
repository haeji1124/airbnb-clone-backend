from django.db import models

class House(models.Model):
    """Model Definition for Houses"""
    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField()
    description = models.TextField(default="")
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True)

    owner = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )