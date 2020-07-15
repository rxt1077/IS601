from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('extend', views.extend, name='extend'),
    path('for', views.for_view, name='for'),
    path('if', views.if_view, name='if'),
    path('cool', views.cool_view, name='cool'),
    path('random', views.random_view, name='random'),
    path('bake', views.bake, name='bake'),
    path('ingredient', views.ingredient, name='ingredient'),
    path('ajax', views.ajax, name='ajax'),
    path('ajax-demo', views.ajax_demo, name='ajax-demo'),
]
