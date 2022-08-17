from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static
from . import views


# router = DefaultRouter()name
# router.register(r'product', ProductViewSet, basename='Product')
# router.register(r'image', ImageViewSet, basename='Image')

urlpatterns = [
    path('', views.index, name="index"),
    path('rate/<str:username>', views.rate, name="rate"),
    path('contact_us', views.contact_us, name="contact_us"),
    path('email_click/<int:id>', views.email_click, name="email_click"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

