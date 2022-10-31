from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Recepie(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Ingredient, through='Quantity')

    def __str__(self):
        return self.name + " [" + ', '.join([str(ig) for ig in self.ingredients.all()]) + "]"

class Quantity(models.Model):
    recepie = models.ForeignKey(Recepie, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return str(self.ingredient) + " * " + str(self.quantity) +  " -> " + str(self.recepie)
