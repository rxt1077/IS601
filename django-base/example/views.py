from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.forms import modelformset_factory

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

def ajax(request):
    return render(request, 'example/ajax.html')

def ajax_demo(request):
    data = []
    for baked_good in BakedGood.objects.all():
        data.append({"name": baked_good.name, "desc": baked_good.desc})

    return JsonResponse({"data": data})
    
def bake_formset(request):
    BakedGoodFormSet = modelformset_factory(BakedGood, extra=5,
            fields=['name', 'desc', 'good_type', 'price', 'recipe'])
    if request.method == 'POST':
        formset = BakedGoodFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        formset = BakedGoodFormSet(queryset=BakedGood.objects.none())

    return render(request, 'example/bake_formset.html', {'formset': formset})