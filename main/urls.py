from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('item/', views.item, name='item'),
    path('brand/', views.brand, name='brand'),
    path('main/<int:pk>', views.NewDetailView.as_view(), name='test')
]
