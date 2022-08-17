from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
   path('', views.index, name="index"),
   path('success',views.success, name="success"),
   path('total_checkin',views.total_checkin, name="total_checkin"),
   path('checkin/<str:username>', views.checkin, name="checkin"),
   path('check_mobile/<str:username>', views.check_mobile, name="check_mobile"),
   path('user_profile', views.user_profile, name="user_profile"),
   path('dashboard', views.dashboard_hotel,name="dashboard_hotel"),
   path('login', views.login_view, name="login_view"),
   path('approve/<int:id>', views.approve, name="approve"),
   path('edit_customer/<int:id>', views.edit_customer, name="edit_customer"),
   path('edit_fun/<int:id>', views.edit_fun, name="edit_fun"),
   path('reject/<int:id>', views.reject, name="reject"),
   path('detailed_view/<int:id>', views.detailed_view,name="detailed_view"),
   path('logout', views.logout_hotel,name="logout_hotel"),
   path('print_customer/<int:id>', views.print_customer,name="print_customer"),
   path('update_hotel_profile_express', views.update_hotel_profile_express, name="update_hotel_profile_express"),
   #end user review template
   path('googlerating/<int:id>', views.googlerating, name="googlerating"),
   path('other_documents/<int:id>', views.other_documents, name="other_documents")
]