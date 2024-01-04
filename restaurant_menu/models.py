from django.db import models
from django.contrib.auth.models import User

MEAL_TYPE = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_dishes", "Main Dishes"),
    ("desserts", "Desserts"),
)

STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)


class Item(models.Model):
    meal = models.CharField(max_length=1000, unique=True)
    description = models.CharField(max_length=4000)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    category = models.CharField(max_length=200, choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_uploaded = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal
