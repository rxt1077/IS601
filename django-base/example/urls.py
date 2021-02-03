from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu', views.menu, name='menu'),
    path('asdf', views.menu, name='asdf'),
    path('bake', views.bake, name='bake'),
    path('ajax', views.ajax, name='ajax'),
    path('ajax-demo', views.ajax_demo, name='ajax-demo'),
    path('bake-multiple', views.bake_formset, name='bake-multiple'),
]