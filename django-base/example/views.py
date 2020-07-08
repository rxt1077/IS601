import random

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import BakedGood, BakedGoodForm, IngredientForm

def index(request):
    baked_goods = BakedGood.objects.all()
    context = {'baked_goods': baked_goods}
    return render(request, 'example/index.html', context)
    
def extend(request):
    return render(request, 'example/extend.html')

def for_view(request):
    baked_goods = BakedGood.objects.all()
    context = {'baked_goods': baked_goods}
    return render(request, 'example/for.html', context)

def if_view(request):
    baked_goods = BakedGood.objects.all()
    context = {'baked_goods': baked_goods}
    return render(request, 'example/if.html', context)
    
def cool_view(request):
    baked_goods = BakedGood.objects.filter(good_type='CO')
    context = {'baked_goods': baked_goods}
    return render(request, 'example/cool.html', context)
    
def random_view(request):
    baked_goods = BakedGood.objects.all()
    random_baked_good = random.choice(baked_goods)
    context = {'baked_good': random_baked_good}
    return render(request, 'example/random.html', context)

def bake(request):
    if request.method == 'POST':
        form = BakedGoodForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = BakedGoodForm()

    return render(request, 'example/bake.html', {'form': form})
    
def ingredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = IngredientForm()
        
    return render(request, 'example/ingredient.html', {'form': form})
