from django.contrib import admin

from tgc.models import Categories, Items, Subcategory, Users

# Register your models here.

admin.site.register(Categories)
admin.site.register(Items)
admin.site.register(Subcategory)
admin.site.register(Users)
