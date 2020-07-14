from django.db import models

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
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)