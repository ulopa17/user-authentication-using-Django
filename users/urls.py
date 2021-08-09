from django.urls import path
from . import views

urlpatterns =[
    path('register/', views.registerUser, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logut/', views.logoutUser, name='logout'),
    path('home', views.homePage, name='home'),
]