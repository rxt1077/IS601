import random

from django.http import HttpResponse
from django.shortcuts import render

from .models import BakedGood

def index(request):
    return HttpResponse("Nothing to see here... yet.")
    
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
    
