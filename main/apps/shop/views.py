from django.shortcuts import render

def index(request):
      is_logged_in = False
      if 'uid' in request.session:
            is_logged_in = True
      context = {
            'user_logged_in': is_logged_in
      }
      return render(request, 'homepage.html', context)