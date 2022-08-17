from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('restaurant_dashboard', views.restaurant_dashboard, name="restaurant_dashboard"),
   

]
