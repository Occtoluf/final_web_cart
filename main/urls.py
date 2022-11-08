from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    #path('item/', views.item, name='item'),
    #path('brand/', views.brand, name='brand'),
    path('brand/<int:pk>', views.NewDetailView.as_view(), name='brand'),
    path('item/<int:pk>', views.NewDetailView2.as_view(), name='tovar'),
]
