from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('brand/<int:brand_id>/', views.show_brand, name='brand'),
    path('product/<int:prod_id>', views.show_product, name='product'),
    path('cart/', views.cart, name='cart'),
    path('confirmation/', views.confirmation, name='confirmation'),
]



