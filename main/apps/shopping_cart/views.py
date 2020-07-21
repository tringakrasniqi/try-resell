from django.shortcuts import render, redirect
from .models import Order, OrderItem 
from apps.authenticate.models import User
from apps.shop.models import Product
import uuid

def index(request):
      context = {
            'user_logged_in' : False
      }
      if 'uid' in request.session:
            context['user_logged_in'] = True
            user = User.objects.get(id=request.session['uid'])
            orders = Order.objects.filter(owner=user)
            incomplete_orders = orders.exclude(is_order_complete=True)
            if incomplete_orders:
                  context['order'] = incomplete_orders.first()
            else: 
                  context['message'] = "Continue Shopping"
      return render(request, 'order.html', context)

def add_to_cart(request, product_id):
      if 'uid' in request.session:
            user = User.objects.get(id=request.session['uid'])
            product = Product.objects.get(id=product_id)
            order, status = Order.objects.get_or_create(owner=user, is_order_complete=False)
            OrderItem.objects.get_or_create(order=order, product=product, quantity=1)

            if status:
                  order.reference_code = uuid.uuid1()
                  order.save()
      return redirect('/')

def delete_order_item(request, order_item_id):
      if 'uid' in request.session:
            order = Order.objects.get(owner__id = request.session['uid'])
            order_item = OrderItem.objects.get(id = order_item_id)
            order.order_items.remove(order_item)
      return redirect('/shopping')

def complete_order(request, order_id):
      if 'uid' in request.session:
            order = Order.objects.get(id=order_id)
            if order.order_items.count != None:
                  order.is_order_complete = True
                  order.save()
                  return redirect('/shopping/checkout')
            else: 
                  return redirect('/shopping')

def checkout_order(request):
      context = {
            'user_logged_in' : False
      }
      if 'uid' in request.session:
            context['user_logged_in'] = True
      return render(request, 'order_complete.html', context)
