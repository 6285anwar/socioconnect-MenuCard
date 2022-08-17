# Generated by Django 4.0.1 on 2022-05-19 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, null=True)),
                ('email', models.EmailField(max_length=60, null=True)),
                ('title_review', models.CharField(max_length=200, null=True)),
                ('review', models.CharField(max_length=200, null=True)),
                ('ratings', models.IntegerField(null=True)),
                ('google', models.BooleanField(default=False, null=True)),
                ('trip_type', models.CharField(choices=[('Business', 'Business'), ('Couples', 'Couples'), ('Family', 'Family'), ('Friends', 'Friends'), ('Solo', 'Solo')], max_length=60, null=True)),
                ('trip', models.BooleanField(default=False, null=True)),
                ('text_review', models.CharField(max_length=200, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=17)),
                ('facebookid', models.CharField(max_length=60, null=True)),
                ('instagramid', models.CharField(max_length=60, null=True)),
                ('url', models.CharField(max_length=200, null=True)),
                ('images', models.ImageField(null=True, upload_to='pics')),
                ('video', models.FileField(null=True, upload_to='vid')),
                ('status', models.BooleanField(default=False, null=True)),
                ('review_method', models.CharField(max_length=50, null=True)),
                ('classic', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Not Sure', 'Not Sure')], max_length=60, null=True)),
                ('mask_required', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Not Sure', 'Not Sure')], max_length=60, null=True)),
                ('health_care_available', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Not Sure', 'Not Sure')], max_length=60, null=True)),
                ('loaundry', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Not Sure', 'Not Sure')], max_length=60, null=True)),
                ('contactless_checkin', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Not Sure', 'Not Sure')], max_length=60, null=True)),
                ('breakfast', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Not Sure', 'Not Sure')], max_length=60, null=True)),
                ('bar_or_lounge', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Not Sure', 'Not Sure')], max_length=60, null=True)),
                ('business', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Not Sure', 'Not Sure')], max_length=60, null=True)),
                ('service', models.CharField(choices=[('Terrible', 'Terrible'), ('Poor', 'Poor'), ('Average', 'Average'), ('Very Good', 'Very Good'), ('Excellent', 'Excellent')], max_length=60, null=True)),
                ('room', models.CharField(choices=[('Terrible', 'Terrible'), ('Poor', 'Poor'), ('Average', 'Average'), ('Very Good', 'Very Good'), ('Excellent', 'Excellent')], max_length=60, null=True)),
                ('clean', models.CharField(choices=[('Terrible', 'Terrible'), ('Poor', 'Poor'), ('Average', 'Average'), ('Very Good', 'Very Good'), ('Excellent', 'Excellent')], max_length=60, null=True)),
                ('expense', models.CharField(choices=[('Budget', 'Budget'), ('Midrange', 'Mid-range'), ('Luxury', 'Luxury')], max_length=60, null=True)),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.hotelusers')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]