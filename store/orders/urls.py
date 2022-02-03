from django.urls import path
from .views import order_detail , order_create

app_name = "orders"
urlpatterns = [
    path('orderdetail/<int:order_id>', order_detail, name='order_detail'),
    path('ordercreate/', order_create, name='order_create'),
  
]
