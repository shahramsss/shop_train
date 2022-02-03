from django.urls import path
from .views import detail ,cart_add , delete_session , cart_remove

app_name = "cart"
urlpatterns = [
    path('cart_detail/', detail, name='cart_detail'),
    path('cart_add/<int:product_id>', cart_add, name='cart_add'),
    path('deletesession/', delete_session, name='deletesession'),
    path('cartremove/<int:product_id>', cart_remove, name='cart_remove'),
  
]
