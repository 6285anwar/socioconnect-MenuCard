# Generated by Django 4.0.6 on 2022-08-17 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='developeradmin',
            name='is_restaurantmenucard',
            field=models.BooleanField(default=False),
        ),
    ]
