from django.db import models
from django.forms import ModelForm

class Ingredient(models.Model):
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=256)

class BakedGood(models.Model):
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=256)
    type_choices = [
        ('BA', 'Bagel'),
        ('BR', 'Bread'),
        ('CO', 'Cookie'),
        ('CA', 'Cake'),
        ('PR', 'Pretzel'),
    ]
    good_type = models.CharField(max_length=2, choices=type_choices)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    recipe = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)

class BakedGoodForm(ModelForm):
    class Meta:
        model = BakedGood
        fields = ['name', 'desc', 'good_type', 'price', 'recipe', 'ingredients']
