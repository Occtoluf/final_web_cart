from django.shortcuts import render, get_object_or_404
from main.models import Brand_s, Product_s, Size, Position
from django.views.generic import View, TemplateView


class IndexView(View):
    """ Главная страница """

    def get(self, request):
        return render(request, 'main/index.html', {'brands': Brand_s.objects.all()})


class AboutTemplateView(TemplateView):
    """ О нас """

    template_name = 'main/about.html'


class BrandView(View):
    """ Просмотр товаров бренда """

    def get(self, request, brand_slug):
        br = get_object_or_404(Brand_s, slug=brand_slug)
        items = Product_s.objects.filter(category=br.id)
        return render(request, 'main/product/list.html', {'items': items, 'br': br})


class ProductDetailView(View):
    """ Детальная информация о продукте"""

    def get(self, request, id, prod_slug):
        item = get_object_or_404(Product_s, id=id, slug=prod_slug)
        positions = Position.objects.filter(product=item)
        return render(request, 'main/product/detail.html', {
            'it': item,
            'br_id': item.category,
            'positions': positions

        })


class ConfirmationTemplateView(TemplateView):
    """ Подтверждение заказа """

    template_name = 'main/confirmation.html'



