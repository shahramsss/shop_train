from django.urls import path
from .views import home , product_detail

app_name = "shop"
urlpatterns = [
    path('home/', home, name='home'),
    path('categoryfilter/<slug:slug>', home, name='category_filter'),
    path('productdetail/<slug:slug>/',product_detail, name='productdetail') ,
]
