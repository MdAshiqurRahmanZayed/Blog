from django.urls import path
from .views import *


urlpatterns = [
    path('',home,name='home'),
    path('all-post/',PostListView,name='all_post'),
    path('add-a-new-post/',PostCreateView.as_view(),name='add_post'),
    path('all-post/category=<slug:category_slug>',AllPost_by_category,name='post_by_category'),
    path('<slug:category_slug>/<slug:post_slug>',PostDetail,name= 'post_detail'),
    path('article/update/<slug:slug>/', UpdatePostView.as_view(), name='update_post'),
    path('article/delete/<slug:slug>/', DeletePostView.as_view(), name='delete_post'),
]
