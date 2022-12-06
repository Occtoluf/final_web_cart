from django.urls import path
from cart.views import CartView, BuyView, RemoveCart, ConfirmCreateView

app_name = 'cart'

urlpatterns = [
    path('', CartView.as_view(), name='detail'),
    path('add', BuyView.as_view(), name='add'),
    path('remove', RemoveCart.as_view(), name='remove'),
    path('confirm', ConfirmCreateView.as_view(), name='confirm')

]