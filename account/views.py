from dataclasses import field
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import *
from blog.models import Profile
# Create your views here.
from django.contrib.auth.forms import *
from .forms import *
from django.contrib.auth.views import PasswordChangeView



class UserRegisterView(CreateView):
     form_class = SignUpForm
     template_name = 'registration/register.html'
     success_url = reverse_lazy('login')

class CreateProfilePageView(CreateView):
    model = Profile
    template_name = "create_user_profile_page.html"
    form_class = ProfilePageForm
    #fields = '__all__'
    def form_valid(self,form):
         form.instance.user = self.request.user
         return super().form_valid(form)
    
    
class UpdateProfilePageView(UpdateView):
     model = Profile
     template_name = 'update_profile_page.html'
     form_class=UpdateProfilePageForm
     # fields = ['bio', 'profile_picture', 'website','birthday',
     #           'facebook_url', 'twitter_url', 'istagram_url']

     
     success_url = reverse_lazy('home')

class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'edit_profile_setting.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
         return self.request.user


class PasswordsChangeView(PasswordChangeView):
     form_class = PasswordChangingForm
     # form_class = PasswordChangingForm
     success_url = reverse_lazy('password_success')
     
     
def password_success(request):
     return render(request,'registration/password_success.html')


class ShowProfilePageView(DetailView):
     model = Profile
     template_name = 'user_profile.html'
