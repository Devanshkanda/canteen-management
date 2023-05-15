from django.contrib import admin
from django.urls import path
from  .  import views
urlpatterns = [
    path('productView/', views.prodView, name='productView'),
    path('tracker/', views.tracker, name='tracker'),
    path('checkout/',views.checkout,name='checkout'),
]