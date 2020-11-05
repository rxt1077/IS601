from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import BakedGood, BakedGoodForm

def index(request):
    baked_goods = BakedGood.objects.all() 
    context = {'baked_goods': baked_goods} 
    return render(request, 'example/index.html', context)
    
def menu(request):
    baked_goods = BakedGood.objects.all()
    context = {'baked_goods': baked_goods}
    return render(request, 'example/for.html', context)
    
def bake(request):
    if request.method == 'POST':
        form = BakedGoodForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = BakedGoodForm()

    return render(request, 'example/bake.html', {'form': form})
