from django.db import models
from admin_user.models import AdminUsers
from admin_user.models import DeveloperAdmin

from django.db.models.deletion import CASCADE, SET_NULL, SET_DEFAULT

TYPES = (
    ("restaurant", "Restaurant"),
    ("hotel", "Hotel"),
    ("coffeeshop", "CoffeeShop"),
    
)
ActiveStatus = (
    ("Active", "Active"),
    ("Inactive", "Inactive"),
    ("Waiting", "Waiting for Approval"),
    ("Deactivate", "Deactivate"),
)


# Restaurant Model
class RestaurantUser(models.Model):
    restaurant_user = models.OneToOneField(
        DeveloperAdmin, related_name='restaurant_user', on_delete=CASCADE, null=True)
    property_code = models.CharField(max_length=20)
    restaurant_name = models.CharField(max_length=80)
   
    username = models.CharField(max_length=80,  null=True)

    owner_name = models.CharField(max_length=80)
    type_of = models.CharField(max_length=10, choices=TYPES, default='restaurant')
    password = models.CharField(max_length=20)
    user_email = models.CharField(max_length=500, null=True)
    user_mobile = models.CharField(max_length=15, null=True)
    profile_photo = models.ImageField(upload_to='media', height_field=None, width_field=None, max_length=100) 
    #Addressdetails
    address = models.CharField(max_length=200)
    location = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    admin_name = models.ForeignKey(AdminUsers, on_delete=SET_NULL, null=True)
    #table count
    tablecount = models.CharField(max_length=15, null=True)
    #payment
    amount = models.FloatField(null=True)
    tax = models.FloatField(null=True)
    total = models.FloatField(null=True)
    #Date
    start_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    duration = models.FloatField(max_length=10)
    end_date = models.DateTimeField(blank=True, null=True)
    website = models.CharField(max_length=50, null=True)


    agreement = models.FileField(upload_to="media", null=True)
    status = models.CharField(choices=ActiveStatus, max_length=60, null=True)

    class Meta:
        ordering = ('-id',)

class tableqrcodes(models.Model):

    tableqr = models.FileField(upload_to='document',null=True)
    restaurantname = models.ForeignKey(RestaurantUser, on_delete=models.CASCADE)

class Restaurantwaiter(models.Model):
    fullname = models.CharField(max_length=80, null=True)
    username = models.CharField(max_length=80, null=True)
    password = models.CharField(max_length=80, null=True)


