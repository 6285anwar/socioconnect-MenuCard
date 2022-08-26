from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from restaurant.models import RestaurantUser
from django.contrib import messages
from django.conf import settings
from datetime import date, timedelta, datetime   
from django.utils import timezone

from restaurant.models import RestaurantUser, tableqrcodes, Restaurantwaiter

# Create your views here.

def restaurant_index(request):  
    return render(request, 'restaurants/restaurant_index.html')
def restaurant_dashboard(request):  
    return render(request, 'restaurants/restaurant_dashboard.html')
def restaurant_menu(request):
    return render(request, 'restaurants/restaurant_menu.html')
def restaurant_waiter(request):
    return render(request, 'restaurants/restaurant_waiter.html')
def restaurant_addwaiter(request):
    
    return render(request,'restaurants/restaurant_addwaiter.html')