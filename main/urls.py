from django.urls import path
from main.views import IndexView, AboutTemplateView, BrandView, ProductDetailView, ConfirmationTemplateView

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('about', AboutTemplateView.as_view(), name='about'),
    path('brand/<slug:brand_slug>/', BrandView.as_view(), name='brand'),
    path('product/<int:id>/<slug:prod_slug>', ProductDetailView.as_view(), name='product'),
    path('confirmation', ConfirmationTemplateView.as_view(), name='confirmation')

]



