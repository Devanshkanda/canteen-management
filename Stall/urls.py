from django.contrib import admin
from django.urls import path
from  .  import views
urlpatterns = [
    path('', views.Stalls, name='Stalls'),
    path('Menu/', views.Menu, name='Menu'),
    path('tracker/', views.tracker, name='tracker'),
    path('checkout/',views.checkout,name='checkout'),
]