from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)

    def __str__(self):
        return "Ingredient [{}]".format(self.name)


class Unit(models.Model):
    name = models.CharField(max_length=200)
    unit_type = models.CharField(max_length=200)
    unit_coeff = models.FloatField(default=1.0)

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    amount = models.IntegerField(null=True, blank=True)
    amount_type = models.ForeignKey(Unit, default=None, blank=True, null=True)

    def __str__(self):
        return "{} {} of {}".format(self.amount, self.amount_type, self.ingredient)


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return "Tag [{}]".format(self.name)


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(RecipeIngredient)
    definition = models.TextField()
