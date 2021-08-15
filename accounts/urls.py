
from . import views
from django.contrib.auth import views as auth_views 


from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [
    path('register', Register_View.as_view(), name='register_url'),
    path('login', Login_View.as_view(), name='login_url'),
    path('logout', Logout_View.as_view(), name='logout_url'),


  



]