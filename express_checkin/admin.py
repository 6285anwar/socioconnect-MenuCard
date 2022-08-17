from django.contrib import admin

from express_checkin.models import Checkin, OtherDocuments

# Register your models here.
admin.site.register(Checkin)
admin.site.register(OtherDocuments)