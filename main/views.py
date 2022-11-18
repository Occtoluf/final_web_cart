from django.shortcuts import render, get_object_or_404
from .models import Brand_s
from .models import Product_s


def index(request):

    news = Brand_s.objects.all()
    return render(request, 'main/index.html', {'news': news})

def about(request):
    
    return render(request, 'main/about.html')

def show_brand(request, brand_id):
    
    items = Product_s.objects.filter(category_id = brand_id)
    brands = Brand_s.objects.all()
    br = brands[brand_id-1]
    context = {
        'items': items,
        'br' : br,
    }
    return render(request, 'main/test.html', context=context)

def show_product(request, prod_id):

    item = get_object_or_404(Product_s, pk = prod_id)
    context = {
        'it': item,
        'br_id': item.category,
    }
    return render(request, 'main/test-product.html', context=context)

def cart(request):
    return render(request, 'main/cart.html')

def confirmation(request):
    return render(request, 'main/confirmation.html')
