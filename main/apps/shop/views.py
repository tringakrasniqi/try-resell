from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import Product, Category
from apps.authenticate.models import User
from django.db.models import Q
from django.db import models


def index(request):    
      context = {
            'user_logged_in': False,
            
            'categories' : Category.objects.all()
      }
      
      if 'category' in request.session:
            context['products'] = Product.objects.filter(categories__id = request.session['category'])
      else:
            context['products'] = Product.objects.all()

      if 'uid' in request.session:
            context['user_logged_in'] = True
            context['user_data'] = User.objects.get(id=request.session['uid'])

      return render(request, 'homepage.html', context)


def new_product(request):
      if not 'uid' in request.session: 
            return redirect('/')
      else:
            context = {
                  'user_logged_in' : True,
                  'categories': Category.objects.all()
            }
            return render(request, 'new_product.html', context)

def create_product(request):
      if 'uid' in request.session:
            logged_user = User.objects.get(id=request.session['uid'])
            category = Category.objects.get(id=request.POST["category"])
            product = Product.objects.create(title=request.POST['title'], description=request.POST['description'], price=request.POST['price'], condition=request.POST['condition'], creator=logged_user)
            product.categories.add(category)
            if 'product_image' in request.FILES != None:
                  pic = request.FILES['product_image']
                  fs = FileSystemStorage()
                  fs.save(pic.name, pic)
                  product.product_image = pic
                  product.save()
      return redirect('/')

def show_product(request, product_id):
      product = Product.objects.get(id=product_id)
      context = {
            'user_logged_in' : True,
            'product_info' :  product,
            
      }

      category = product.categories.first()
      if category != None:
            filters = models.Q()
            if product:
                  filters &= models.Q(
                        categories__name = category.name,
                  )
            similar_products = Product.objects.filter(filters).exclude(id=product.id)
            context['similar_products'] = similar_products
      return render(request, 'show_product.html', context)

def show_user_profile(request):
      if 'uid' in request.session:
            logged_in_user = User.objects.get(id=request.session['uid'])
            context = {
                  'user_logged_in' : True,
                  'user_data' : logged_in_user,
                  'selling_products': logged_in_user.selling_products.all(),
                  'orders' : logged_in_user.has_orders.all()
            }
            return render(request, 'profile.html', context)
      else:
            return render(request,'index.html')

def delete_product(request, product_id):
      if 'uid' in request.session:
            product = Product.objects.get(id=product_id)
            product.delete()
      return redirect('/profile')

def save_profile_image(request):
      if 'uid' in request.session:
            user = User.objects.get(id = request.session['uid'])
            pic = request.FILES['profile_pic']
            fs = FileSystemStorage()
            fs.save(pic.name, pic)
            user.profile_image = pic
            user.save()
      return redirect('/profile')

def filter_products(request, category_id):
      request.session['category'] = category_id
      return redirect('/')

def remove_filter_products(request):
      if 'category' in request.session:
            del request.session['category'] 
      return redirect('/')