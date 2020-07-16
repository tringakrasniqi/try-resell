from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('product/new', views.new_product),
    path('product/create', views.create_product),
    path('product/<int:product_id>', views.show_product),
    path('product/<int:product_id>/delete', views.delete_product),
    path('product/filter/<int:category_id>', views.filter_products),
    path('product/filter/remove', views.remove_filter_products),
    path('profile', views.show_user_profile),
    path('profile/image', views.save_profile_image)
]