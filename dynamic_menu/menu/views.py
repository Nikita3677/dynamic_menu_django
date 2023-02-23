from django.shortcuts import render
from menu.models import Category, SubCategory


def index(request):
    return render(request, 'index.html')

def category(request, slug):
    menu = Category.objects.get(slug=slug)
    context = {
        'menu': menu,
    }
    return render(request, 'menu/category.html', context)

def sub_category(request, slug, sub_slug):
    menu = SubCategory.objects.select_related('category').get(slug=sub_slug)
    context = {
        'menu': menu,
    }
    return render(request, 'menu/sub_category.html', context)