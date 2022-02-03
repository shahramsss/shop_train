import imp
from statistics import mode, quantiles
from venv import create
from django.db import models
from django.conf import settings
from shop.models import Product


class Order (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE , related_name='orders')
    created = models.DateField(auto_now_add=True)    
    updated = models.DateField(auto_now=True)    
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',) 

    def __str__(self):
        return f'{self.user} - {str(self.id)}'

    def get_total_price(self):
        return sum(item.get_cost() for item in self.items.all())




class OrderItem (models.Model):
    order = models.ForeignKey(Order , on_delete= models.CASCADE, related_name='items')
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='order_items')
    price = models.DecimalField(max_digits=11 , decimal_places=0)
    quantity = models.PositiveSmallIntegerField(default=1)


    def __str__(self):
        return str(self.id)


    def get_cost(self):
        return self.price * self.quantity