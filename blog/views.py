from tkinter import EXCEPTION
from unicodedata import category
# from unicodedata import category
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
# from django.http import HttpResponse
# Create your views here.
from .models import *
from category.models import *
from django.views.generic import *
from .forms import *
from django.core.paginator import Paginator


def home(request):
     category = Category.objects.all().filter(parent=None)
   #   post_by_category = Post.objects.filter(category__category_name="Computer",published=True).order_by('-created_on')
   #   post_by_computer = Post.objects.filter(category=Category.objects.get(category_name="Computer"),published=True).order_by('-created_on')
     post_by_category = Post.objects.filter(published=True).order_by('-category')


     slider = Post.objects.filter(slider=True).order_by('-created_on')


     context = {
          'category':category,
          'post_by_category':post_by_category,
          'slider':slider,
         #  'page_obj':page_obj,
     }
     return render(request,'home.html',context)



# class PostListView(ListView):
#     model = Post
#     t = model.objects.all().filter(published=True)
#     template_name = "all_post.html"
    
def PostListView(request):
     object_list = Post.objects.all().filter(published=True).order_by('-created_on')
     category = Category.objects.all().filter(parent=None)
     p = Paginator(object_list, 5)  # creating a paginator object
    # getting the desired page number from url
     page_number = request.GET.get('page')
     try:
        page_obj = p.get_page(page_number)  # returns the desired page object
     except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
     except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)     
     
     
     context={
          "post":object_list,
          'page_obj':page_obj,
          'category':category,
     }
     return render(request,'all_post.html',context)



def AllPost_by_category(request,category_slug=None):
     categories = None
     page_obj   = None
     
     if category_slug !=None :
        categories     = get_object_or_404(Category, slug = category_slug)
        page_obj           = Post.objects.filter(category=categories,published=True)
        post_count     = page_obj.count()
     else:
        page_obj           = Post.objects.all(published=True)
        post_count     = page_obj.count()
        
     #paginator
     category = Category.objects.all().filter(parent=None)
     p = Paginator(page_obj, 5)  # creating a paginator object
    # getting the desired page number from url
     page_number = request.GET.get('page')
     try:
        page_obj = p.get_page(page_number)  # returns the desired page object
     except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
     except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)     
     

     
     context  ={
        'page_obj':page_obj,
        'post_count':post_count,
     }
    
     return render(request,'all_post.html',context)

def PostDetail(request,category_slug,post_slug):
   try:
      single_post = Post.objects.get(category__slug=category_slug ,slug=post_slug)
   except EXCEPTION as e:
      raise e
   context = {
      'single_post':single_post,
      
   }

   return render(request,'post_detail.html',context)


class PostCreateView(CreateView): # new
   model = Post
   form_class = PostForm
   template_name = 'add_post.html'



class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.html"
    
class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")
   