from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('',views.home,name= ""),
    path('register',views.register,name="register"),
    path('login',views.user_login, name="login"),
    
]
