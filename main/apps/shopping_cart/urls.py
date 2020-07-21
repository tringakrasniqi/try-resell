from django.urls import path
from . import views

urlpatterns = [
       path('', views.index),
       path('add/<int:product_id>', views.add_to_cart),
       path('delete/<int:order_item_id>', views.delete_order_item),
       path('checkout/<int:order_id>', views.complete_order),
       path('checkout', views.checkout_order)
]