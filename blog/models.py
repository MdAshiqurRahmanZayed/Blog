import datetime
from email import message
from operator import truediv
from pickle import TRUE
import profile
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# from django.utils import timezone
# import datetime
# from datetime import date,datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingFormField
from ckeditor_uploader.fields import RichTextUploadingField
# from froala_editor.fields import FroalaField
from category.models import *
from django.conf import settings
from .helpers import *
# from taggit.managers import TaggableManager




STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Profile(models.Model):
    user =  models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,null=True,blank=True)
    last_name = models.CharField(max_length=100,null=True,blank=True)
    username = models.CharField(max_length=50,null=True,blank=True)
    bio =RichTextField(max_length=500)
    profile_picture = models.ImageField(null=True, blank=True, upload_to="images/profile", height_field=None, width_field=None, max_length=None)
    birthday =  models.DateField(blank=True, null=True)
    website = models.URLField(blank=True)
    facebook_url = models.CharField(max_length=255,null=True,blank=True)
    twitter_url = models.CharField(max_length=255,null=True,blank=True)
    istagram_url = models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.user.get_username()
    def get_absolute_url(self): # new
        return reverse('home')


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True, max_length=250, null=True, blank=True)
    subtitle = models.CharField(max_length=255, blank=True)
    heder_image =  models.ImageField(null=False,blank=True,upload_to="images/")
    heder_image_url =  models.CharField(null=True,blank=True,max_length=200)
    heder_image_Under_line =  models.TextField(null=True,default="image")
    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    body   = RichTextUploadingField(null=True,blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    meta_description = models.TextField(max_length=300, blank=True,default='click link above to read the blog post')
    category = models.ForeignKey(Category,on_delete= models.CASCADE)
    # comments = models.TextField(blank=True,null=True)
    
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)
    # tags = TaggableManager()
    
    slider = models.BooleanField(default=False)
    
    # def __str__(self):
    #     return self.title + " | "+str(self.author)
    def get_url(self):
        return reverse('post_detail',args=[self.category.slug,self.slug])
    



    class Meta:
        ordering = ['-created_on']
        
        
    def get_absolute_url(self): # new
        return reverse('post_detail', args=[self.category.slug,self.slug])
    
    
    # def save(self , *args, **kwargs): 
    #     self.slug = generate_slug(self.title)
    #     super(Post, self).save(*args, **kwargs)
    def save(self, *args, **kwargs):  # new
        if not self.slug:
            slug_str = f"{self.title}-{datetime.datetime.now()}"
            self.slug = slugify(slug_str, allow_unicode=True)
        return super().save(*args, **kwargs)





     
     
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
    
    
    
    
class Contact(models.Model):
    name = models.CharField( max_length=50)
    email = models.CharField( max_length=50)
    subject = models.CharField( max_length=50)
    message = models.TextField()
    
    
    def __str__(self):
        return self.name+' '+self.email 
    
    def get_absolute_url(self): # new
        return reverse('home')