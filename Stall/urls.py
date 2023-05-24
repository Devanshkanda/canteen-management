from django.contrib import admin
from django.urls import path
from  .  import views
urlpatterns = [
    path('stall/', views.Stalls, name='Stalls'),
    path('menu/<slug:url>', views.Menu, name='Menu'),
    path('updateItem/', views.updateItem, name='updateItem'),
    path('cart/',views.cart,name='cart'),
]