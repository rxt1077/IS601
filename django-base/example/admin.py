from django.contrib import admin

from .models import BakedGood, Ingredient
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class BakedGoodResource(resources.ModelResource):
    class Meta:
        model = BakedGood

class BakedGoodAdmin(ImportExportModelAdmin):
    resource_class = BakedGoodResource

admin.site.register(BakedGood, BakedGoodAdmin)
admin.site.register(Ingredient)
