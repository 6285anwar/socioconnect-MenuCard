from email import message
from inspect import currentframe
from operator import not_
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib import messages
from django.template import context
from django.core.mail import EmailMessage
from django.core import mail
from django.contrib.staticfiles import finders
from email.mime.image import MIMEImage
# from admin_user.models import Complaints
from .models import AdminUsers
from hotel.models import HotelUsers, Complaints
from customer.models import Customer
from restaurant.models import *
import calendar
from django.template.loader import get_template
from django.conf import settings
from datetime import date, timedelta, datetime                         
from django.contrib.auth import get_user_model
  
from django.http.response import HttpResponse
from datetime import date, timedelta, datetime   
from django.utils import timezone

# Create your views here.

# Dashboard of the hotel
def hotel_dashboard(request):
    try:
        current_user = request.user
        current_user.is_hotel
        current_hotel = HotelUsers.objects.get(hotel_user=current_user)
    except:
        messages.info(request,"Please login to your account")
        return redirect('login_view')
    
    if current_user.id != None and current_user.is_hotel == True and current_hotel.status == "Active" and current_hotel.other == True and current_hotel.status == "Active":
        current_hotel = HotelUsers.objects.get(hotel_user=current_user)
        total_ratings = Customer.objects.filter(hotel=current_hotel).order_by('-id')

        month = datetime.now().month
        year = datetime.now().year
        number_of_days = calendar.monthrange(year, month)[1]
        first_date = date(year, month, 1)
        last_date = date(year, month, number_of_days)
        delta = last_date - first_date
        dates = [(first_date + timedelta(days=i)).strftime('%Y-%m-%d')
                 for i in range(delta.days + 1)]

        dates_start = datetime.strptime(
            dates[0] + " 00:00:00", '%Y-%m-%d %H:%M:%S')
        dates_end = datetime.strptime(
            dates[-1] + " 00:00:00", '%Y-%m-%d %H:%M:%S')
        dates_1 = timezone.make_aware(dates_start)
        dates_2 = timezone.make_aware(dates_end)

        thismonth = []
        happy = []
        average = []
        total_upload = []
        for rating in total_ratings:
            # print(type(hotels.start_date))
            if dates_1 <= rating.date and dates_2 >= rating.date:
                thismonth.append(rating)
            if int(rating.ratings) >= 4:
                happy.append(rating)
            if rating.ratings:
                average.append(int(rating.ratings))
            if rating.images or rating.video:
                total_upload.append(rating)
        upload = len(total_upload)
        average_rating = 0
        if average:
            average_rating = round(sum(average)/len(average), 2)
        len_month = len(thismonth)
        total_len = len(total_ratings)
        happy_len = len(happy)
        unhappy = total_len - happy_len
        try:
            happy_per = round((happy_len/total_len)*100, 2)
            not_happy_per = round(100 - happy_per, 2)
        except ZeroDivisionError:
            happy_per = 0
            not_happy_per = 0
        context = {"unhappy": unhappy,"not_happy_per":not_happy_per,"happy_per":happy_per, "upload": upload, "current_hotel": current_hotel, "happy_len": happy_len,
                   "total_ratings": total_ratings, "total_len": total_len, "len_month": len_month, "average_rating": average_rating}
        return render(request, 'hotels/hotel_dashboard.html', context=context)
    else:
        
        return redirect("hotel_login")

# Profile of a hotel user
def hotel_profile(request):
    try:
        current_user = request.user
        current_user.is_hotel
    except:
        messages.info(request,"Please login to your account")
        return redirect('hotel_login')
    if current_user.is_hotel == True:
        hotel = HotelUsers.objects.get(hotel_user=current_user)
        context = {"hotel": hotel}
        return render(request, 'hotels/user_profile_hotel.html', context=context)
    else:
        return redirect("hotel_login")

# Login the hotels dashboard
def hotel_login(request):
    if request.method == 'POST':
        postdata = request.POST.copy()
        username = postdata.get('username', '')
        password = postdata.get('password', '')
        property_code = postdata.get('property_code', '')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_restaurantmenucard == True:

            
                try:
                    rest=RestaurantUser.objects.get(restaurant_user=user)
                    if rest.property_code==property_code and user.is_restaurantmenucard == True and rest.end_date >= timezone.make_aware(datetime.now()):
                        login(request, user)
                        
                        return redirect('restaurant_dashboard')
                except:
                    messages.info(request, "You are not a registerd hotel")
                    return render(request, 'login.html')

            elif user.is_hotel == True:
                try:
                   hotel = HotelUsers.objects.get(hotel_user=user) 

                   if hotel.property_code==property_code and user.is_hotel == True and hotel.other == True and hotel.end_date >= timezone.make_aware(datetime.now()):
                        login(request, user)
                        return redirect('hotel_dashboard')
                    
                   if user.is_hotel == True and hotel.property_code==property_code and hotel.express_checkin == True and hotel.end_date >= timezone.make_aware(datetime.now()):
                        login(request, user)
                        return redirect('dashboard_hotel')
              
                except:
                    messages.info(request, "You are not a registerd hotel")
                    return render(request, 'login.html')


                    

            else:
                messages.info(request, "You are not allowed to login")

        else:
            messages.info(request, "Invalid credentials")
            return render(request, 'login.html')

    return render(request, 'login.html')

# The ratings list
def rating_details(request, id):
    try:
        current_user = request.user
        current_user.is_hotel
    except:
        messages.info(request,"Please login to your account")
        return redirect('hotel_login')

    if current_user.is_hotel == True:
        hotel = HotelUsers.objects.get(hotel_user=current_user)
        ratings = Customer.objects.get(id=id)
        if ratings.hotel == hotel:
            rating = ratings
        return render(request, 'hotels/detailreviewpage.html', {"hotel": hotel, "ratings": rating})
    else:
        return redirect("hotel_login")

# Detailed review page
def detail_review(request):
    try:
        current_user = request.user
        current_user.is_hotel
    except:
        messages.info(request,"Please login to your account")
        return redirect('hotel_login')
    if current_user.is_hotel == True:
        hotel = HotelUsers.objects.get(hotel_user=current_user)
        total_ratings = Customer.objects.filter(hotel=hotel).order_by('-id')
        return render(request, 'hotels/detail_rating.html', {"total_ratings": total_ratings, "hotel":hotel})
    else:
        return redirect("hotel_login")

# Update user profile with details
def update_hotel_profile(request):
    try:
        current_user = request.user
        current_user.is_hotel
    except:
        messages.info(request,"Please login to your account")
        return redirect('hotel_login')

    if current_user.is_hotel == True:
        if request.method == 'POST':
            name = request.POST["username"]
            firstname = request.POST["first_name"]
            lastname = request.POST["last_name"]
            email = request.POST["email"]
            property_name = request.POST["property_name"]
            website = request.POST["website"]
            mobile = request.POST["mobile"]
            location = request.POST["location"]
            # trip = request.POST["trip"]
            # phone = request.POST["phone"]
            # google_link = request.POST["google_link"]

            try:
                profile_photo = request.FILES["profile_photo"]
            except:
                profile_photo = False
            User = get_user_model()

            user = User.objects.filter(id=current_user.id).update(
                username=name, first_name=firstname, last_name=lastname, email=email)
            hotel_user = User.objects.get(id=current_user.id)
            if profile_photo:
                HotelUsers.objects.filter(hotel_user=hotel_user).update(property_name=property_name, website=website,
                                                                        mobile=mobile, location=location, profile_photo=profile_photo)
            else:
                HotelUsers.objects.filter(hotel_user=hotel_user).update(
                    property_name=property_name, website=website, mobile=mobile, location=location)

            return redirect('hotel_dashboard')
    else:
        return redirect("hotel_login")

# Write the complaints or queries
def complaints(request):
    try:
        current_user = request.user
        current_user.is_hotel
    except:
        messages.info(request,"Please login to your account")
        return redirect('hotel_login')

    if current_user.is_hotel == True:
        if request.method == 'POST':
            complaint = request.POST["complaint"]
            hotel = HotelUsers.objects.get(hotel_user=current_user)
            com = Complaints.objects.create(
                complaint=complaint, admin_user=hotel.admin_name, hotel=hotel, status="new")
            return redirect('hotel_dashboard')
    else:
        return redirect("hotel_login")

# Logout the hotel user
def logout_hotel(request):

    logout(request)
    return redirect('/')


# def get_fb_token(request):
#     url = 'https://www.facebook.com/v12.0/dialog/oauth?client_id=3147361772161730&redirect_uri=https://testratingapp.herokuapp.com/hotel/test/&scope=instagram_basic,pages_show_list'
#     payload = {
#         'grant_type': 'client_credentials',
#         'client_id': '3147361772161730',
#         'client_secret': 'ee11d5cd0db75da6c54aa877a4f97089'
#     }
#     response = requests.post(url)
#     return HttpResponse(response.content)

# Update the default 
def update_caption(request):
    try:
        current_user = request.user
        current_user.is_hotel
    except:
        messages.info(request,"Please login to your account")
        return redirect('hotel_login')

    if current_user.is_hotel == True:
        if request.method == 'POST':
            default_caption = request.POST["default_caption"]
            HotelUsers.objects.filter(hotel_user=current_user).update(default_caption=default_caption)
            return redirect('hotel_dashboard')
        return redirect('hotel_dashboard')


# To send bulk emails
def send_emails(request):
    try:
        current_user = request.user
        current_user.is_hotel
    except:
        messages.info(request,"Please login to your account")
        return redirect('hotel_login')
    if current_user.is_hotel == True:
        hotel = HotelUsers.objects.get(hotel_user=current_user)
        customer = Customer.objects.filter(hotel=hotel)
        if request.method == 'POST':
            emails = request.POST["emails"]
            coupon_code = request.POST["coupon_code"]
            offer_caption = request.POST["offer_caption"]
            email_content = request.POST["email_content"]
            extra = request.POST["extra"]
            email_image = request.FILES.get("email_image", False)
# .update(email_image=email_image,extra=extra,offer_caption=offer_caption,coupon_code=coupon_code,email_content=email_content)
            hotel.email_image = email_image
            hotel.offer_caption = offer_caption
            hotel.extra = extra
            hotel.coupon_code = coupon_code
            hotel.email_content = email_content
            hotel.save()
            email_ids = emails.split()
            html_tpl_path = 'email/offer2.html'
            connection = mail.get_connection()
            context_data = {'hotel': hotel,"email_content":email_content,"offer_caption": offer_caption,"coupon_code":coupon_code,"email_content":email_content,"extra":extra}
            email_html_template = get_template(html_tpl_path).render(context_data)

            email_msg = EmailMessage('Thank you for your review',
                                        email_html_template, 
                                        hotel.property_name + "<noreply@hudels.com>",
                                        email_ids,
                                        reply_to=[settings.APPLICATION_EMAIL],
                                        connection=connection
                                        )
            # this is the crucial part that sends email as html content but not as a plain text

            email_msg.content_subtype = 'html'
            with open(finders.find('images/logo.png'), 'rb') as f:
                tick = f.read()
          
            # attch = email_msg.attach(email_image.name, email_image.read(), email_image.content_type)
            
            hotelImage = MIMEImage(email_image.read(), email_image.content_type)
            hotelImage.add_header('Content-ID', '<hotelImage>')
            email_msg.attach(hotelImage)

            tickMime = MIMEImage(tick, 'png')
            tickMime.add_header('Content-ID', '<tickMime>')
            email_msg.attach(tickMime)
            email_msg.send(fail_silently=False)
            return redirect("hotel_dashboard")
        else:
            return render(request, 'hotels/send_emails.html', {"hotel":hotel, "customer":customer})


def restaurant_dashboard(request):
    
        return render(request, 'restaurants/restaurant_dashboard.html')