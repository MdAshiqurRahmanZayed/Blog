
from dataclasses import field
from django import forms
from .models import *
choices = Category.objects.all().values_list('category_name', 'category_name')
choices_list = []

for item in choices:
    choices_list.append(item)

class PostForm(forms.ModelForm):
     
     class Meta:
          model = Post

          fields =('title','category','author','heder_image',
                   'heder_image_url','heder_image_Under_line', 'body',
                   'meta_description', 'published','tags')
          widgets = {
              'title': forms.TextInput(attrs={'class': 'form-control'}),
               'slug': forms.TextInput(attrs={'class':'form-control'}),
               'category': forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
               'author': forms.TextInput(attrs={'class': 'form-control','value':'','id':'elder','type':'hidden'}),
               'heder_image_Under_line': forms.TextInput(attrs={'class':'form-control'}),
               # 'author': forms.TextInput(attrs={'class': 'form-control','value':'','id':'elder','type':'hidden'}),
               'heder_image_url': forms.TextInput(attrs={'class':'form-control'}),
               'body': forms.Textarea(attrs={'class':'form-control'}),
               'meta_description': forms.TextInput(attrs={'class':'form-control'}),
               
          }
      
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category','heder_image','heder_image_url',
                  'heder_image_Under_line', 'body','meta_description','tags' )

        widgets = {
              'title': forms.TextInput(attrs={'class': 'form-control'}),
               'category': forms.Select(choices=choices_list, attrs={'class': 'form-control'}),
               'heder_image_url': forms.TextInput(attrs={'class':'form-control'}),
               'heder_image_Under_line': forms.TextInput(attrs={'class':'form-control'}),
               # 'author': forms.TextInput(attrs={'class': 'form-control','value':'','id':'elder','type':'hidden'}),
               'body': forms.Textarea(attrs={'class':'form-control'}),
               'meta_description': forms.TextInput(attrs={'class':'form-control'}),
              
        }
