# Generated by Django 4.0.6 on 2022-08-26 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0011_alter_restaurantuser_admin_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='waiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=80, null=True)),
                ('username', models.CharField(max_length=80, null=True)),
                ('password', models.CharField(max_length=80, null=True)),
            ],
        ),
    ]
