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
    try:
        current_user = request.user
        current_user.is_restaurantmenucard
        # restaurant=RestaurantUser.objects.get(restaurant_user=current_user)
    except:
        messages.info(request,"Please login to your account")
        return redirect('hotel_login')
    
    if current_user.is_restaurantmenucard == True:
        restaurant=RestaurantUser.objects.get(restaurant_user=current_user)
    return render(request, 'restaurants/restaurant_index.html',{"restaurant":restaurant})

def restaurant_dashboard(request):  
    try:
        current_user = request.user
        current_user.is_restaurantmenucard
        # restaurant=RestaurantUser.objects.get(restaurant_user=current_user)
    except:
        messages.info(request,"Please login to your account")
        return redirect('hotel_login')
    
    if current_user.is_restaurantmenucard == True:
        restaurant=RestaurantUser.objects.get(restaurant_user=current_user)
        
        return render(request, 'restaurants/restaurant_dashboard.html',{"restaurant":restaurant})


def restaurant_menu(request):
    return render(request, 'restaurants/restaurant_menu.html')
def restaurant_waiter(request):
    try:
        current_user = request.user
        current_user.is_restaurantmenucard
        # restaurant=RestaurantUser.objects.get(restaurant_user=current_user)
    except:
        messages.info(request,"Please login to your account")
        return redirect('hotel_login')
    
    if current_user.is_restaurantmenucard == True:
        restaurant=RestaurantUser.objects.get(restaurant_user=current_user)
    return render(request, 'restaurants/restaurant_waiter.html',{"restaurant":restaurant})
def restaurant_addwaiter(request):   
    return render(request,'restaurants/restaurant_addwaiter.html')

def restaurant_profile(request):
    try:
        current_user = request.user
        current_user.is_restaurantmenucard
        # restaurant=RestaurantUser.objects.get(restaurant_user=current_user)
    except:
        messages.info(request,"Please login to your account")
        return redirect('hotel_login')
    
    if current_user.is_restaurantmenucard == True:
        restaurant=RestaurantUser.objects.get(restaurant_user=current_user)   
    return render(request,'restaurants/restaurant_profile.html',{"restaurant":restaurant})

def logout_restaurant(request):

    logout(request)
    return redirect('/')