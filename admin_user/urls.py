import imp
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('register_admin', views.register_admin, name="register_admin"),
    path('register_hotel', views.register_hotel, name="register_hotel"),
    path('update_hotel', views.update_hotel, name="update_hotel"),
    path('login', views.admin_login, name="login"),
    path('hotel_details/<int:id>', views.hotel_details, name="hotel_details"),
    path('dashboard/update_hotel/<int:id>',
         views.update_hotel, name="update_hotel"),
    path('dashboard/renewal/<int:id>', views.renew, name="renewal"),
    path('dashboard/renewal/renew_hotel',
         views.renew_hotel, name="renew_hotel"),
    path('dashboard/update_hotel_function/<int:id>',
         views.update_hotel_function, name="update_hotel_function"),
    path('dashboard', views.dashboard_admin, name="dashboard_admin"),
    path('manage_property', views.manage_property, name="manage_property"),
    path('dashboard/super_admin_approve/<int:id>',
         views.super_admin_approve, name="super_admin_approve"),
    path('dashboard/manager_list', views.manager_list, name="manager_list"),
    path('dashboard/manager_list/update_manager/<int:id>',
         views.update_manager, name="update_manager"),
    path('dashboard/manager_list/update_admin_function/<int:id>',
         views.update_admin_function, name="update_admin_function"),
    path('logout_view', views.logout_view, name="logout_view"),
    path('admin_profile', views.admin_profile, name="admin_profile"),
    path('manage_property/delete_hotel/<int:id>',
         views.delete_hotel, name="delete_hotel"),
    path('deactivate/<id>', views.deactivate, name="deactivate"),
    path('dashboard/manager_list/delete_admin/<int:id>',
         views.delete_admin, name="delete_admin"),
    path('complaints_admin', views.complaints_admin, name="complaints_admin"),
    path('complaint_status/<int:id>', views.complaint_status, name="complaint_status"),
    path('update_token/<int:id>', views.update_token, name="update_token"),
    #google qr urls
    path('gr_list', views.gr_list, name="gr_list"),
    path('gr_detail/<int:id>', views.gr_detail, name="gr_detail"),
    path('renew_review/<int:id>', views.renew_review, name="renew_review"),
    path('deativate_review/<int:id>', views.deativate_review, name="deativate_review"),
    path('activate_review/<int:id>', views.activate_review, name="activate_review"),
    path('gr_update/<int:id>', views.gr_update, name="gr_update"),
    path('gr_total_reviews', views.gr_total_reviews, name="gr_total_reviews"),
    path('gr_property', views.gr_property, name="gr_property"),
    path('detail_hotel_review/<int:id>', views.detail_hotel_review, name="detail_hotel_review"),
    path('detail_hotel_checkin/<int:id>', views.detail_hotel_checkin, name="detail_hotel_checkin"),
    path('total_review_list', views.total_review_list, name="total_review_list"),
    path('total_checkin_list', views.total_checkin_list, name="total_checkin_list"),
    path('update_products/<int:id>', views.update_products, name="update_products"),



#--------------------- ANWAR --------------

    path('register_restaurant', views.register_restaurant, name="register_restaurant"),
    path('admin_manage_restaurant', views.admin_manage_restaurant, name="admin_manage_restaurant"),
    path('restaurant_approve/<int:id>',views.restaurant_approve, name="restaurant_approve"),
    path('admin_restaurant_home',views.admin_restaurant_home, name="admin_restaurant_home"),
    path('admin_restaurant_fooditemadd',views.admin_restaurant_fooditemadd, name="admin_restaurant_fooditemadd"),
    path('admin_restaurant_fooditemadd_delete/<int:id>',views.admin_restaurant_fooditemadd_delete, name="admin_restaurant_fooditemadd_delete"),







]
