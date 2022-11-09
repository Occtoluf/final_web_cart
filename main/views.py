from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from .models import Brand_s
from .models import Product_s
from django.views.generic import DetailView


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

    items = Product_s.objects.all()
    brands = Brand_s.objects.all()
    it = items[prod_id-1]

    el = it.category
    br = brands[1]

    

    
    '''for b in brands:
        if Brand_s.objects.filter( = b.id):
            br = b
            break
    
    br = brands[el-1]


    for x in brands:
        if x.name == el:
            br = x
            break

    


def brand(request, catid): 
    return render(request, 'main/brand.html', )

def item(request):
    return render(request, 'main/item.html')


class NewDetailView2(DetailView):
    model = Product_s
    template_name = 'main/test-product.html'
    context_object_name = 'beticle'
    x = Brand_s.objects.all()
    

    extra_context = {'penek': Brand_s.objects.all()}
    
class NewDetailView(DetailView):
    model = Brand_s
    template_name = 'main/test.html'
    context_object_name = 'article'
    x = Product_s.objects.all()

    extra_context = {'taburetka': Product_s.objects.all()}'''

    context = {
        'it': it,
        'br' : br,
    }
    return render(request, 'main/test-product.html', context=context)