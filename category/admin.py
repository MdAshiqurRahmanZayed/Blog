
# Register your models here.
from django.contrib import admin
from .models import Category


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
     


admin.site.register(Category,CategoryAdmin)