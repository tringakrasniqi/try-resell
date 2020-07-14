from django.shortcuts import render, redirect
from .models import Product

def index(request):    
      context = {
            'user_logged_in': False,
            'products' : Product.objects.all()
      }
      if 'uid' in request.session:
            context['user_logged_in'] = True

      return render(request, 'homepage.html', context)


def new_product(request):
      if not 'uid' in request.session: 
            return redirect('/')
      else:
            return render(request, 'new_product.html')

def create_product(request):
      if 'uid' in request.session:
            Product.objects.create(title=request.POST['title'], description=request.POST['description'], price=request.POST['price'], condition=request.POST['condition'])
      return redirect('/')

def show_product(request, product_id):
      context = {
            'product_info' :  Product.objects.get(id=product_id)
      }
      return render(request, 'show_product.html', context)