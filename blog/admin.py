from django.contrib import admin
from .models import *

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    
    list_display = (
        'user',
        'birthday',
        'website',
    )

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post

    list_display = (
        "id",
        "title",
        'category',
        'created_on',
        # "subtitle",
        # "slug",
        "publish_date",
        "published",
        "slider",
    )
    list_filter = (
        "published",
        "publish_date",
    )
    list_editable = (
        "title",
        # "subtitle",
        # "slug",
        "publish_date",
        "published",
        "slider",
    )
    search_fields = (
        "title",
        "subtitle",
        "slug",
        "body",
    )
    prepopulated_fields = {
        "slug": (
            "title",
            "subtitle",
        )
    }
    date_hierarchy = "publish_date"
    save_on_top = True


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']
    list_editable = (

        "active",
    )

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    model = Contact
    
    list_display = (
        'name',
        'email',
        'subject',      
    )
    
    

admin.site.register(About)
admin.site.register(TeamLeader)

# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title','category',"publish_date","published",'created_on')
#     list_filter = ("status",)
#     search_fields = ['title', 'content']
#     prepopulated_fields = {'slug': ('title',)}

# admin.site.register(Post, PostAdmin)