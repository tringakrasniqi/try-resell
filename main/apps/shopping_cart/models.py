from django.db import models
from apps.shop.models import Product
from apps.authenticate.models import User

class Order(models.Model):
      owner = models.ForeignKey(User, related_name="has_orders", on_delete=models.SET_NULL, null=True)
      reference_code = models.CharField(max_length=50)
      is_order_complete = models.BooleanField(default=False)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)

      def get_cart_items(self):
            return self.items.all() 

      def get_total_price(self):
            return sum([item.product.price for item in self.order_items.all()])
      

class OrderItem(models.Model):
      product = models.ForeignKey(Product, related_name="in_order", on_delete=models.SET_NULL, null=True)
      order = models.ForeignKey(Order, related_name="order_items", on_delete=models.SET_NULL, null=True)
      quantity = models.IntegerField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)

      def __str__(self):
          return self.product.name
