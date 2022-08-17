from email.mime import image
from json import dumps
from django.shortcuts import render, redirect
from django.core.files.uploadedfile import InMemoryUploadedFile
import base64
import io
from email.mime.image import MIMEImage
from django.contrib.staticfiles import finders
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.contrib import messages
from express_checkin.models import Checkin, GoogleQr, OtherDocuments, Ratings
from PIL import Image
from django.contrib.auth import get_user_model
# import datetime
from django.contrib.staticfiles import finders
from django.conf import settings
from hotel.models import HotelUsers
import base64
from django.core.files.base import ContentFile
from django.contrib.auth import authenticate, login, logout
import calendar
from datetime import date, timedelta,datetime
from django.utils import timezone
import time
import requests
from django.core.files.storage import FileSystemStorage


#This is a function for sending whatsapp messages with whatsapp cloud API

def SendWhatsapp(to, template, hotel, room, checkin,checkout,mobile):
    url = "https://graph.facebook.com/v14.0/105843008848181/messages"
    print(to, template, hotel, room, checkin,checkout,mobile)
 
    headers = {"Content-Type": "application/json", "Connection":"keep-alive", "Authorization": "Bearer EABJfq9jYvloBAACO7YgnzMqADTxBPanNUsYatASSw6vyIXxJCfGjfxLOYZA5s3N1OXP9XMtd9V9hlE5HWHZCWfyk7B3RHdUVwRnKlYfa0TYsv9o4xVoVmgXUSqLdZAVuESNr0ChTpZAbRZA5qQBKQluDvpGkNgjy5M69ghi4zwA74dIOQ48w4ZA8xt19N2jJebb6oh6sEaSwZDZD", }
 
    data = {
    "messaging_product": "whatsapp",
    "to": to,
    "type": "template",
    "template": {
        "name": template,
        "language": {
            "code": "en"
        },
        "components": [
      {
        "type": "body",
        "parameters": [
          {
            "type": "text",
            "text": hotel
          },
        
      {
        
            "type": "text",
            "text": room
        
      },
      {
        
            "type": "date_time",
            "date_time": {
              "fallback_value": checkin
            }
         
      },
      {
        
            "type": "date_time",
            "date_time": {
              "fallback_value": checkout
            }
         
      },
      {
        
            "type": "text",
            "text": mobile
         
      }
        ]
        
    }
        ]
    }
    }
    response = requests.post(url, headers=headers, json=data)
    return response

# Home page of the website socioconnects.com
def index(request):

    return render(request, 'index.html')


#checking the mobile is already saved or not and it will redirect to the next page with the customer details if the number is saved once
def check_mobile(request, username):
    User = get_user_model()
    user = User.objects.get(username=username)
    hotel_user = HotelUsers.objects.get(hotel_user=user)
    if request.method=="POST" and user.is_hotel==True and hotel_user.express_checkin == True and hotel_user.end_date >= timezone.make_aware(datetime.now()) and hotel_user.status!="inactive":
        phone = request.POST["phone"]
        # phone = customer_phone
        try:
            customer = Checkin.objects.filter(mobile=phone)[0]
            
        except:
            customer = False
        return render(request,'checkin/checkin-form.html', {"hotel_name":hotel_user.property_name,"hotel_profile":hotel_user.profile_photo , "username":user.username, "customer":customer, "phone":phone})
    return render(request, 'checkin/checkin-login.html', {"hotel_profile":hotel_user.profile_photo, "hotel_name":hotel_user.property_name, "username": user.username})


# Checkin form 
def checkin(request, username):
    User = get_user_model()
    user = User.objects.get(username=username)
    hotel = HotelUsers.objects.get(hotel_user=user)
    quests = Checkin.objects.filter(hotel=hotel).count()
    if request.method=="POST" and user.is_hotel==True and hotel.express_checkin == True and hotel.end_date >= timezone.make_aware(datetime.now()) and hotel.status!="inactive":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        mobile = request.POST["mobile"]
        email = request.POST["email"]
        address = request.POST["address"]
        purpose_of_visit = request.POST["purpose"]
        no_of_adults = request.POST["no_of_adults"]
        sign = request.POST["sign"]
        no_of_children = request.POST["no_of_children"]
        idp = request.FILES.get("idp", False)
        idp_back = request.FILES.get("idp_back", False)
        selfi = request.FILES.get('selfi', False)
        nationality = request.POST["nationality"]
        passport_no = request.POST.get("passport_no", False)
        if nationality!="indian":
            date_of_issue = request.POST["date_of_issue"]
            date_of_expiry = request.POST["date_of_expiry"]
            date_of_arrival = request.POST["date_of_arrival"]
            date_of_issue_visa = request.POST["date_of_issue_visa"]
            date_of_expiry_visa = request.POST["date_of_expiry_visa"]
            
        else:
            date_of_issue = "1111-11-11"
            date_of_expiry ="1111-11-11"
            date_of_arrival = "1111-11-11"
            date_of_issue_visa = "1111-11-11"
            date_of_expiry_visa = "1111-11-11"
        employed_india = request.POST.get("employed_india", False)
        duration_in_india = request.POST.get("duration_in_india", False)
        visa_no = request.POST.get("visa_no", False)
             # idp3 = request.FILES.get("idpthree",False)
        name_list = [s[0] for s in hotel.property_name.split()]
       
        str_app = ""
        for i in name_list:
            str_app = str_app + i
        grc_num = str_app + str(quests + 1)

        try:
            customer_det = Checkin.objects.filter(mobile=mobile)[0] 
        except:
            customer_det = False

        if customer_det != False:

            hotel = HotelUsers.objects.get(hotel_user=user)
           
            customer = Checkin.objects.create(firstname=firstname,purpose_of_visit=purpose_of_visit,id_proof_back=customer_det.id_proof_back,grc_no=grc_num, lastname=lastname, hotel=hotel,email=email,
                    address=address,id_proof=customer_det.id_proof,no_of_adult=no_of_adults,nationality=nationality,passport_no=passport_no,date_of_issue=date_of_issue,date_of_expiry=date_of_expiry, no_of_children=no_of_children, 
                    duration_stay_india=duration_in_india,employed_india=employed_india,date_of_expiry_visa=date_of_expiry_visa,date_of_issue_visa=date_of_issue_visa,visa_no=visa_no,
                    date_of_arrival=date_of_arrival,selfi=selfi, mobile=mobile, status="waiting")

            
            customer.save()

            im = Image.open(io.BytesIO(base64.b64decode(sign.split(',')[1])))
            # buf = io.BytesIO(im)
            rgb_im = im.convert('RGB')
            img_io = io.BytesIO(base64.b64decode(sign.split(',')[1]))
            # rgb_im.save(rgb_im, format='JPEG')
            # img = decodeDesignImage(data)
            rgb_im.save('image.jpg')
            
            customer.signature = InMemoryUploadedFile(img_io, field_name=None, name=firstname + "signature"+".jpg", content_type='image/jpeg', size=img_io.tell, charset=None)
            customer.save()
            messages.success(request, "Successfully Registered")
            if int(no_of_adults)==1:
                return redirect('success')
            else:
                return render(request, 'checkin/checkin-otherdoc.html', {"profile": hotel.profile_photo, "prop_name":hotel.property_name, "customer":customer})
        else:
            hotel = HotelUsers.objects.get(hotel_user=user)
            customer = Checkin.objects.create(firstname=firstname, lastname=lastname,grc_no=grc_num, hotel=hotel,email=email,id_proof_back=idp_back,
                    address=address,id_proof=idp,nationality=nationality,passport_no=passport_no,date_of_issue=date_of_issue,date_of_expiry=date_of_expiry,
                    no_of_adult=no_of_adults, no_of_children=no_of_children, purpose_of_visit=purpose_of_visit,
                    selfi=selfi, mobile=mobile, status="waiting",duration_stay_india=duration_in_india,employed_india=employed_india,
                    date_of_expiry_visa=date_of_expiry_visa,date_of_issue_visa=date_of_issue_visa,
                    visa_no=visa_no,date_of_arrival=date_of_arrival)
            

            im = Image.open(io.BytesIO(base64.b64decode(sign.split(',')[1])))        
            # buf = io.BytesIO(im)
            rgb_im = im.convert('RGB')
            img_io = io.BytesIO(base64.b64decode(sign.split(',')[1]))
            # rgb_im.save(rgb_im, format='JPEG')
            # img = decodeDesignImage(data)
            rgb_im.save('image.jpg')
            
            customer.signature = InMemoryUploadedFile(img_io, field_name=None, name=firstname + "signature"+".jpg", content_type='image/jpeg', size=img_io.tell, charset=None)
            customer.save()

            messages.success(request, "Successfully Registered")
            if int(no_of_adults)==1:
                return redirect('success')
            else:
                return render(request, 'checkin/checkin-otherdoc.html', {"profile": hotel.profile_photo, "prop_name":hotel.property_name,"customer":customer})
    
    return render(request, 'checkin/checkin-form.html', {"username": user.username, "profile": hotel.profile_photo, "prop_name":hotel.property_name} )

#Checkin Completed 
def success(request):
    return render(request, 'success.html')

# To add other documents if the adults are more than one they need to upload thier Id card too
def other_documents(request, id):
    customer = Checkin.objects.get(id=id)
    if request.method=="POST":
        for i in range(1, int(customer.no_of_adult)):
            documents = request.FILES.get("document_"+str(i), False)
            documents_back = request.FILES.get("document_back_"+str(i), False)
            OtherDocuments.objects.create(checkins=customer,id_proofs=documents,id_proofs_back=documents_back)
        return redirect('success')
    return render(request, 'checkin/checkin-otherdoc.html')

# def signature(request):
#     data = "data:image/png;base64,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"

#     format, imgstr = data.split(';base64,') 
#     ext = format.split('/')[-1] 

#     data = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)
#     print(type(data))
#     return render(request, 'checkin/signature.html')


# Dashboard of the hotel who are using self checkin
def dashboard_hotel(request):
    try:
        current_user = request.user
        current_user.is_hotel
        hotel = HotelUsers.objects.get(hotel_user=current_user)
    except:
        messages.info(request,"Please login to your account")
        return redirect('hotel_login')
        
        
    if current_user.is_hotel == True and hotel.end_date >= timezone.make_aware(datetime.now()) and hotel.status!="inactive" and hotel.express_checkin == True:

        customer = Checkin.objects.filter(hotel=hotel).order_by('-id')

        month = datetime.now().month
        year = datetime.now().year
        number_of_days = calendar.monthrange(year, month)[1]
        first_date = date(year, month, 1)
        last_date = date(year, month, number_of_days)
        delta = last_date - first_date
        dates = [(first_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(delta.days + 1)]

        dates_start = datetime.strptime(dates[0]+ " 00:00:00", '%Y-%m-%d %H:%M:%S')
        dates_end = datetime.strptime(dates[-1]+ " 00:00:00",'%Y-%m-%d %H:%M:%S')
        # dates_1 = timezone.make_aware(dates_start)
        # dates_2 = timezone.make_aware(dates_end)

        this_month =[]
        today_reg = []
        total_reg = len(customer)
        for i in customer:
            if i.check_in >= dates_start.date() and i.check_in <= dates_end.date():
                this_month.append(i)
            if i.check_in == date.today():
                today_reg.append(i)
                
        this_month_reg = len(this_month)


        context = {"today_reg":len(today_reg),"this_month_reg":this_month_reg,"hotel":hotel, "total_reg":total_reg, "customer": customer}
        return render(request, 'checkin/dashboard.html', context=context)
    else:
        messages.error(request, "Not Allowed")
        return redirect('login_view')


#Login of checkin (not needed)
def login_view(request):
    if request.method == 'POST':
        # print("working")
        postdata = request.POST.copy()
        username = postdata.get('username', '')
        password = postdata.get('password', '')
        property_code = postdata.get('property_code', '')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            try:
                hotel = HotelUsers.objects.get(hotel_user=user)
                
            except:
                messages.error(request, "You are not a Hotel")
           
            #  and hotel.end_date>=timezone.make_aware(datetime.now())
            if hotel.property_code==property_code and user.is_hotel == True and hotel.express_checkin == True and hotel.end_date >= timezone.make_aware(datetime.now()):
                login(request, user)
                return redirect('dashboard_hotel')
            else:
                messages.error(request, "You are not allowed to login")
        else:
            messages.info(request,"Invalid credentials")

            return render(request,'login.html')
    return render(request,'login.html')

#The detailed view of view checkins
def detailed_view(request, id):
    try:
        current_user = request.user
        current_user.is_hotel
    except:
        messages.info(request,"Please login to your account")
        return redirect('login_view')
    if current_user.is_hotel==True:
        customer = Checkin.objects.get(id=id)
        other_doc = OtherDocuments.objects.filter(checkins=customer)
        return render(request, 'checkin/detailed_view.html',{"customer":customer, "other_doc":other_doc})


#print grc form of the guests
def print_customer(request, id):
    try:
        current_user = request.user
        current_user.is_hotel
    except:
        messages.info(request,"Please login to your account")
        return redirect('login_view')

    if current_user.is_hotel==True:
        customer = Checkin.objects.get(id=id)
        other_doc = OtherDocuments.objects.filter(checkins=customer)
        return render(request, 'checkin/grc.html',{"customer":customer,"other_doc":other_doc})

#To make date string
def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

#Aproving the check-in request
def approve(request, id):
    try:
        current_user = request.user
        current_user.is_hotel
    except:
        messages.info(request,"Please login to your account")
        return redirect('login_view')

    if current_user.is_hotel==True:
        if request.method=="POST":
            checkout = request.POST["checkout"]
            room = request.POST["room"]
            remark = request.POST["remark"]
            amount = request.POST["amount"]
            plan = request.POST["plan"]
            mode_of_payment = request.POST["mode_of_payment"]
            booking_agency = request.POST["booking_agency"]
            # date_str_value = str(checkout)
            # date_str = date_str_value.replace('T', ',')
            # date_str = date_str.replace('-',',')
            # date_str = date_str.replace(':',',')
            # # dt = datetime.datetime(date_str)
            # format_data = "%Y,%m,%d"
            # dt = datetime.strptime(date_str, format_data)
            # print(dt)
            customer_data =  Checkin.objects.get(id=id)

            if checkout:

                customer = Checkin.objects.filter(id=id).update(status="approved",check_in=date.today(), room=room, check_out=checkout,payment_type=mode_of_payment, booking_agency=booking_agency,plan=plan,amount=amount,remark=remark)
            else:
                customer = Checkin.objects.filter(id=id).update(status="approved",check_in=date.today(), room=room,payment_type=mode_of_payment, booking_agency=booking_agency,plan=plan,amount=amount,remark=remark)

            html_tpl_path = 'email/customer.html'

            context_data = {'customer': customer_data, "room":room, "checkout": checkout}
            email_html_template = get_template(html_tpl_path).render(context_data)

            email_msg = EmailMessage('Your Check-in is completed',
                                        email_html_template, 
                                        customer_data.hotel.property_name + "<noreply@hudels.com>",
                                        [customer_data.email],
                                        reply_to=[settings.APPLICATION_EMAIL]
                                        )
            # this is the crucial part that sends email as html content but not as a plain text
            if customer_data.hotel.whatsapp == True:
                sent_wtsp = SendWhatsapp(customer_data.mobile, "checkin_completed", customer_data.hotel.property_name, room,str(dumps(customer_data.check_in, default=json_serial)),str(dumps(customer_data.check_out, default=json_serial)), customer_data.hotel.mobile)
            with open(finders.find('images/logoheader.png'), 'rb') as f:
                logo = f.read()
            with open(finders.find('images/image-2.png'), 'rb') as f:
                tick = f.read()
            
            logoMime = MIMEImage(logo, 'png')
            tickMime = MIMEImage(tick, 'png')
            tickMime.add_header('Content-ID', '<tickMime>')
            logoMime.add_header('Content-ID', '<logoMime>')
            email_msg.attach(logoMime)
            email_msg.attach(tickMime)
            email_msg.content_subtype = 'html'

            email_msg.send(fail_silently=False)
            return redirect('dashboard_hotel')

#To reject the Checkin 
def reject(request, id):
    try:
        
        current_user = request.user
        current_user.is_hotel
    except:
        messages.info(request,"Please login to your account")
        return redirect('login_view')

    if current_user.is_hotel==True:
        Checkin.objects.filter(id=id).update(status="rejected")
        return redirect('dashboard_hotel')

#To edit guest details getting the guest details
def edit_customer(request, id):
    try:
        current_user = request.user
        current_user.is_hotel
    except:
        messages.info(request,"Please login to your account")
        return redirect('login_view')

    if current_user.is_hotel==True:
        customer = Checkin.objects.get(id=id)
        date = customer.check_in
        other_doc = OtherDocuments.objects.filter(checkins=customer)
        return render(request, 'checkin/edit_customer.html', {"customer": customer,"other_doc":other_doc, "hotel": customer.hotel})

# Update Guest details from the function
def edit_fun(request, id):
    try:
        
        current_user = request.user
        current_user.is_hotel
    except:
        messages.info(request,"Please login to your account")
        return redirect('login_view')

    if current_user.is_hotel==True:
        if request.method=="POST":
            firstname = request.POST["firstname"]
            lastname = request.POST["lastname"]
            mobile = request.POST["mobile"]
            email = request.POST["email"]
            address = request.POST["address"]
            checkout = request.POST["checkout"]
            checkin_date = request.POST["checkin"]
            grc_no = request.POST["grc_no"]
            no_of_adult = request.POST["no_of_adult"]
            room = request.POST["room"]
            remark = request.POST["remark"]
            plan = request.POST["plan"]
            booking_agency = request.POST["booking_agency"]
            no_of_children = request.POST["no_of_children"]
            purpose_of_visit=request.POST["purpose_of_visit"]
            idp = request.FILES.get("id_proof", False)
            idp_back = request.FILES.get("id_proof_back", False)
            selfi = request.FILES.get('selfi', False)

            checkin = Checkin.objects.get(id=id)
            other_doc = OtherDocuments.objects.filter(checkins=checkin)
            for i in other_doc:
                id_proofs =  request.FILES.get("id_proof"+str(i.id), False)
                id_proofs_back = request.FILES.get("id_proof_back"+str(i.id), False)
                if id_proofs:
                    i.id_proofs = id_proofs
                    i.save()
                if id_proofs_back:
                    i.id_proofs_back = id_proofs_back
                    i.save()
            if checkin.no_of_adult < int(no_of_adult):
                change = int(no_of_adult) - checkin.no_of_adult
                for i in range(1,change+1):
                    idp = request.FILES.get("idp"+str(i), False)
                    idp_back = request.FILES.get("idp_back"+ str(i), False)
                    OtherDocuments.objects.create(id_proofs=idp,id_proofs_back=idp_back,checkins=checkin)
            if idp!=True:
                customer = Checkin.objects.filter(id=id).update(room=room,purpose_of_visit=purpose_of_visit,grc_no=grc_no,check_out=checkout,check_in=checkin_date,remark=remark,
                plan=plan,booking_agency=booking_agency, firstname=firstname, lastname=lastname,
                mobile=mobile,email=email,id_proof=idp, address=address,no_of_adult=no_of_adult,
                no_of_children=no_of_children )
            if idp_back!=True:
                customer = Checkin.objects.filter(id=id).update(room=room,purpose_of_visit=purpose_of_visit,grc_no=grc_no,check_out=checkout,check_in=checkin_date,remark=remark,
                plan=plan,booking_agency=booking_agency, firstname=firstname, lastname=lastname,
                mobile=mobile,email=email,id_proof_back=idp_back, address=address,no_of_adult=no_of_adult,
                no_of_children=no_of_children )
            if selfi!=False:
                customer = Checkin.objects.filter(id=id).update(room=room,grc_no=grc_no,purpose_of_visit=purpose_of_visit,check_out=checkout,check_in=checkin_date,remark=remark,
                plan=plan,booking_agency=booking_agency, firstname=firstname, lastname=lastname,
                mobile=mobile,email=email,selfi=selfi, address=address,no_of_adult=no_of_adult,
                no_of_children=no_of_children )
            return redirect('dashboard_hotel')

#To logout the hotel admin
def logout_hotel(request):
    logout(request)
    return redirect('/')

# Profile of a user
def user_profile(request):
    try:
        
        current_user = request.user
        current_user.is_hotel
    except:
        messages.info(request,"Please login to your account")
        return redirect('login_view')

    hotel = HotelUsers.objects.get(hotel_user=current_user)
    return render(request,"checkin/user_profile.html", {"hotel":hotel})

#To update hotel profile 
def update_hotel_profile_express(request):
    try:
        
        current_user = request.user
        current_user.is_hotel
    except:
        messages.info(request,"Please login to your account")
        return redirect('login_view')

    if current_user.is_hotel==True:
        if request.method=="POST":
            name = request.POST["username"]
            firstname = request.POST["first_name"]
            lastname = request.POST["last_name"]
            email = request.POST["email"]
            property_name = request.POST["property_name"]
            website = request.POST["website"]
            mobile = request.POST["mobile"]
            location = request.POST["location"]
            

            try:
                profile_photo = request.FILES["profile_photo"]
            except:
                profile_photo= False
            User=get_user_model()
            if profile_photo:
                User.objects.filter(id=current_user.id).update(username=name, first_name=firstname, last_name=lastname, email=email, phone=mobile, profile_pic=profile_photo)
                hotel = HotelUsers.objects.filter(hotel_user=current_user).update(property_name=property_name,website=website, location=location)
            else:
                User.objects.filter(id=current_user.id).update(username=name, first_name=firstname, last_name=lastname, email=email, phone=mobile)
                hotel = HotelUsers.objects.filter(hotel_user=current_user).update(property_name=property_name,website=website, location=location)
            return redirect('dashboard_hotel')

#List of all check-ins
def total_checkin(request):
    try:
        
        current_user = request.user
        current_user.is_hotel
    except:
        messages.info(request,"Please login to your account")
        return redirect('login_view')

    if current_user.is_hotel==True:
        hotel = HotelUsers.objects.get(hotel_user=current_user)
        customer = Checkin.objects.filter(hotel=hotel).order_by('-id')
        return render(request, 'checkin/total_checkin.html', { "customer" : customer, "hotel" : hotel })
    else:
        return redirect("/")



#google qr rating (not using) 
def googlerating(request, id):

    property = GoogleQr.objects.get(id=id)
    if property.package == "filter" and property.end_date >= date.today() and property.status!="inactive" and property.status!="deactivated":
        if request.method=="POST":
            name = request.POST["name"]
            mobile = request.POST["mobile"]
            rating = request.POST["rating"]

            Ratings.objects.create(name=name, rating=rating, property=property, mobile=mobile)
            
            if int(rating) >= 4:
                return redirect("https://search.google.com/local/writereview?placeid="+property.place_id)
            else:
                return render(request,"checkin/regret.html", {"property":property})
           
                
        # return render(request, 'checkin/rating.html', { "property" : property })
        return render(request,"checkin/googlereviewpage.html", {"property":property})
    if property.package == "without_filter" and property.end_date >= date.today() and property.status!="inactive" and property.status!="deactivated":
        time.sleep(2)
        return redirect("https://search.google.com/local/writereview?placeid="+property.place_id)