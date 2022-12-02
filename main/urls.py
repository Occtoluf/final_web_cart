from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('brand/<slug:brand_slug>/', views.show_brand, name='brand'),
    path('product/<int:id>/<slug:prod_slug>', views.show_product, name='product'),
    path('confirmation/', views.confirmation, name = 'confirmation'),
]



