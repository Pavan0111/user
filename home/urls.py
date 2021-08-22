from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post', views.post, name='post'),
    path('product', views.product, name='product'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handlelogin, name='handlelogin'),
    path('logout', views.handlelogout, name='handlelogout')
]
