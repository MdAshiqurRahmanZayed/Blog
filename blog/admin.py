from django.contrib import admin
from .models import Profile, Post, Tag


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


# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title','category',"publish_date","published",'created_on')
#     list_filter = ("status",)
#     search_fields = ['title', 'content']
#     prepopulated_fields = {'slug': ('title',)}

# admin.site.register(Post, PostAdmin)