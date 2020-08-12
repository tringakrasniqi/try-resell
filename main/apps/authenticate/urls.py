from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('register/new', views.go_to_register),
    path('login', views.login),
    path('logout', views.logout), 
    path('account/delete', views.delete_user)
]
