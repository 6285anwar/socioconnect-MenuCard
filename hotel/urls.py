from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('dashboard', views.hotel_dashboard, name="hotel_dashboard"),
    path('login', views.hotel_login, name="hotel_login"),
    path('user_profile', views.hotel_profile, name="user_profile_hotel"),
    path('detail_review', views.detail_review, name="detail_review"),
    path('update_hotel_profile', views.update_hotel_profile,
         name="update_hotel_profile"),
    path('complaints', views.complaints, name="complaints"),
    path('rating_details/<int:id>', views.rating_details, name="rating_details"),
    path('logout', views.logout_hotel, name="logout_hotel"),
    path('update_caption', views.update_caption, name="update_caption"),
    path('send_emails', views.send_emails, name="send_emails"),

    path('restaurant_dashboard', views.restaurant_dashboard, name="restaurant_dashboard"),

]
