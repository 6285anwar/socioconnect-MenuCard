# Generated by Django 4.0.6 on 2022-08-18 05:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0009_restaurantuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantuser',
            name='restaurant_user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_user', to=settings.AUTH_USER_MODEL),
        ),
    ]