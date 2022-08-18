from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from restaurant.models import RestaurantUser
from django.contrib import messages
from django.conf import settings
from datetime import date, timedelta, datetime   
from django.utils import timezone

# Create your views here.


def restaurant_dashboard(request):
    return render(request, 'restaurants/restaurant_dashboard.html')