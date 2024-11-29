from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.sign_up, name='sign_up'),
    path('login/', views.login_user, name='login'),
    path('index/', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
]
