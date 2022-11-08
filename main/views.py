from django.shortcuts import render
from django.http import HttpResponse
from .models import Brand_s
from .models import Product_s
from django.views.generic import DetailView


def index(request):

    news = Brand_s.objects.all()
    return render(request, 'main/index.html', {'news': news})

"""def index (request):
    brand = Brand_s.objects.all()
    context = {
        'brand' : brand
    }
    return render (request,'main/index.html', context)"""

def about(request):
    return render(request, 'main/about.html')

def item(request):
    return render(request, 'main/item.html')

def brand(request): 
    return render(request, 'main/brand.html', )

"""def brand (request, id):
    brands__1 = Brand_s.objects.get(pk=id)
    context = {
        'brandsss': brands__1
    }
    session_key = request.session.session_key
    if not session_key:
        request.session["session_key"]=123
        request.session.cycle_key()
        print(request.session.session_key)
    return render (request,'main/brand.html', context)"""


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

    extra_context = {'taburetka': Product_s.objects.all()}