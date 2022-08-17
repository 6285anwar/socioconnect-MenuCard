from django.contrib import admin

from .models import AdminUsers, DeveloperAdmin
# Register your models here.

admin.site.register(AdminUsers)
admin.site.register(DeveloperAdmin)
