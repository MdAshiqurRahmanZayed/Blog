from .models import Category

def menu_links(request):
     menu_links = Category.objects.filter(parent=None)
     return dict(menu_links=menu_links)