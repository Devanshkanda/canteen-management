from django.contrib import admin
from django.urls import path
from Home import views
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
     path('login/', views.Login, name="login"),
    path('signup/',views.SignUp),
    path('logout/',views.handelLogout,name="logout" )
]