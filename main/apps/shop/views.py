from django.shortcuts import render, redirect
from .models import Product
from apps.authenticate.models import User

def index(request):    
      context = {
            'user_logged_in': False,
            'products' : Product.objects.all()
      }
      if 'uid' in request.session:
            context['user_logged_in'] = True
            context['user_data'] = User.objects.get(id=request.session['uid'])

      return render(request, 'homepage.html', context)


def new_product(request):
      if not 'uid' in request.session: 
            return redirect('/')
      else:
            context = {
                  'user_logged_in' : True
            }
            return render(request, 'new_product.html', context)

def create_product(request):
      if 'uid' in request.session:
            logged_user = User.objects.get(id=request.session['uid'])
            Product.objects.create(title=request.POST['title'], description=request.POST['description'], price=request.POST['price'], condition=request.POST['condition'], creator=logged_user)
      return redirect('/')

def show_product(request, product_id):
      context = {
            'user_logged_in' : True,
            'product_info' :  Product.objects.get(id=product_id)
      }
      return render(request, 'show_product.html', context)

def show_user_profile(request):
      if 'uid' in request.session:
            logged_in_user = User.objects.get(id=request.session['uid'])
            context = {
                  'user_logged_in' : True,
                  'user_data' : logged_in_user,
                  'selling_products': logged_in_user.selling_products.all()
            }
            return render(request, 'profile.html', context)
      else:
            return render(request,'index.html')
