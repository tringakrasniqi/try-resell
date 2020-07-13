from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
      # if 'uid' in request.session:
      #       return redirect('/shop')
      # else:
      return render(request, 'index.html')

def login(request):
      errors = User.objects.login_validator(request.POST)
      
      if len(errors) > 0:
            for key, value in errors.items():
                  messages.error(request, value)
            return redirect('/authenticate/')
      else:
            user = User.objects.filter(email=request.POST['email'])
            request.session['uid'] = user[0].id 
            return redirect('/')

def register(request):
      errors = User.objects.register_validator(request.POST)

      if len(errors) > 0:
            for key, value in errors.items():
                  messages.error(request, value)
            return redirect('/authenticate')
      else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], alias=request.POST['alias'], email=request.POST['email'], password=pw_hash)
            request.session['uid'] = user.id
            return redirect('/')
      
def logout(request):
      request.session.flush()
      return redirect('/')
