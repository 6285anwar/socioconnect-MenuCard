from email.policy import default
from django.db import models

from django.db.models.deletion import CASCADE, SET_NULL, SET_DEFAULT

from admin_user.models import AdminUsers
from admin_user.models import DeveloperAdmin

# Create your models here.

TYPES = (
    ("restaurant", "Restaurant"),
    ("hotel", "Hotel"),
    ("resort", "Resort"),
    ("lodge", "Lodge"),
    ("service", "Service Apartment"),
    ("home_stay", "Home stay"),
    ("house_boat", "House Boat"),
)

PackageType = (
    ("standered", "Standered"),
    ("premium", "Premium"),
    ("ultimate", "Ultimate"),
)

ActiveStatus = (
    ("Active", "Active"),
    ("Inactive", "Inactive"),
    ("Waiting", "Waiting for Approval"),
    ("Deactivate", "Deactivate"),
)

# BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

#Property Model
class HotelUsers(models.Model):
    hotel_user = models.OneToOneField(
        DeveloperAdmin, related_name='hotel_user', on_delete=CASCADE)
    property_name = models.CharField(max_length=80)
    password = models.CharField(max_length=20)
    with_filter = models.BooleanField(default=False, null=True)
    without_email = models.BooleanField(default=False, null=True)
    without_filter = models.BooleanField(default=False, null=True)
    without_backend = models.BooleanField(default=False, null=True)
    profile_photo = models.ImageField(
        upload_to='media', height_field=None, width_field=None, max_length=100)
    property_code = models.CharField(max_length=20, unique=True)
    default_caption = models.CharField(max_length=300, null=True)
    amount = models.FloatField(null=True)
    tax = models.FloatField(null=True)
    url_checkin = models.CharField(max_length=200,null=True)
    total = models.FloatField(null=True)
    url = models.CharField(null=True, max_length=100)
    mobile = models.CharField(max_length=50, null=True)
    admin_name = models.ForeignKey(AdminUsers, on_delete=SET_NULL, null=True)
    designation = models.CharField(null=True, max_length=100)
    checkin_qr = models.ImageField(upload_to="qr", null=True)
    property_images = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    type_of = models.CharField(max_length=10, choices=TYPES, default='hotel')
    start_date = models.DateTimeField(auto_now_add=True, blank=True)
    duration = models.FloatField(max_length=10)
    end_date = models.DateTimeField(blank=True, null=True)
    insta_id = models.CharField(max_length=200)
    page_id = models.CharField(max_length=200, null=True)
    google_link = models.CharField(max_length=200)
    website = models.URLField(max_length=200)
    location = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=200)
    twitter_id = models.CharField(max_length=50, null=True)
    agreement = models.FileField(upload_to="media", null=True)
    whatsapp = models.BooleanField(default=False, null=True)
    text_sms = models.BooleanField(default=False, null=True)
    trip_adviser_link = models.CharField(max_length=200, null=True)
    facebook_access_token = models.CharField(max_length=200, null=True)
    status = models.CharField(choices=ActiveStatus, max_length=60, null=True)
    qr_code = models.ImageField(upload_to="qr", null=True)
    google = models.BooleanField(default=False)
    trip_adviser = models.BooleanField(default=False)
    social_media = models.BooleanField(default=False)
    other = models.BooleanField(default=False)
    express_checkin = models.BooleanField(default=False)
    g_t = models.BooleanField(default=False)
    inhouse = models.BooleanField(default=False)
    t_g = models.BooleanField(default=False)
    access_token_end_date = models.DateField(null=True)
    #new
    email_content = models.CharField(max_length=500, null=True)
    email_image = models.ImageField(null=True, upload_to="email")
    offer_caption = models.CharField(max_length=100, null=True)
    coupon_code = models.CharField(max_length=30, null=True)
    extra = models.CharField(max_length=100, null=True)
    
    class Meta:
        ordering = ('-id',)

#Renewals Model
class Renewals(models.Model):
    hotel = models.ForeignKey(HotelUsers, on_delete=CASCADE)
    renew_date = models.DateTimeField()
    google = models.BooleanField(default=False)
    trip_adviser = models.BooleanField(default=False)
    in_house = models.BooleanField(default=False)
    social_media = models.BooleanField(default=False)
    express_checkin = models.BooleanField(default=False)
    g_t = models.BooleanField(default=False)
    t_g = models.BooleanField(default=False)
    agreement = models.FileField(upload_to="media", null=True)
    duration = models.IntegerField()
    amount = models.FloatField(null=True, default=0)

    class Meta:
        ordering = ('-id',)
    
    def __str__(self):
        return self.hotel.hotel_user.username


Status = (
    ("new", "New"),
    ("working", "Working"),
    ("solved", "Solved"),
)

# Complaints model (Not using)
class Complaints(models.Model):
    admin_user = models.ForeignKey(
        AdminUsers, on_delete=SET_DEFAULT, default=DeveloperAdmin.DEFAULT_PK)
    complaint = models.CharField(max_length=200)
    current_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=Status, max_length=100)
    hotel = models.ForeignKey(HotelUsers, on_delete=CASCADE)

    class Meta:
        ordering = ('-id',)
