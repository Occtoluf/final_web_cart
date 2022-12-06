from django.shortcuts import render, redirect
from django.views.generic import View, CreateView
from cart.models import OrderLine, Order
from cart.services.cart import get_or_create_cart, add_to_cart, count_total, write_off_postions
from cart.services.notification import send_notification
from cart.forms import ContactInformationForm


class BuyView(View):
    def post(self, request):
        """ Добавление товаров к корзину """
        cart = get_or_create_cart()
        add_to_cart(cart, request)
        return redirect('cart:detail')


class CartView(View):
    def get(self, request):
        """ Просмотр корзины """
        cart = get_or_create_cart()
        order_lines = OrderLine.objects.filter(order=cart).prefetch_related('position')
        return render(request, 'cart/detail.html', {
            'order_lines': order_lines,
            'total': count_total(order_lines)
        })


class RemoveCart(View):
    def get(self, request):
        """ Удаление товаров в корзине """
        cart = get_or_create_cart()
        cart.delete()

        return redirect('cart:detail')


class ConfirmCreateView(CreateView):
    template_name = 'cart/confirmation.html'
    form_class = ContactInformationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = get_or_create_cart()
        order_lines = OrderLine.objects.filter(order=cart).prefetch_related('position')
        context['total'] = count_total(order_lines)
        return context

    def form_valid(self, form):
        contact_information = form.save(commit=False)
        pay_method = form.cleaned_data['pay_method']
        contact_information.save()
        cart = get_or_create_cart()
        Order.objects.filter(id=cart.id).update(
            contact_information=contact_information,
            status='in_delivery',
            type_payment=pay_method
        )
        write_off_postions(cart)

        order_lines = OrderLine.objects.filter(order=cart).prefetch_related('position')
        send_notification(order_lines, count_total(order_lines), contact_information, pay_method)
        return redirect('home')
