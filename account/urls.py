
from django.urls import path,include
from .views import *

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name='register'),
    path('create_profile_page/', CreateProfilePageView.as_view(),name='create_profile_page'),
    path('update_profile_page/<int:pk>', UpdateProfilePageView.as_view(),name='update_profile_page'),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(),name='show_profile_page'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('change-password/', PasswordsChangeView.as_view(template_name='registration/change_password.html'),name='change_password'),
    path('password_success/', password_success, name='password_success'),
    
]
