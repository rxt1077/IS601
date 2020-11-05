from django.db import models
from django.forms import ModelForm

class BakedGood(models.Model):
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=256)
    good_type = models.CharField(
        max_length=2,
        choices=[
            ('BG',"Bagel"),
            ('BR',"Bread"),
            ('CO',"Cookie"),
            ('CA',"CAKE"),
            ('PR',"PRETZEL")
        ]
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    recipe = models.TextField()
    
class BakedGoodForm(ModelForm):
    class Meta:
        model = BakedGood
        fields = ['name', 'desc', 'good_type', 'price', 'recipe']