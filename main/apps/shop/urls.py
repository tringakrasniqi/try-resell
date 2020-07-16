from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('product/new', views.new_product),
    path('product/create', views.create_product),
    path('product/<int:product_id>', views.show_product),
    path('product/<int:product_id>/delete', views.delete_product),
    path('profile', views.show_user_profile),
]