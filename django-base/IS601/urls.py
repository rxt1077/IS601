from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('example/', include('example.urls')),
    path('example2/', include('example2.urls')),
    path('admin/', admin.site.urls), 
]