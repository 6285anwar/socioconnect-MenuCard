"""socioconnects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_user/', include('admin_user.urls')),
    path('hotel/', include('hotel.urls')),
    path('checkin/', include('express_checkin.urls')),
    path('', include('customer.urls')),
    # path('sales_executive/', include('sales_executive.urls')),
]

handler404 = 'socioconnects.views.handler404'
handler500 = 'socioconnects.views.handler500'
handler403 = 'socioconnects.views.handler403'