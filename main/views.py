from django.shortcuts import render, get_object_or_404
from .models import Brand_s
from .models import Product_s


def index(request):

    news = Brand_s.objects.all()
    return render(request, 'main/index.html', {'news': news})

def about(request):
    
    return render(request, 'main/about.html')

def show_brand(request, brand_slug):
    

    '''items = Product_s.objects.filter(category_id = brand_id)
    brands = Brand_s.objects.all()
    br = brands[brand_slug-1]'''

   
    #items = Product_s.objects.all()
    br = get_object_or_404(Brand_s, slug = brand_slug)
    items = Product_s.objects.filter(category = br.id)

    context = {
        'items': items,
        'br' : br,
    }
    return render(request, 'main/test.html', context=context)

def show_product(request, prod_slug):

    item = get_object_or_404(Product_s, slug = prod_slug)
    context = {
        'it': item,
        'br_id': item.category,
    }
    return render(request, 'main/test-product.html', context=context)

def cart(request):
    return render(request, 'main/cart.html')

def confirmation(request):
    return render(request, 'main/confirmation.html')
