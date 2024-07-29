from django.shortcuts import render
# IMPORT DATABASE MODEL
from item.models import Category, Item


def index(request):
    # 0 to 6 items
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })


def contact(request):
    return render(request, 'core/contact.html')
