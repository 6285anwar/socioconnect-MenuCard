from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.deletion import SET_DEFAULT


# Custom User model
class DeveloperAdmin(AbstractUser):
    DEFAULT_PK = 1

    is_admin_user = models.BooleanField(default=False)
    is_super_admin = models.BooleanField(default=False)
    is_hotel = models.BooleanField(default=False)
    is_sales_executives = models.BooleanField(default=False)

    def __str__(self):
        return self.username


# Admin User Model
class AdminUsers(models.Model):
    admin_user = models.OneToOneField(
        DeveloperAdmin, on_delete=SET_DEFAULT, default=DeveloperAdmin.DEFAULT_PK, related_name='admin_user')
    designation = models.CharField(max_length=20, null=True)
    profile_photo = models.ImageField(upload_to="media", null=True)
    mobile = models.CharField(max_length=15, null=True)
    password = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.admin_user.username

    class Meta:
        ordering = ('-id',)
