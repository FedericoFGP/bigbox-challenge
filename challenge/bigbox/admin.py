from django.contrib import admin
from .models import *

class ActivityAdmin(admin.ModelAdmin):
   # fields = ['category', 'description'] 

   fieldsets = [
       (None,               {'fields': ['category','purchase_available']}),
       ('Datos',            {'fields': ['description', 'name', 'internal_name']}),
   ]
   # exclude = ['internal_name']
class BoxInline(admin.StackedInline):
    model = Box
    extra = 3

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['name']}),
        ('Datos',           {'fields': ['description','order','slug']}),
    ]
    inlines = [BoxInline]

admin.site.register(Activity, ActivityAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Box)
admin.site.register(Reason)
