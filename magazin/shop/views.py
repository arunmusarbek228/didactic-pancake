from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        # Если выбрана категория, фильтруем по ней
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    else:
        # Если это главная страница, фильтруем только популярные
        products = products.filter(is_popular=True)

    return render(request, 'shop/product/list.html', {
        'category': category,
        'categories': categories,
        'products': products,
    })
