import re
from django.contrib.auth import get_user_model
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from dateutil.relativedelta import relativedelta
import admin_user
from dateutil import tz

from restaurant.models import RestaurantUser, tableqrcodes
from .models import AdminUsers, DeveloperAdmin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from hotel.models import Complaints, HotelUsers, Renewals, Status
from customer.models import Customer
import calendar
from django.template.loader import get_template
from datetime import date, timedelta, datetime
from django.utils import timezone
from django.conf import settings
from email.mime.image import MIMEImage
from django.contrib.staticfiles import finders
from django.core.mail import EmailMessage
# google review imports
from express_checkin.models import Checkin, GoogleQr, Ratings
from django.core.files.base import ContentFile
from io import BytesIO
import segno
from django.contrib.auth.decorators import login_required
from django.db.models import Sum


# Create your views here.

#For creating a Sales Executive or Manager from the form
#
def register_admin(request):
    try:
        current_user = request.user
        current_user.is_admin_user
    except:
        messages.info(request,"Please login to your account")
        return redirect('login')

    if current_user.is_super_admin == True:

        current_user = request.user
        admins = AdminUsers.objects.get(admin_user=current_user)
        if request.method == 'POST':
            name = request.POST["username"]
            firstname = request.POST["firstname"]
            lastname = request.POST["lastname"]
            email = request.POST["email"]
            psw = request.POST["password"]
            repeat_password = request.POST["confirm_password"]
            designation = request.POST["designation"]
            try:
                profile_photo = request.FILES["profile_photo"]
            except:
                profile_photo = False

            User = get_user_model()
            use = User.objects.filter(username=name)
            if use:
                use.username = "not"
                messages.error(request, "Username Taken")

            else:
                if psw == repeat_password:
                    user = User.objects.create_user(
                        username=name, email=email, password=psw, first_name=firstname, last_name=lastname)
                    user.is_admin_user = True
                    user.save()
                    admin_user_object = AdminUsers.objects.create(
                        admin_user=user, designation=designation, password=psw, profile_photo=profile_photo)
            return redirect('dashboard_admin')
        return render(request, 'admin_user/admin-add-user.html', {"profile_pic":admins.profile_photo})
    else:
        return redirect('login')

#For Creating a property from the form

def register_hotel(request):
    try:
        current_user = request.user
        current_user.is_admin_user
        admins = AdminUsers.objects.get(admin_user=current_user)
    except:
        messages.info(request,"Please login to your account")
        return redirect('login')
    admin_users = AdminUsers.objects.all()
    if current_user.is_super_admin == True or current_user.is_admin_user == True:
        if request.method == 'POST':
            name = request.POST["username"]
            firstname = request.POST["firstname"]
            email = request.POST["email"]
            country = request.POST["country"]
            facebook_access_token = request.POST["facebook_access_token"]
            insta_id = request.POST["insta_id"]
            page_id = request.POST["page_id"]
            psw = request.POST["password"]
            repeat_password = request.POST["confirm_password"]
            property_name = request.POST["property_name"]
            amount = request.POST["amount"]
            without_filter = request.POST.get("without_filter", False)
            tax = request.POST["tax"]
            type_of = request.POST["type_of"]
            duration = request.POST["duration"]
            url = request.POST["url"]
            mobile = request.POST["mobile"]
            total = request.POST["total"]
            google_link = request.POST["google_link"]
            website = request.POST["website"]
            address = request.POST["address"]
            state = request.POST["state"]
            checkin_qr = request.FILES.get("checkin_qr",  False)
            admin_user_name = request.POST["admin_user"]
            location = request.POST["location"]
            trip_adviser_link = request.POST["trip_adviser_link"]

            google = request.POST.get("google", False)
            inhouse = request.POST.get("inhouse", False)
            trip_adviser = request.POST.get("trip_adviser",  False)
            whatsappin = request.POST.get("whatsappin", False)

            social_media = request.POST.get("social_media", False)
            backend = request.POST.get("backend", False)
            g_t = request.POST.get("g_t", False)
            t_g = request.POST.get("t_g", False)
            express_checkin = request.POST.get("express_checkin", False)

            qr_code = request.FILES.get("qr", False)

            # package_type = request.POST["package_type"]
            profile_photo = request.FILES.get("profile_photo", False)
            agreement = request.FILES.get("agreement", False)

            # print([t_g, g_t, google, trip_adviser, social_media])
            User = get_user_model()
            use = User.objects.filter(username=name)
            user_d = User.objects.get(username=str(admin_user_name))
            ad_user = AdminUsers.objects.get(admin_user=user_d)
            if use:

                messages.error(request, "Username Taken")

            else:
                field_name = 'admin_user__username__icontains'
                admin_user_object = AdminUsers.objects.get(
                    admin_user=current_user)
                if psw == repeat_password:
                    user = User.objects.create_user(
                        username=name, email=email, password=psw, first_name=firstname)
                    user.is_hotel = True
                    user.save()
                    hotel_user_object = HotelUsers.objects.create(hotel_user=user,
                                                                  without_filter=without_filter,
                                                                  page_id=page_id,
                                                                  whatsapp=whatsappin,
                                                                  inhouse=inhouse,
                                                                  insta_id=insta_id,
                                                                  facebook_access_token=facebook_access_token,
                                                                  property_name=property_name,
                                                                  profile_photo=profile_photo,
                                                                  google=google,
                                                                  location=location,
                                                                  state=state,
                                                                  country=country,
                                                                  url=url,
                                                                  without_backend=backend,
                                                                  checkin_qr=checkin_qr,
                                                                  total=total,
                                                                  password=psw,
                                                                  mobile=mobile,
                                                                  tax=tax,
                                                                  trip_adviser=trip_adviser,
                                                                  social_media=social_media,
                                                                  g_t=g_t,
                                                                  t_g=t_g,
                                                                  admin_name=ad_user,
                                                                  type_of=type_of,
                                                                  duration=duration,
                                                                  qr_code=qr_code,
                                                                  amount=amount,
                                                                  google_link=google_link,
                                                                  website=website,
                                                                  address=address,
                                                                  agreement=agreement,
                                                                  express_checkin=express_checkin,
                                                                  trip_adviser_link=trip_adviser_link,
                                                                  # facebook_access_token=facebook_access_token,
                                                                  status="Waiting"
                                                                  )
                    if inhouse == "True" or google == "True" or trip_adviser == "True" or t_g == "True" or g_t == "True" or social_media == "True":
                        hotel_user_object.other = True
                        # print("working")
                        hotel_user_object.save()
                    else:
                        hotel_user_object.other = False
                        # print("not working")

                        hotel_user_object.save()
                    hotel_user_object.access_token_end_date = date.today() + relativedelta(days=+27)
                    if duration == "7":
                        end_date = datetime.today() + relativedelta(days=+int(duration))
                    else:
                        end_date = datetime.today() + relativedelta(months=+int(duration))
                    hotel_user_object.end_date = timezone.make_aware(end_date)
                    hotel_user_object.property_code = "SC" + \
                        str(hotel_user_object.id).zfill(5)
                    hotel_user_object.save()

                    # start_date = hotel_user_object.start_date
                    # Renewals.objects.create(hotel=hotel_user_object, renew_date = start_date,package_type = package_type, agreement = agreement,duration = duration )
                    return redirect("dashboard_admin")
                else:
                    return HttpResponse("Password not matching")

        return render(request, 'admin_user/admin-register-property.html', {"profile_pic":admins.profile_photo,"admin_users":admin_users})
    else:
        return redirect('login')


# login form for the Admin
def admin_login(request):

    if request.method == 'POST':

        postdata = request.POST.copy()
        username = postdata.get('username', '')
        password = postdata.get('password', '')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_super_admin == True or user.is_admin_user == True:
                login(request, user)
                return redirect('dashboard_admin')
        else:
            messages.info(request, "Invalid credentials")

            return render(request, 'admin_login.html')
    return render(request, 'admin_login.html')

#Detailed View of a property
def hotel_details(request, id):
    try:
        current_user = request.user
        current_user.is_admin_user
    except:
        messages.info(request,"Please login to your account")
        return redirect('login')
        
    if current_user.is_admin_user == True or current_user.is_super_admin == True:
        hotel = HotelUsers.objects.get(id=id)
        renewals = Renewals.objects.filter(hotel=hotel).count()
        if renewals:
            renewals_date = Renewals.objects.filter(hotel=hotel)[0]

        admin = AdminUsers.objects.get(admin_user=current_user)
        return render(request, 'admin_user/admin-property-detailedview.html', {"hotel":hotel,"renewals_date":renewals_date if renewals else None, "profile_pic": admin.profile_photo,"admin":admin,"admin_": admin,"renewals":renewals})

# Dashboard of the Admin
def dashboard_admin(request):
    try:
        current_user = request.user
        current_user.is_admin_user
    except:
        messages.info(request,"Please login to your account")
        return redirect('login')

    if current_user.is_admin_user == True or current_user.is_super_admin == True:
        hotels_object = HotelUsers.objects.all().order_by('-id')
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

        customer_list = Customer.objects.all()
        customer_this_month = Customer.objects.filter(date__range=[dates_1, dates_2])
        hotels_count = len(hotels_object)
        customers_count = len(customer_list)
        hotels_list = []
        thismonth = []
        hotels_order = HotelUsers.objects.all()
        this_month_renewals = HotelUsers.objects.filter(end_date__range=[dates_1, dates_2])

        this_month_revenue = HotelUsers.objects.filter(start_date__range=[dates_1, dates_2]).aggregate(Sum('amount'))
        this_month_renew_revenue = Renewals.objects.filter(renew_date__range=[dates_1, dates_2]).aggregate(Sum('amount'))
        today = datetime.utcnow().date()
        st = datetime(today.year, today.month, today.day, tzinfo=tz.tzutc())
        et = datetime(today.year, today.month, today.day, tzinfo=tz.tzutc())+ relativedelta(days=1)
        customer_today = Customer.objects.filter(date__range=[st, et])
        today_revenue = HotelUsers.objects.filter(start_date__range=[st, et]).aggregate(Sum('amount'))
        renew_revenue_today = Renewals.objects.filter(renew_date__range=[st, et]).aggregate(Sum('amount'))
        for hotels in hotels_object:
            # print(type(hotels.start_date))
        
            if dates_1 <= hotels.start_date and dates_2 >= hotels.start_date:
                thismonth.append(hotels)

            if hotels.status == "Waiting" and hotels.status != "Deactivate":
                hotels.status = "Waiting"
                hotels.save()
                hotels_list.append(hotels)
            elif hotels.end_date >= timezone.make_aware(datetime.now()) and hotels.status != "Waiting" and hotels.status != "Deactivate":
                hotels.status = "Active"
                hotels.save()
                hotels_list.append(hotels)
            elif hotels.end_date <= timezone.make_aware(datetime.now()) and hotels.status != "Waiting" and hotels.status != "Deactivate":
                hotels.status = "Inactive"
                hotels.save()
                hotels_list.append(hotels)
            elif hotels.status == "Deactivate":
                hotels_list.append(hotels)
        access_token_expired = HotelUsers.objects.filter(social_media=True).filter(access_token_end_date__lte = date.today())
        waiting_list = HotelUsers.objects.filter(status="Waiting")
        active_hotels = HotelUsers.objects.filter(status="Active").count()
        # inactive_hotels = HotelUsers.objects.filter(status="Inactive").count()+HotelUsers.objects.filter(status="Deactivate").count()
        inactive_hotels = HotelUsers.objects.filter(status__in=["Inactive","Deactivate"]).count()
        
        revenue = HotelUsers.objects.aggregate(Sum('amount')).get("amount__sum")
        renew_revenue = Renewals.objects.aggregate(Sum('amount')).get("amount__sum")
        hotels_today = HotelUsers.objects.filter(start_date__range=[st, et]).count()
        len_month = len(thismonth)
        admins = AdminUsers.objects.all()
        admin_ = AdminUsers.objects.get(admin_user=current_user)
        renewals_count = len(HotelUsers.objects.filter(status="Inactive"))
        context = {"profile_pic":admin_.profile_photo,"hotels_today":hotels_today,"today_revenue":int(today_revenue.get("amount__sum")) + int(renew_revenue_today.get("amount__sum") or 0) if today_revenue.get("amount__sum") != None else 0,"this_month_revenue":int(this_month_revenue.get("amount__sum")) + int(this_month_renew_revenue.get("amount__sum") or 0) if this_month_revenue.get("amount__sum")!= None else 0,"admin_": admin_,
        "admins":admins, "waiting_list": waiting_list, "hotel_list": hotels_list, "hotels_count": hotels_count,
         "customer_this_month": customer_this_month.count(), "customer_today":customer_today.count(),
        "customers_count": customers_count,"access_token_expired":access_token_expired, "renewals_count": renewals_count,
         "len_month": len_month,"revenue" :int(revenue or 0)+ int(renew_revenue or 0),"active":active_hotels,"inactive":inactive_hotels,"pending":waiting_list.count(),"this_month_renewals":this_month_renewals.count() }

        return render(request, 'admin_user/admin-dashboard.html', context=context)
    # "active":active_hotels,"inactive":inactive_hotels,"pending":waiting_list.count(),"waiting_list": waiting_list
    else:
        # return
        return redirect('login')

# EAAZBTHZAkMUZA4BAG0UU9bCjN3j4UFZB2aQhFyrxNqA7CaWXKzgQjycZAowGhUh6WY1Io7OtMil3wWJFN81HAb4tYXgnSVDztbDxUNyEUbgD6QR44f26sgkfs3kIj8VnFf78kzmPuJykwZBibUco8yuLPeYPfwflvMoiVI1UaVRdIxtEJhb6fq8vXkqpl6ekTezXjy1bx7F01GIDSqLdFj
# page_id - 106023245317843

# inst_id - 17841451497621889



# To update the propery details
def update_hotel(request, id):
    try:
        current_user = request.user
        current_user.is_admin_user
        admin = AdminUsers.objects.get(admin_user=current_user)
    except:
        messages.info(request,"Please login to your account")
        return redirect('login')

    if current_user.is_admin_user == True or current_user.is_super_admin == True:
        User = get_user_model()

        user = User.objects.get(id=id)

        hotel_all = AdminUsers.objects.all()

        hotel = HotelUsers.objects.get(hotel_user=user)

        context = {"hotel_all": hotel_all,"profile_pic":admin.profile_photo,
                   "hotel": hotel, "user": user, "id": id}

        return render(request, 'admin_user/admin-update-property.html', context=context)
    else:
        return redirect("login")


#Total property details and able to manage the properties
def manage_property(request):
    try:
        current_user = request.user
        current_user.is_admin_user
        admin = AdminUsers.objects.get(admin_user=current_user)
    except:
        messages.info(request,"Please login to your account")
        return redirect('login')

    if current_user.is_admin_user == True or current_user.is_super_admin == True:
        hotels_object = HotelUsers.objects.all().order_by('-id')
        admins = AdminUsers.objects.all()
        
        active_hotels = HotelUsers.objects.filter(status="Active").count()
        # inactive_hotels = HotelUsers.objects.filter(status="Inactive").count()+HotelUsers.objects.filter(status="Deactivate").count()
        inactive_hotels = HotelUsers.objects.filter(status__in=["Inactive","Deactivate"]).count()
        renewals_count = len(HotelUsers.objects.filter(status="Inactive"))
        reviews = Customer.objects.all().count()
        checkin = Checkin.objects.all().count()
        #month

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
        # print("hhhhuuhuhhii",date.today())
        today = datetime.utcnow().date()
        st = datetime(today.year, today.month, today.day, tzinfo=tz.tzutc())
        et = datetime(today.year, today.month, today.day, tzinfo=tz.tzutc())+ relativedelta(days=1)
        hotels_today = HotelUsers.objects.filter(start_date__range=[st, et]).count()
        hotels_this_month = HotelUsers.objects.filter(start_date__range=[dates_1, dates_2]).count()

        reviews_this_month = Customer.objects.filter(date__range=[dates_1, dates_2]).count()
        reviews_today = Customer.objects.filter(date__range=[st, et]).count()
        checkin_this_month = Checkin.objects.filter(check_in__range=[dates_1, dates_2]).count()
        checkin_today = Checkin.objects.filter(check_in=date.today()).count()
        context = {"checkin_today":checkin_today,"profile_pic":admin.profile_photo,"checkin_this_month":checkin_this_month,"reviews_today":reviews_today,"reviews_this_month":reviews_this_month,"hotel_list": hotels_object,"hotels_today":hotels_today,"hotels_this_month":hotels_this_month, "admins":admins ,"properties":hotels_object.count(),"active":active_hotels,"inactive":inactive_hotels,"renewals_count": renewals_count,"reviews":reviews,"checkin":checkin}
        
        return render(request, 'admin_user/admin-manage-property.html', context=context)
    else:
        return redirect('login')


#Update Property details from the form 

def update_hotel_function(request, id):
    try:
        current_user = request.user
        current_user.is_admin_user
        admin = AdminUsers.objects.get(admin_user=current_user)
    except:
        messages.info(request,"Please login to your account")
        return redirect('login')

    if current_user.is_super_admin == True or current_user.is_admin_user == True:
        User = get_user_model()
        user_a = User.objects.get(id=id)
        hotel_object = HotelUsers.objects.get(hotel_user=user_a)
        if request.method == 'POST':
            name = request.POST["username"]
            firstname = request.POST["firstname"]
            mobile = request.POST["mobile"]
            email = request.POST["email"]
            profile_photo = request.FILES.get("profile_photo", False)
            agreement = request.FILES.get("agreement", False)
            psw = request.POST["password"]
            amount = request.POST["amount"]
            tax = request.POST["tax"]
            total = request.POST["total"]

            property_name = request.POST["property_name"]
            type_of = request.POST["type_of"]
            city = request.POST["location"]
            state = request.POST["state"]
            country = request.POST["country"]
            admin_user = request.POST["admin_user"]
            website = request.POST["website"]
            address = request.POST["address"]
            if psw:
      
                user_a.username = name
                user_a.email=email
                user_a.first_name=firstname
                user_a.set_password(psw)
                user_a.save()
           
            if profile_photo != False:
                hotel_object.profile_photo = profile_photo
                hotel_object.save()
            if agreement != False:
                hotel_object.agreement = agreement
                hotel_object.save()


            if hotel_object.other:
               
                trip_adviser_link = request.POST.get("trip_adviser_link", False)
                google_link = request.POST["google_link"]
                review_url = request.POST["url"]
                qr_code = request.FILES.get("qr_code", False)
                # new fields
                # facebook_access_token = request.POST["facebook_access_token"]
                if hotel_object.social_media:
                    page_id = request.POST["page_id"]
                    insta_id = request.POST["insta_id"]
                else:
                    page_id = ""
                    insta_id = ""
                
                if qr_code != False:
                    hotel_object.qr_code = qr_code
                    hotel_object.save()

                hotel_object.hotel_user = user_a
                hotel_object.property_name=property_name
                hotel_object.password=psw                                                                
                hotel_object.trip_adviser_link=trip_adviser_link                                                                
                hotel_object.type_of=type_of                                                                
                hotel_object.insta_id=insta_id                                                                
                hotel_object.page_id=page_id                                                                
                hotel_object.google_link=google_link                                                                
                hotel_object.mobile=mobile                                                                
                hotel_object.website=website                                                                
                hotel_object.address=address         
                hotel_object.amount = amount                                                       
                hotel_object.tax = tax
                hotel_object.total = total                                                       
                hotel_object.country = country                                                       
                hotel_object.url=review_url                                                                
                hotel_object.location=city
                hotel_object.state=state
                hotel_object.save()


            if hotel_object.express_checkin:
                url_checkin = request.POST["url_checkin"]
                checkin_qr = request.FILES.get("checkin_qr", False)

            
                
                    # status=status
                if checkin_qr != False:

                    hotel_object.hotel_user = user_a
                    hotel_object.property_name=property_name
                    hotel_object.password=psw                                                                
                    hotel_object.type_of=type_of
                    hotel_object.checkin_qr = checkin_qr
                    hotel_object.url_checkin = url_checkin
                    hotel_object.address=address
                    hotel_object.amount = amount                                                   
                    hotel_object.tax = tax
                    hotel_object.mobile = mobile
                    hotel_object.total = total 
                    hotel_object.country = country
                    hotel_object.website=website
                    hotel_object.location=city
                    hotel_object.state=state
                    hotel_object.save()

            user_d = User.objects.get(username=str(admin_user))
            ad_user = AdminUsers.objects.get(admin_user=user_d)
            hotel_object.admin_name = ad_user
    
            hotel_object.save()
            return redirect("manage_property")

        return render(request, 'admin_user/admin-update-property.html', {"id": id, "profile_pic":admin.profile_photo})
    else:
        return redirect("login")

    # return render(request, 'admin_user/update_hotel.html', {"id": id})


# To view the renew form of the selected property
def renew(request, id):
    try:
        current_user = request.user
        current_user.is_admin_user
        admin = AdminUsers.objects.get(admin_user=current_user)

    except:
        messages.info(request,"Please login to your account")
        return redirect('login')
    if current_user.is_super_admin == True or current_user.is_admin_user == True:
        hotel = HotelUsers.objects.get(id=id)

        return render(request, 'admin_user/admin-renewal.html', {"id": id, "hotel": hotel, "profile_pic":admin.profile_photo})
    else:
        return redirect('login')

#To delete the property
def delete_hotel(request, id):
    try:
        current_user = request.user
        current_user.is_admin_user
    except:
        messages.info(request,"Please login to your account")
        return redirect('login')
    if current_user.is_super_admin == True or current_user.is_admin_user == True:
        User = get_user_model()
        user = User.objects.get(id=id)
        hotel = HotelUsers.objects.get(hotel_user=user)
        hotel.delete()
        user.delete()
        return redirect('manage_property')

    else:
        return redirect("dashboard_admin")

# To renew the hotel from the form
def renew_hotel(request):
    try:
        current_user = request.user
        current_user.is_admin_user
    except:
        messages.info(request,"Please login to your account")
        return redirect('login')

    if current_user.is_super_admin == True or current_user.is_admin_user == True:

        if request.method == 'POST':
            property_code = request.POST["property_code"]
            property_name = request.POST["property_name"]
            # lastname = request.POST["lastname"]
            duration = request.POST["duration"]
            amount = request.POST["amount"]

            if duration == "7":
                end_date = datetime.today() + relativedelta(days=+int(duration))
            else:
                end_date = datetime.today() + relativedelta(months=+int(duration))

           
            agreement = request.FILES.get("agreement")
           
            current_hotel = HotelUsers.objects.get(property_code=property_code)
            renewals = Renewals.objects.create(hotel=current_hotel, renew_date=current_hotel.start_date, amount=current_hotel.amount,
                                               google=current_hotel.google, trip_adviser=current_hotel.trip_adviser, g_t=current_hotel.g_t, t_g=current_hotel.t_g, social_media=current_hotel.social_media, agreement=current_hotel.agreement, duration=current_hotel.duration)
            hotel = HotelUsers.objects.filter(property_code=property_code)
            # end_date = datetime.today() + relativedelta(months=+int(hotel.duration))
            current_hotel.end_date = timezone.make_aware(end_date)
            current_hotel.status = "Waiting"
            current_hotel.duration = duration
            current_hotel.amount = amount
            current_hotel.agreement = agreement
            current_hotel.save()
            return redirect("dashboard_admin")
    else:
        return redirect('login')


# To approve the request from admin to the superadmin
def super_admin_approve(request, id):
    try:
        current_user = request.user
        current_user.is_admin_user
    except:
        messages.info(request,"Please login to your account")
        return redirect('login')

    if current_user.is_super_admin == True:
        hotel = HotelUsers.objects.get(id=id)
        hotel.status = "Active"
        hotel.start_date = datetime.now()
        
        if int(hotel.duration) == 7:
            end_date = datetime.today() + relativedelta(days=+int(hotel.duration))
        else:
            end_date = datetime.today() + relativedelta(months=+int(hotel.duration))
        hotel.end_date = end_date
        hotel.save()
        if hotel.without_backend == False:
            html_tpl_path = 'email/email.html'

            context_data = {'username': hotel.hotel_user.username, "hotel_owner": hotel.hotel_user.first_name,
                            "property_name": hotel.property_name,"property_code": hotel.property_code, "password": hotel.password}
            email_html_template = get_template(html_tpl_path).render(context_data)

            email_msg = EmailMessage('Your registration completed',
                                     email_html_template,
                                     "Hudels <noreply@hudels.com>",
                                     [hotel.hotel_user.email],
                                     reply_to=[settings.APPLICATION_EMAIL]
                                     )
            # this is the crucial part that sends email as html content but not as a plain text
            email_msg.content_subtype = 'html'
            if hotel.express_checkin:
                with open(finders.find('images/checkins.png'), 'rb') as f:
                    logo = f.read()
            if hotel.other:
                with open(finders.find('assets/img/socioconnects.png'), 'rb') as f:
                    logo = f.read()

            with open(finders.find('images/image-2.png'), 'rb') as f:
                tick = f.read()

            logoMime = MIMEImage(logo, 'png')
            tickMime = MIMEImage(tick, 'png')
            tickMime.add_header('Content-ID', '<tickMime>')
            logoMime.add_header('Content-ID', '<logoMime>')
            email_msg.attach(logoMime)
            email_msg.attach(tickMime)
            email_msg.send(fail_silently=False)

        return redirect('dashboard_admin')
    else:
        return redirect('login')


def manager_list(request):
    try:
        current_user = request.user
        current_user.is_admin_user
        admin_user = AdminUsers.objects.get(admin_user=current_user)

    except:
        messages.info(request,"Please login to your account")
        return redirect('login')

    if current_user.is_super_admin == True:
        admin = AdminUsers.objects.all()
        return render(request, 'admin_user/admin-manage-user.html', {"admin": admin, "profile_pic":admin_user.profile_photo})
    else:
        return redirect('login')


def update_manager(request, id):
    try:
        current_user = request.user
        current_user.is_admin_user
        admin_user = AdminUsers.objects.get(admin_user=current_user)

    except:
        messages.info(request,"Please login to your account")
        return redirect('login')

    if current_user.is_super_admin == True:
        admin = AdminUsers.objects.get(id=id)

        return render(request, 'admin_user/admin-update-user.html', {"id": id, "admin": admin, "profile_pic":admin_user.profile_photo})

    else:
        return redirect('login')

# Update details of admin users
def update_admin_function(request, id):
    try:
        current_user = request.user
        current_user.is_admin_user

    except:
        messages.info(request,"Please login to your account")
        return redirect('login')

    if current_user.is_super_admin == True:

        if request.method == 'POST':
            name = request.POST["username"]
            firstname = request.POST["firstname"]
            lastname = request.POST["lastname"]
            email = request.POST["email"]
            psw = request.POST["password"]
            # repeat_password = request.POST["confirm_password"]
            designation = request.POST["designation"]
            # try:
            #     profile_photo = request.FILES["profile_photo"]
            # except:
            #     profile_photo= False
            User = get_user_model()

            user = User.objects.filter(id=id).update(
                username=name, first_name=firstname, last_name=lastname, email=email)
            user_a = User.objects.get(id=id).set_password(psw)

            adm_user = User.objects.get(id=id)
            AdminUsers.objects.filter(admin_user=adm_user).update(
                designation=designation, password=psw)
            return redirect('dashboard_admin')
    else:
        return redirect('login')

#To logout the user
def logout_view(request):
    logout(request)
    return redirect('/')

# The profile of admin user
def admin_profile(request):
    try:
        current_user = request.user
        current_user.is_admin_user
        admin_user = AdminUsers.objects.get(admin_user=current_user)

    except:
        messages.info(request,"Please login to your account")
        return redirect('login')

    if current_user.is_super_admin == True:
        admin = AdminUsers.objects.get(admin_user=current_user)
        return render(request, 'admin_user/admin_profile.html', {"admin": admin, "current_user": current_user, "profile_pic":admin_user.profile_photo})
    else:
        return redirect('login')

# To delete admin users (not using)
def delete_admin(request, id):
    try:
        current_user = request.user
        current_user.is_admin_user
    except:
        messages.info(request,"Please login to your account")
        return redirect('login')

    if current_user.is_super_admin == True:
        User = get_user_model()
        user = User.objects.get(id=id)
        admin_user = AdminUsers.objects.get(admin_user=user)

        admin_user.delete()
        user.delete()
        return redirect('manager_list')
    else:
        return redirect('login')

#Complaints got from hotels
def complaints_admin(request):
    try:
        current_user = request.user
        current_user.is_admin_user
        admin_user = AdminUsers.objects.get(admin_user=current_user)

    except:
        messages.info(request,"Please login to your account")
        return redirect('login')

    if current_user.is_super_admin == True:
        complaints = Complaints.objects.all().order_by('-id')
        return render(request, 'admin_user/complaints_admin.html', {"complaints": complaints})
    if current_user.is_admin_user == True:
        admin = AdminUsers.objects.get(admin_user=current_user)
        complaints_manager = Complaints.objects.filter(admin_user=admin)

        return render(request, 'admin_user/complaints_admin.html', {"complaints_manager": complaints_manager, "profile_pic":admin_user.profile_photo})

# Complaint status
def complaint_status(request, id):
    try:
        current_user = request.user
        current_user.is_admin_user
    except:
        messages.info(request,"Please login to your account")
        return redirect('login')

    if current_user.is_super_admin == True or current_user.is_admin_user == True:
        complaint = Complaints.objects.get(id=id)
        if complaint.status == "working":
            Complaints.objects.filter(id=id).update(status="solved")
            return redirect("complaints_admin")
        if complaint.status == "new":
            Complaints.objects.filter(id=id).update(status="working")
            return redirect("complaints_admin")

# Update the faceboook access token
def update_token(request, id):
    try:
        current_user = request.user
        current_user.is_admin_user
    except:
        messages.info(request,"Please login to your account")
        return redirect('login')

    if current_user.is_super_admin == True or current_user.is_admin_user == True:
        if request.method == 'POST':
            access_token = request.POST["access_token"]
            hotel = HotelUsers.objects.filter(id=id).update(
                facebook_access_token=access_token, access_token_end_date=date.today() + relativedelta(days=+27))
            return redirect("dashboard_admin")


# google review
def gr_list(request):
    try:
        current_user = request.user
        current_user.is_admin_user
    except:
        messages.info(request,"Please login to your account")
        return redirect('login')

    if current_user.is_admin_user == True or current_user.is_super_admin == True:
        google_qr_prop = GoogleQr.objects.all().order_by('-id')
        google_qr = []
        for google in google_qr_prop:
            if google.end_date >= date.today() and google.status != "deactivated":
                google.status = "active"
                google.save()
                google_qr.append(google)
            if google.end_date <= date.today() and google.status != "deactivated":
                google.status = "inactive"
                google.save()
                google_qr.append(google)
            if google.status == "deactivated":
                google_qr.append(google)

        return render(request, 'admin_user/gr_list_view.html', {"google_qr": google_qr})


def gr_property(request):
    try:
        current_user = request.user
        current_user.is_admin_user
    except:
        messages.info(request,"Please login to your account")
        return redirect('login')

    if current_user.is_admin_user == True or current_user.is_super_admin == True:
        if request.method == "POST":

            name = request.POST["name"]
            mobile = request.POST["mobile"]
            place_id = request.POST["place_id"]
            duration = request.POST["duration"]
            package = request.POST["package"]
            email = request.POST["email"]
            city = request.POST["location"]
            state = request.POST["stt"]
            address = request.POST["address"]
            amount = request.POST["amount"]
            agreement = request.FILES.get("agreement", False)
            review_hotel = GoogleQr.objects.create(name=name, mobile=mobile, start_date=date.today(), place_id=place_id, duration=duration, email=email,
                                                   city=city, state=state, address=address, package=package, amount=amount, agreement=agreement, status="active")

            if duration == "7":
                end_date = date.today() + relativedelta(days=+int(duration))
            else:
                end_date = date.today() + relativedelta(months=+int(duration))

            domain = request.build_absolute_uri('/')[:-1]
            qrcode = segno.make(
                str(domain) + "/checkin/googlerating/"+str(review_hotel.id))
# Save the QR code with transparent background and use dark blue for
# the dark modules
            out = BytesIO()
            qrcode.save(out, kind='png', dark='#000000', light=None, scale=3)

            review_hotel.qr_code.save(
                'Hudels.png', ContentFile(out.getvalue()), save=False)
            review_hotel.end_date = end_date
            review_hotel.link = domain + \
                "/checkin/googlerating/"+str(review_hotel.id)
            review_hotel.save()
            return redirect("dashboard_admin")
        return render(request, 'admin_user/gr_create_property.html')


def gr_detail(request, id):
    try:
        current_user = request.user
        current_user.is_admin_user
    except:
        messages.info(request,"Please login to your account")
        return redirect('login')

    if current_user.is_admin_user == True or current_user.is_super_admin == True:
        property = GoogleQr.objects.get(id=id)
        return render(request, 'admin_user/gr_detail_view.html', {"property": property})


def renew_review(request, id):
    try:
        current_user = request.user
        current_user.is_admin_user
    except:
        messages.info(request,"Please login to your account")
        return redirect('login')

    if current_user.is_admin_user == True or current_user.is_super_admin == True:
        property = GoogleQr.objects.get(id=id)
        if request.method == "POST":
            name = request.POST["name"]
            package = request.POST["package"]
            duration = request.POST["duration"]
            amount = request.POST["amount"]
            if duration == "7":
                end_date = date.today() + relativedelta(days=+int(duration))
            else:
                end_date = date.today() + relativedelta(months=+int(duration))
            property = GoogleQr.objects.filter(id=id).update(
                package=package, duration=duration, amount=amount, end_date=end_date, start_date=date.today())
            return redirect('gr_list')


def gr_update(request, id):
    try:
        current_user = request.user
        current_user.is_admin_user
    except:
        messages.info(request,"Please login to your account")
        return redirect('login')

    if current_user.is_admin_user == True or current_user.is_super_admin == True:
        property = GoogleQr.objects.get(id=id)
        if request.method == "POST":
            name = request.POST["name"]
            mobile = request.POST["mobile"]
            place_id = request.POST["place_id"]
            link = request.POST["link"]
            package = request.POST["city"]
            email = request.POST["email"]
            city = request.POST["city"]
            state = request.POST["state"]
            address = request.POST["address"]
            agreement = request.FILES.get("agreement", False)
            qr_code = request.FILES.get("qr_code", False)

            if agreement != False:
                property = GoogleQr.objects.filter(id=id).update(name=name, mobile=mobile, place_id=place_id, link=link,
                                                                 city=city,  package=package, email=email, state=state, address=address, agreement=agreement)
            if qr_code != False:
                property = GoogleQr.objects.filter(id=id).update(name=name, mobile=mobile, place_id=place_id, link=link,
                                                                 city=city, package=package, email=email, state=state, address=address, qr_code=qr_code)
            else:
                property = GoogleQr.objects.filter(id=id).update(name=name, mobile=mobile, place_id=place_id, link=link,
                                                                 city=city, package=package, email=email, state=state, address=address)

            return redirect("gr_list")
        return render(request, 'admin_user/gr_update_view.html', {"customer": property})


def activate_review(request, id):
    try:
        current_user = request.user
        current_user.is_admin_user
    except:
        messages.info(request,"Please login to your account")
        return redirect('login')

    if current_user.is_admin_user == True or current_user.is_super_admin == True:
        property = GoogleQr.objects.get(id=id)

        if property.status == "deactivated":
            property.status = "active"
            property.save()
            return redirect('gr_list')


def deativate_review(request, id):
    try:
        current_user = request.user
        current_user.is_admin_user
    except:
        messages.info(request,"Please login to your account")
        return redirect('login')

    if current_user.is_admin_user == True or current_user.is_super_admin == True:
        property = GoogleQr.objects.get(id=id)

        if property.status == "active":
            property.status = "deactivated"
            property.save()
            return redirect('gr_list')


def gr_total_reviews(request):
    try:
        current_user = request.user
        current_user.is_admin_user
    except:
        messages.info(request,"Please login to your account")
        return redirect('login')

    if current_user.is_admin_user == True or current_user.is_super_admin == True:

        ratings = Ratings.objects.all().order_by('-id')
        return render(request, 'admin_user/gr_total_reviews.html', {'ratings': ratings})

def detail_hotel_review(request, id):
    try:
        current_user = request.user
        current_user.is_admin_user
        admin_user = AdminUsers.objects.get(admin_user=current_user)

    except:
        messages.info(request,"Please login to your account")
        return redirect('login')

    if current_user.is_admin_user == True or current_user.is_super_admin == True:
        hotel_object = HotelUsers.objects.get(id=id)
        reviews = Customer.objects.filter(hotel=hotel_object)
        return render(request, 'admin_user/admin-hotel-review.html', {'reviews': reviews, 'hotel_object':hotel_object,"profile_pic":admin_user.profile_photo})

def detail_hotel_checkin(request, id):
    try:
        current_user = request.user
        current_user.is_admin_user
        admin_user = AdminUsers.objects.get(admin_user=current_user)

    except:
        messages.info(request,"Please login to your account")
        return redirect('login')
    if current_user.is_admin_user == True or current_user.is_super_admin == True:
        hotel_object = HotelUsers.objects.get(id=id)
        checkins = Checkin.objects.filter(hotel=hotel_object)
        return render(request, 'admin_user/admin-hotel-checkin.html', {'checkins': checkins, 'hotel_object':hotel_object, "profile_pic":admin_user.profile_photo})

def total_review_list(request):
    try:
        current_user = request.user
        current_user.is_admin_user
        admin_user = AdminUsers.objects.get(admin_user=current_user)

    except:
        messages.info(request,"Please login to your account")
        return redirect('login')
    if current_user.is_admin_user == True or current_user.is_super_admin == True:
        customer = Customer.objects.all()
        hotels  = HotelUsers.objects.all()
        context = {"hotels":hotels, "customers": customer, "profile_pic":admin_user.profile_photo}
        return render(request, 'admin_user/admin-total-review.html', context=context)

def total_checkin_list(request):
    try:
        current_user = request.user
        current_user.is_admin_user
        admin_user = AdminUsers.objects.get(admin_user=current_user)

    except:
        messages.info(request,"Please login to your account")
        return redirect('login')
    if current_user.is_admin_user == True or current_user.is_super_admin == True:
        customer = Checkin.objects.all()
        hotels  = HotelUsers.objects.all()
        context = {"hotels":hotels, "customers": customer, "profile_pic":admin_user.profile_photo}
        return render(request, 'admin_user/admin-total-checkin.html', context=context)


# To update the products used by hotels
def update_products(request, id):
    try:
        current_user = request.user
        current_user.is_admin_user
        admin_user = AdminUsers.objects.get(admin_user=current_user)
    except:
        messages.info(request,"Please login to your account")
        return redirect('login')
        
    if current_user.is_super_admin == True or current_user.is_admin_user == True:
        hotel = HotelUsers.objects.get(id=id)
        if request.method=="POST":
            property_code = request.POST["property_code"]
            property_name = request.POST["property_name"]
            # lastname = request.POST["lastname"]
            google = request.POST.get("google", False)
            tripadvisor = request.POST.get("tripadvisor", False)
            socialmedia = request.POST.get("social_media", False)
            whatsapp = request.POST.get("whatsapp", False)
            g_t = request.POST.get("g_t", False)
            t_g = request.POST.get("t_g", False)
            checkin = request.POST.get("checkin", False)
            tripadvisor_link = request.POST["tripadvisor_link"]
            google_link = request.POST["google_link"]
            access_token = request.POST["facebook_access_token"]
            inhouse = request.POST.get("inhouse", False)
            page_id = request.POST["page_id"]
            insta_id = request.POST["insta_id"]
            checkin_url = request.POST["checkin_url"]
            without_email = request.POST.get("without_email", False)
            without_filter = request.POST.get("without_filter", False)
            review_url = request.POST["review_url"]
            checkin_qr = request.FILES.get("checkin_qr", False)
            review_qr = request.FILES.get("review_qr", False)

            # hotels = HotelUsers.objects.filter(id=id).update(trip_adviser_link=tripadvisor_link,google_link=google_link,facebook_access_token=access_token,
            # page_id=page_id,insta_id=insta_id, url_checkin=checkin_url, with_filter=with_filter, without_filter=without_filter, url=review_url,
            # checkin_qr=checkin_qr, qr_code=review_qr)
            
            if inhouse == "True" or google == "True" or tripadvisor == "True" or t_g == "True" or g_t == "True" or socialmedia == "True":
                hotel.other = True
                hotel.google=True if google == "True" else False
                hotel.trip_adviser=True if tripadvisor == "True" else False
                hotel.social_media=True if socialmedia == "True" else False
                hotel.g_t=True if g_t == "True" else False
                hotel.whatsapp=True if whatsapp =="True" else False
                hotel.inhouse=True if inhouse == "True" else False
                hotel.t_g=True if t_g == "True" else False
                hotel.trip_adviser_link=tripadvisor_link
                hotel.express_checkin=True if checkin == "True" else False
                hotel.access_token_end_date = date.today() + relativedelta(days=+27)
                hotel.google_link = google_link
                hotel.page_id = page_id
                hotel.facebook_access_token=access_token
                hotel.insta_id = insta_id
                hotel.url_checkin = checkin_url
                hotel.checkin_qr = checkin_qr
                hotel.without_email = without_email
                hotel.without_filter = without_filter
                hotel.url = review_url
                hotel.qr_code = review_qr
                hotel.save()
            else:
                hotel.other = False
                hotel.express_checkin=True if checkin == "True" else False
                hotel.whatsapp=True if whatsapp =="True" else False
                hotel.url_checkin = checkin_url
                hotel.checkin_qr = checkin_qr
                hotel.save()
            return redirect("dashboard_admin")
        return render(request,'admin_user/admin-update-products.html', {"id": id,"hotel":hotel})

# To deativate the properties
def deactivate(request, id):
    try:
        current_user = request.user
        current_user.is_admin_user
    except:
        messages.info(request,"Please login to your account")
        return redirect('login')

    if current_user.is_admin_user == True or current_user.is_super_admin == True:
        hotel = HotelUsers.objects.get(id=id)
        if hotel.status == "Active":
            hotel.status = "Deactivate"
            hotel.save()
            return redirect("dashboard_admin")
        if hotel.status == "Deactivate":
            hotel.status = "Active"
            hotel.save()
            return redirect("dashboard_admin")
        return render(request, 'admin_user/admin-property-detailedview.html', {"hotel": hotel})





# --------------------- ANWAR -----------------------------------------

def register_restaurant(request):
    try:
        current_user = request.user
        current_user.is_admin_user
        admin = AdminUsers.objects.get(admin_user=current_user)
    except:
        messages.info(request,"Please login to your account")
        return redirect('login')
    admin_users = AdminUsers.objects.all()

    if request.method == 'POST':
        r_username = request.POST["username"]

        r_restaurant_name = request.POST["property_name"]
        r_owner_name = request.POST["firstname"]
        r_type_of = request.POST["type_of"]
        r_password = request.POST["password"]
        r_user_email = request.POST["email"]
        r_user_mobile = request.POST["mobile"]
        r_profile_photo = request.FILES.get("profile_photo", False)
        r_address = request.POST["address"]
        r_location = request.POST["location"]
        r_state = request.POST["state"]
        r_country = request.POST["country"]
        r_tablecount = request.POST["tablecount"]
        r_amount = request.POST["amount"]
        r_tax = request.POST["tax"]
        r_total = request.POST["total"]
        r_duration = request.POST["duration"]
        r_website = request.POST["website"]
        r_agreement = request.FILES.get("agreement", False)

        r_admin_user = request.POST["admin_user"]
        
        

        # r_qr = request.FILES["qrfile"]
        # adminname = DeveloperAdmin.objects.get(id=r_admin_user)

        User = get_user_model()
        use = User.objects.filter(username=r_username)
        user_d = User.objects.get(username=str(r_admin_user))
        ad_user = AdminUsers.objects.get(admin_user=user_d)
        if use:

            messages.error(request, "Username Taken")

        else:
            field_name = 'admin_user__username__icontains'
            admin_user_object = AdminUsers.objects.get(
                admin_user=current_user)

            if r_password == r_password:
                user = User.objects.create_user(
                    username=r_username, email=r_user_email, password=r_password, first_name=r_owner_name)
                user.is_restaurantmenucard = True
                user.save()

                
            
                restaurant=RestaurantUser(restaurant_name=r_restaurant_name,
                                            owner_name=r_owner_name,
                                            # username=r_username,
                                            type_of=r_type_of,
                                            password=r_password,
                                            user_email=r_user_email,
                                            user_mobile=r_user_mobile,
                                            profile_photo=r_profile_photo,
                                            address=r_address,
                                            location=r_location,
                                            state=r_state,
                                            country=r_country,
                                            tablecount=r_tablecount,
                                            amount=r_amount,
                                            tax=r_tax,
                                            total=r_total,
                                            duration=r_duration,
                                            website=r_website,
                                            agreement=r_agreement,
                                            admin_name= ad_user,
                                            status="Waiting",
                                            restaurant_user=user

                                            )
                restaurant.save()

                restaurant.access_token_end_date = date.today() + relativedelta(days=+27)
                if r_duration == "7":
                    end_date = datetime.today() + relativedelta(days=+int(r_duration))
                else:
                    end_date = datetime.today() + relativedelta(months=+int(r_duration))
                restaurant.end_date = timezone.make_aware(end_date)
                restaurant.property_code =  "SC" + \
                                str(restaurant.id).zfill(5)
                restaurant.save()
                
                def range1(start, end):
                    return range(start, end+1)
                
                for i in range1(1, int(r_tablecount)):
                    documents = request.FILES.get("qr"+str(i), False)
                    tableqrcodes.objects.create(tableqr=documents,restaurantname_id=restaurant.id)

                # resid=(restaurant.id)
                # restaurantqr=tableqrcodes(tableqr=r_qr,restaurantname_id=resid)
                # restaurantqr.save()

                return redirect("admin_manage_restaurant")
                                                
    return render(request,'admin_user/register_restaurant.html',{"admin_users":admin_users})




def admin_manage_restaurant(request):
    try:
        current_user = request.user
        current_user.is_admin_user
        admin = AdminUsers.objects.get(admin_user=current_user)
    except:
        messages.info(request,"Please login to your account")
        return redirect('login')
    admins = AdminUsers.objects.all()
    restaurant=RestaurantUser.objects.all().order_by('-id')
    active_restaurant = RestaurantUser.objects.filter(status="Active").count()
    inactive_restaurants = RestaurantUser.objects.filter(status__in=["Inactive","Deactivate"]).count()
    renewals_count = len(RestaurantUser.objects.filter(status="Inactive"))
    waiting_list = RestaurantUser.objects.filter(status="Waiting")
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
    
    today = datetime.utcnow().date()
    st = datetime(today.year, today.month, today.day, tzinfo=tz.tzutc())
    et = datetime(today.year, today.month, today.day, tzinfo=tz.tzutc())+ relativedelta(days=1)
    restaurant_today = RestaurantUser.objects.filter(start_date__range=[st, et]).count()
    restaurant_this_month = RestaurantUser.objects.filter(start_date__range=[dates_1, dates_2]).count()


    context = {"restaurant":restaurant,"restaurant_today":restaurant_today,"restaurant_this_month":restaurant_this_month,"properties":restaurant.count(),"active":active_restaurant,"inactive":inactive_restaurants,"renewals_count": renewals_count, "admins":admins, "waiting_list": waiting_list,}
        


    return render(request,'admin_user/admin_manage_restaurant.html',context=context)

def restaurant_approve(request, id):
    try:
        current_user = request.user
        current_user.is_admin_user
    except:
        messages.info(request,"Please login to your account")
        return redirect('login')
    
    restaurant = RestaurantUser.objects.get(id=id)
    restaurant.status = "Active"
    restaurant.start_date = datetime.now()
    if int(restaurant.duration) == 7:
        end_date = datetime.today() + relativedelta(days=+int(restaurant.duration))
    else:
        end_date = datetime.today() + relativedelta(months=+int(restaurant.duration))
    restaurant.end_date = end_date
    restaurant.save()
    if restaurant == False:
        html_tpl_path = 'email/emailforrestaurantmenucard.html'

        context_data = {'username': restaurant.username, "hotel_owner": restaurant.owner_name,
                        "property_name": restaurant.restaurant_name,"property_code": restaurant.property_code, "password": restaurant.password}
        email_html_template = get_template(html_tpl_path).render(context_data)

        email_msg = EmailMessage('Your registration completed',
                                            email_html_template,
                                            "Hudels <noreply@hudels.com>",
                                            [restaurant.user_email],
                                            reply_to=[settings.APPLICATION_EMAIL]
                                            )
        email_msg.content_subtype = 'html'
        if restaurant.express_checkin:
            with open(finders.find('images/checkins.png'), 'rb') as f:
                logo = f.read()
        if restaurant.other:
            with open(finders.find('assets/img/socioconnects.png'), 'rb') as f:
                logo = f.read()

        with open(finders.find('images/image-2.png'), 'rb') as f:
            tick = f.read()

        logoMime = MIMEImage(logo, 'png')
        tickMime = MIMEImage(tick, 'png')
        tickMime.add_header('Content-ID', '<tickMime>')
        logoMime.add_header('Content-ID', '<logoMime>')
        email_msg.attach(logoMime)
        email_msg.attach(tickMime)
        email_msg.send(fail_silently=False)


    return redirect('admin_manage_restaurant')
