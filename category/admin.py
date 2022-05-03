
# Register your models here.
from django.contrib import admin
from .models import Category,SubCategory


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
     prepopulated_fields = {
          'slug':('category_name',)
          }
     # list_display  = (
     #      'parent',
     #      'category_name',
     #      'slug',
          
     # )
class SubCategoryAdmin(admin.ModelAdmin):
     prepopulated_fields = {
          'slug':('category_name',)
          }     


admin.site.register(Category,CategoryAdmin)
# admin.site.register(SubCategory,SubCategoryAdmin)