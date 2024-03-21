from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('',views.home,name= ""),

    # login and register
    path('register',views.register,name="register"),

    path('login',views.user_login, name="login"),

    path('user_logout', views.user_logout, name='user_logout'),

    # CRUD operations

    path('dashboard', views.dashboard, name='dashboard'),

    path('create',views.create_record, name="create"),

    path('update/<int:pk>',views.update_record,name='update'),
    
    path('record/<int:pk>', views.singular_record,name = 'record'),
    path('delete/<int:pk>', views.delete_record, name="delete"),
]
