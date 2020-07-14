from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new_product', views.new_product),
    path('create_product', views.create_product),
    path('product/<int:product_id>', views.show_product)
]