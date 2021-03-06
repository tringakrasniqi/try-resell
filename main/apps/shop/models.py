from django.db import models
from apps.authenticate.models import User

DEFAULT_VALUE = 1

class Category(models.Model):
      name = models.CharField(max_length=100)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
      title = models.CharField(max_length=255)
      description = models.TextField()
      price = models.IntegerField()
      condition = models.IntegerField()
      categories = models.ManyToManyField(Category, related_name="products")
      creator = models.ForeignKey(User, related_name="selling_products", on_delete=models.CASCADE, default=DEFAULT_VALUE)
      product_image = models.ImageField(upload_to='product_image', blank=True)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)


class ProductImage(models.Model):
      product = models.ForeignKey(Product, related_name="product_images", on_delete=models.CASCADE)
      images = models.ImageField(upload_to="product_images", blank=True)
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)