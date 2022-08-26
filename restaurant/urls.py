from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('restaurant_index', views.restaurant_index, name="restaurant_index"),
    path('restaurant_dashboard', views.restaurant_dashboard, name="restaurant_dashboard"),
    path('restaurant_menu', views.restaurant_menu, name="restaurant_menu"),
    path('restaurant_waiter', views.restaurant_waiter, name="restaurant_waiter"),
    path('restaurant_addwaiter', views.restaurant_addwaiter, name="restaurant_addwaiter"),



   

]
