from django.shortcuts import render
from django.http import HttpResponse
from .models import Brand_s
from .models import Product_s
from django.views.generic import DetailView


def index(request):

    news = Brand_s.objects.all()
    return render(request, 'main/index.html', {'news': news})

   #return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def item(request):
    return render(request, 'main/item.html')

def brand(request): 
    return render(request, 'main/brand.html')

class NewDetailView2(DetailView):
    model = Product_s
    template_name = 'main/test-product.html'
    context_object_name = 'beticle'

    
class NewDetailView(DetailView):
    model = Brand_s
    template_name = 'main/test.html'
    context_object_name = 'article'