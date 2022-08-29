from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from restaurant.models import RestaurantUser
from django.contrib import messages
from django.conf import settings
from datetime import date, timedelta, datetime   
from django.utils import timezone

from restaurant.models import *
# Create your views here.

def restaurant_index(request):  
    try:
        current_user = request.user
        current_user.is_restaurantmenucard
    except:
        messages.info(request,"Please login to your account")
        return redirect('hotel_login')
    
    if current_user.is_restaurantmenucard == True:
        restaurant=RestaurantUser.objects.get(restaurant_user=current_user)
    return render(request, 'restaurants/restaurant_index.html',{"restaurant":restaurant})

def logout_restaurant(request):

    logout(request)
    return redirect('/')

def restaurant_dashboard(request):  
    try:
        current_user = request.user
        current_user.is_restaurantmenucard
    except:
        messages.info(request,"Please login to your account")
        return redirect('hotel_login')
    
    if current_user.is_restaurantmenucard == True:
        restaurant=RestaurantUser.objects.get(restaurant_user=current_user)
        
        return render(request, 'restaurants/restaurant_dashboard.html',{"restaurant":restaurant})

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

        waiter=Restaurantwaiter.objects.filter(restaurant_id=restaurant)

        context={"restaurant":restaurant,"waiter":waiter}

    return render(request, 'restaurants/restaurant_waiter.html',context=context)


def restaurant_addwaiter(request):   
    try:
        current_user = request.user
        current_user.is_restaurantmenucard
        # restaurant=RestaurantUser.objects.get(restaurant_user=current_user)
    except:
        messages.info(request,"Please login to your account")
        return redirect('hotel_login')
    
    if current_user.is_restaurantmenucard == True:
            restaurant=RestaurantUser.objects.get(restaurant_user=current_user)
    
    if request.method == 'POST':
        r_fullname = request.POST["fullname"]
        
        restwaiter=Restaurantwaiter(fullname=r_fullname)
        restwaiter.save()
        restwaiter.username="W"+str(restwaiter.id)+current_user.username+"-"+r_fullname
        restwaiter.save()
        restwaiter.password=r_fullname+"@"+"W"+str(restwaiter.id)
        restwaiter.save()

        if current_user.is_restaurantmenucard == True:
            restaurantuser=RestaurantUser.objects.get(restaurant_user=current_user)
            rest=RestaurantUser.objects.get(id=restaurantuser.id)  
            
            restwaiter.restaurant=(rest)
            restwaiter.save()

        return redirect('restaurant_waiter')

    return render(request,'restaurants/restaurant_addwaiter.html',{'restaurant':restaurant})


def restaurant_deletewaiter(request,id):   
    try:
        current_user = request.user
        current_user.is_restaurantmenucard
       
    except:
        messages.info(request,"Please login to your account")
        return redirect('hotel_login')
    
    waiter=Restaurantwaiter.objects.get(id=id)
    waiter.delete()

    return redirect('restaurant_waiter')



def restaurant_menu(request):
    try:
        current_user = request.user
        current_user.is_restaurantmenucard
       
    except:
        messages.info(request,"Please login to your account")
        return redirect('hotel_login')
    
    if current_user.is_restaurantmenucard == True:
        restaurant=RestaurantUser.objects.get(restaurant_user=current_user)


        context={"restaurant":restaurant}
    return render(request, 'restaurants/restaurant_menu.html',context=context)


def restaurant_add_menu(request):
    try:
        current_user = request.user
        current_user.is_restaurantmenucard
       
    except:
        messages.info(request,"Please login to your account")
        return redirect('hotel_login')
    
    if current_user.is_restaurantmenucard == True:
        restaurant=RestaurantUser.objects.get(restaurant_user=current_user) 
        item=RestaurantFoodItem.objects.all()


    return render(request, 'restaurants/restaurant_add_menu.html',{"item":item,"restaurant":restaurant})

def restaurant_add_foodmenu(request):
    try:
        current_user = request.user
        current_user.is_restaurantmenucard
       
    except:
        messages.info(request,"Please login to your account")
        return redirect('hotel_login')

    if request.method == 'POST':
        r_fooditem = request.POST["fooditem"]
        r_foodname = request.POST["foodname"]
        r_foodprice = request.POST["foodprice"]

        menu = RestaurantFoodmenu(foodname=r_foodname)
        menu.save()

        price=r_foodprice+".00"
        menu.price=price
        menu.save()

        item = RestaurantFoodItem.objects.get(id=r_fooditem)

        menu.fooditem=(item)
        menu.save()

        if current_user.is_restaurantmenucard == True:
            restaurantuser=RestaurantUser.objects.get(restaurant_user=current_user)
            rest=RestaurantUser.objects.get(id=restaurantuser.id)  
            
            menu.restaurant=(rest)
            menu.save()

        return redirect('restaurant_menu')