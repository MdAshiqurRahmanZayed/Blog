from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
from .models import *
from category.models import *
def home(request):
     category = Category.objects.filter(parent=None)
     context = {
          'catg':category,
     }
     return render(request,'home.html',context)