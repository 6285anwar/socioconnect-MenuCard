from django.contrib import admin

# Register your models here.
from .models import Complaints, HotelUsers, Renewals

admin.site.register(HotelUsers)
admin.site.register(Renewals)
admin.site.register(Complaints)
