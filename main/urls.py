from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('brand/<int:brand_id>/', views.show_brand, name='brand'),
    path('product/<int:prod_id>', views.show_product, name='product'),
]

    #path('item/', views.item, name='item'),
    #path('brand/', views.brand, name='brand'),
    #path('brand/<int:pk>/', views.NewDetailView.as_view(), name='brand'),
    #path('item/<int:pk>/', views.NewDetailView2.as_view(), name='tovar'),

