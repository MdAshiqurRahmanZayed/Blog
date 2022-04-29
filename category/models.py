from django.db import models

# Create your models here.
# from audioop import reverse
from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
     parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank = True, null=True)
     category_name = models.CharField(max_length=50,unique=True)
     slug = models.SlugField(max_length=100,unique=True)
     description =models.TextField(max_length=300,blank=True)
     cat_image = models.ImageField(upload_to = 'photo/categories',blank = True)
     created_at = models.DateTimeField(auto_now_add=True)
     
     
     def __str__(self):
          return self.category_name


     class Meta:
          verbose_name = "Category"
          verbose_name_plural = "Categories"
          unique_together = ('slug', 'parent',)    
          
     def get_url(self):
          return reverse('products_by_category',args=[self.slug])

     
     
     def __str__(self):                           
        full_path = [self.category_name]                  
        k = self.parent
        while k is not None:
            full_path.append(k.category_name)
            k = k.parent
        return ' -> '.join(full_path[::-1])
     
     

     # def get_absolute_url(self):
     #      return reverse("category_detail", kwargs={"pk": self.pk})
