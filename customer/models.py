from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from hotel.models import HotelUsers
from io import BytesIO  #basic input/output operation
from PIL import Image #Imported to compress images
from django.core.files import File #to store files
from django.utils.translation import gettext_lazy as _


TripType = (
    ("Business", "Business"),
    ("Couples", "Couples"),
    ("Family", "Family"),
    ("Friends", "Friends"),
    ("Solo", "Solo"),
)
yes_or_no = (
    ("Yes", "Yes"),
    ("No", "No"),
    ("Not Sure", "Not Sure"),
)
expenses = (
    ("Budget", "Budget"),
    ("Midrange", "Mid-range"),
    ("Luxury", "Luxury"),
)
reviews = (
    ("1", "Terrible"),
    ("2", "Poor"),
    ("3", "Average"),
    ("4", "Very Good"),
    ("5", "Excellent"),
)


# Review/Rating Model
class Customer(models.Model):

    name = models.CharField(max_length=60, null=True)
    email = models.EmailField(max_length=60, null=True)
    hotel = models.ForeignKey(HotelUsers, on_delete=CASCADE, null=True)
    title_review = models.CharField(null=True, max_length=200)
    review = models.CharField(null=True, max_length=200)
    ratings = models.IntegerField(null=True)
    google = models.BooleanField(default=False, null=True)
    trip_type = models.CharField(max_length=60, null=True,choices=TripType)
    trip = models.BooleanField(default=False, null=True)
    text_review = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    phone_number = models.CharField(max_length=17, blank=True)
    facebookid = models.CharField(max_length=60, null=True)
    instagramid = models.CharField(max_length=60, null=True)
    url = models.CharField(max_length=200, null=True)
    images = models.ImageField(
        upload_to="pics", null=True)
    video = models.FileField(upload_to="vid", null=True)
    status = models.BooleanField(null=True,default=False)
    review_method = models.CharField(null=True, max_length=50)
    #new
    classic = models.CharField(max_length=60, null=True,choices=yes_or_no)
    mask_required = models.CharField(max_length=60, null=True,choices=yes_or_no)
    health_care_available = models.CharField(max_length=60, null=True,choices=yes_or_no)
    loaundry = models.CharField(max_length=60, null=True,choices=yes_or_no)
    contactless_checkin = models.CharField(max_length=60, null=True,choices=yes_or_no)
    breakfast = models.CharField(max_length=60, null=True,choices=yes_or_no)
    bar_or_lounge = models.CharField(max_length=60, null=True,choices=yes_or_no)
    business = models.CharField(max_length=60, null=True,choices=yes_or_no)
    service = models.CharField(max_length=60, null=True,choices=reviews)
    room = models.CharField(max_length=60, null=True,choices=reviews)
    clean = models.CharField(max_length=60, null=True,choices=reviews)
    expense = models.CharField(max_length=60, null=True,choices=expenses)


    class Meta:
        ordering = ('-id',)
    # def __str__(self):
    #     return self.name
