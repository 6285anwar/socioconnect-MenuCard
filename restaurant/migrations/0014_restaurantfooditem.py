# Generated by Django 4.0.6 on 2022-08-29 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0013_rename_waiter_restaurantwaiter'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantFoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=80, null=True)),
            ],
        ),
    ]
