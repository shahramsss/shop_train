from itertools import product
from math import prod
from statistics import quantiles
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from cart.cart import Cart


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order.html', {'order': order})


@login_required
def order_create(request):
    cart = Cart(request)
    order = Order.objects.create(user=request.user)
    for item in cart:
        OrderItem.objects.create(order=order ,product = item['product'], price = item['price'], quantity=item['quantity'],)
    cart.clear()
    return redirect('orders:order_detail', order.id)
