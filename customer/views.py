from django.shortcuts import render, redirect
from datetime import date, timedelta,datetime


from restaurant.models import RestaurantUser
import restaurant
from .models import Customer
from hotel.models import HotelUsers
# from sales_executive.serializers import CustomerSerializer
from django.http import Http404, HttpResponse, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
import requests
import time
from threading import Event
from email.mime.image import MIMEImage
from django.contrib.staticfiles import finders
from django.core.mail import EmailMessage
import json
import os
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import datetime
from rest_framework import permissions
from io import BytesIO  #basic input/output operation
from django.core.files.base import ContentFile
from PIL import Image
from io import StringIO #Imported to compress images
from django.core.files import File #to store files
import urllib.request
import urllib.parse
 
def sendSMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'sender': sender, 'test': True})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)
 
# resp =  sendSMS('apikey', '918123456789',
#     'Jims Autos', 'This is your message')
# print (resp)



# Index page
def index(request):
    # res = sendSMS('NDk2ZDY3NzI2YjRiMzI3YTM5Nzg1NjYzNTI0MzM1MzE=', '917561071623','Jims Autos', 'This is your message')
    # print(res)
    # SendWhatsapp("919739506060", "hello_world")
    return render(request, "index.html")

# Contact us in index page
def contact_us(request):
    if request.method=="POST":
        name = request.POST["name"]
        mobile = request.POST["mobile"]
        email = request.POST["email"]
        location = request.POST["location"]

        email_msg = EmailMessage('Enquiry From ' + str(name),
                                            "Name :"+ name+ "  \nMobile :"+ mobile+"  \nEmail :" +email+ "  \nLocation : "+location , 
                                            "  \nContact" + "<noreply@hudels.com>",
                                            ["sales@hudels.com"],
                                            reply_to=[settings.APPLICATION_EMAIL]
                                            )
        email_msg.send(fail_silently=False)
       
        # NDk2ZDY3NzI2YjRiMzI3YTM5Nzg1NjYzNTI0MzM1MzE=	
        return redirect("index")


# Rating function 
def rate(request, username):

    User = get_user_model()
    user = User.objects.get(username=username)
    hotel = HotelUsers.objects.get(hotel_user=user)

    if hotel.end_date >= timezone.make_aware(datetime.now()) and hotel.status=="Active" and hotel.other==True:
        if request.method=="POST":
            name = request.POST["name"]
            mobile = request.POST["mobile"]
            rating = request.POST["rating"]
            if hotel.without_filter == False and hotel.inhouse != True and hotel.without_email == False:
                email = request.POST["email"]
                facebook = request.POST["facebook"]
                id_x = request.POST["id_x"]
                id_y = request.POST["id_y"]
                review = request.POST["review"]
                id_height = request.POST["id_height"]
                id_width = request.POST["id_width"]
                text_review = request.POST["text_review"]
                image = request.FILES.get("image", False)
                video = request.FILES.get("video", False)
                imagecaption = request.POST["imagecaption"]
                videocaption = request.POST["videocaption"]
                
                if imagecaption:
                    caption = imagecaption
                else:
                    caption = videocaption

            if hotel.inhouse:
                email = request.POST["email"]
                title_review = request.POST["title_review"]
                review = request.POST["review"]
                triptype = request.POST.get("triptype", False)
                checkin = request.POST.get("checkin", False)
                date = request.POST.get("date", False)
                laundry = request.POST.get("laundry", False)
                breakfast = request.POST.get("breakfast", False)
                classic = request.POST.get("classic", False)
                bar = request.POST.get("bar", False)
                business = request.POST.get("business", False)
                service = request.POST.get("rating1", False)
                room = request.POST.get("rating2", False)
                clean = request.POST.get("rating3", False)
                expensive = request.POST.get("expensive", False)

                customer = Customer.objects.create(classic=classic,business=business,room=room,clean=clean,service=service,expense=expensive,bar_or_lounge=bar,breakfast=breakfast,loaundry=laundry,date=date,contactless_checkin=checkin,trip_type=triptype,name=name,review=review, title_review=title_review,email= email, ratings=rating, hotel=hotel, phone_number=mobile)

            if hotel.without_filter and hotel.google:
                customer = Customer.objects.create(name=name,ratings=rating, hotel=hotel, phone_number=mobile)
                return redirect("https://search.google.com/local/writereview?placeid="+hotel.google_link)
            
            else:
                if hotel.inhouse != True and hotel.without_email != True:
                    customer = Customer.objects.create(name=name,review=review, images=image, text_review=text_review, video=video,email= email,instagramid=caption,facebookid=facebook, ratings=rating, hotel=hotel, phone_number=mobile)
                
                if hotel.without_email == True:
                    customer = Customer.objects.create(name=name,ratings=rating,phone_number=mobile)

                if int(rating) < 4 and hotel.inhouse != True:
                    html_tpl_path = 'email/apology_email.html'
                    context_data = {'hotel': hotel, "name":name}
                    email_html_template = get_template(html_tpl_path).render(context_data)
                    email_msg = EmailMessage('Thank you for your review',
                                                email_html_template, 
                                                hotel.property_name + "<noreply@hudels.com>",
                                                [email],
                                                reply_to=[settings.APPLICATION_EMAIL]
                                                )
                    # this is the crucial part that sends email as html content but not as a plain text

                    email_msg.content_subtype = 'html'
                    
                    email_msg.send(fail_silently=False)
                    # email_msg.send(fail_silently=False)
                   

                    return render(request,"customer/regret.html", {"hotel":hotel})
                
                if hotel.social_media==True:
                    if image!=False:
                        im = Image.open(image)
                        cropped_image = im.crop((float(id_x), float(id_y), float(id_width)+float(id_x), float(id_height)+float(id_y)))
                        # resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
                        cropped_image = cropped_image.convert("RGB")
                        output_file = BytesIO()
                        cropped_image.save(output_file, "JPEG", quality=200)
                        customer.images.save(name+".jpg", ContentFile(output_file.getvalue()), save=False)
                        
                        customer.save()
                    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
                    access_token = str(hotel.facebook_access_token)
                    insta_id = hotel.insta_id
                    page_id = str(hotel.page_id)
                    request_page = requests.get("https://graph.facebook.com/" + page_id+"?fields=access_token&access_token="+ access_token)
                    page_data = request_page.json()
                    page_access_token = page_data.get("access_token")
                    if int(rating) >= 4:
                        if customer.images:
                            image_url = customer.images.url

                            url = "https://graph.facebook.com/"+ insta_id+"/media"
                            
                            data = {'image_url': image_url, 'caption': caption+" "+ hotel.default_caption if hotel.default_caption else "", 'access_token': access_token}
                            data2 = {'url': image_url, 'access_token': page_access_token}
                            url2 = "https://graph.facebook.com/"+ page_id +"/photos"

                            respose_post2 = requests.post(url2, data=json.dumps(data2), headers=headers)
                            response = requests.post(url, data=json.dumps(data), headers=headers)

                            if response.status_code == 200:
                                container = response.json()
                                time.sleep(5)
                                container_id = container.get("id")

                                url = "https://graph.facebook.com/"+ insta_id+"/media_publish"
                                data3 = {'creation_id': container_id, 'access_token': access_token}
                                respose_post = requests.post(url, data=json.dumps(data3), headers=headers)
                                customer.review_method = "Image"
                                customer.save()

                        if customer.video:
                        
                            video_url = customer.video.url
                            # video_url = "https://socioconnects.herokuapp.com/media/vid/WhatsApp_Video_2022-03-07_at_12.03.58.mp4"
                            insta_data = {"media_type": "VIDEO","video_url": video_url,"caption": caption+" "+ hotel.default_caption, "access_token": access_token}      
                            url_insta = "https://graph.facebook.com/"+str(insta_id)+"/media"
                            insta_post = requests.post(url_insta, data=json.dumps(insta_data), headers=headers)
                            video_upload_url = "https://graph-video.facebook.com/v13.0/"+ str(page_id) + "/videos"
                            video_data = {"file_url": video_url, "access_token": page_access_token}
                            response_video = requests.post(video_upload_url, data=json.dumps(video_data), headers=headers)


                            if insta_post.status_code == 200:
                                time.sleep(10)
                                container = insta_post.json()

                                container_id = container.get("id")

                                data_publish = {'creation_id': container_id, 'access_token': access_token}
                                insta_url = "https://graph.facebook.com/"+ str(insta_id)+"/media_publish"
                                insta_publish = requests.post(insta_url, data=json.dumps(data_publish), headers=headers)
                                customer.review_method = str(customer.review_method) + "Video"
                                customer.save()

                        if customer.text_review:
                            url = "https://graph.facebook.com/" + str(page_id) + "/feed"
                            data = {'message': text_review, 'access_token': page_access_token}
                            response = requests.post(url, data=json.dumps(data), headers=headers)
                            customer.review_method = str(customer.review_method) + " Text"
                            customer.save()
                
                
                if hotel.google:
                    if int(rating) >= 4:
                        return redirect("https://search.google.com/local/writereview?placeid="+hotel.google_link)
                
                if hotel.trip_adviser:
                    if int(rating) >= 4:
                        return redirect(hotel.trip_adviser_link)
                
                if hotel.g_t:
                    if int(rating) >=4:
                        html_tpl_path = 'email/Tripadvisor-review-template.html'
                        domain = request.build_absolute_uri('/')[:-1]

                        trip_url = str(domain) + "/email_click/" + str(customer.id)
                        context_data = {'hotel': hotel, "name":name, "trip_url":trip_url}
                        email_html_template = get_template(html_tpl_path).render(context_data)

                        email_msg = EmailMessage('Rate us on Trip Adviser',
                                                    email_html_template, 
                                                    hotel.property_name + "<noreply@hudels.com>",
                                                    [email],
                                                    reply_to=[settings.APPLICATION_EMAIL]
                                                    )
                        # this is the crucial part that sends email as html content but not as a plain text
                        with open(finders.find('images/tripadvisor.png'), 'rb') as f:
                            logo = f.read()
                        
                        logoMime = MIMEImage(logo, 'png')
                    
                        
                        logoMime.add_header('Content-ID', '<logoMime>')
                        email_msg.attach(logoMime)
                        
                        email_msg.content_subtype = 'html'
                        
                        email_msg.send(fail_silently=False)

                    
                        return redirect("https://search.google.com/local/writereview?placeid=" + hotel.google_link)
                        

                if hotel.t_g:
                    if int(rating) >=4:
                        html_tpl_path = 'email/google-review-template.html'
                        domain = request.build_absolute_uri('/')[:-1]
                        googlelink = str(domain) + "/email_click/" + str(customer.id)

                        context_data = {'hotel': hotel, "googlelink":googlelink, "name": name}
                        email_html_template = get_template(html_tpl_path).render(context_data)

                        email_msg = EmailMessage('Rate us on Google',
                                                    email_html_template, 
                                                    hotel.property_name + "<noreply@hudels.com>",
                                                    [email],
                                                    reply_to=[settings.APPLICATION_EMAIL]
                                                    )
                        # this is the crucial part that sends email as html content but not as a plain text
                        with open(finders.find('images/googlereviewimg.png'), 'rb') as f:
                            logo = f.read()

                        logoMime = MIMEImage(logo, 'png')
                            
                        logoMime.add_header('Content-ID', '<logoMime>')
                        email_msg.attach(logoMime)
                        email_msg.content_subtype = 'html'
                        email_msg.send(fail_silently=False)
                        return redirect(hotel.trip_adviser_link)
            # return render(request, 'checkin/rating.html', { "property" : property })
                return render(request,"customer/regret.html", {"hotel":hotel})
        if hotel.inhouse == True:
            return render(request,"customer/inhouse-review-form.html", {"hotel":hotel})
        else:
            return render(request,"customer/rate.html", {"hotel":hotel})

# To check whether the link is clicked which is sent through mail
def email_click(request, id):
    customer = Customer.objects.get(id=id)
    Customer.objects.filter(id=id).update(status=True)
    if customer.hotel.t_g:
        return redirect("https://search.google.com/local/writereview?placeid=" + customer.hotel.google_link)
    if customer.hotel.g_t:
        return redirect(str(customer.hotel.trip_adviser_link))






#======================  Restaurant =========================

def restaurant_menucard(request,username,tableno):

    restaurant=RestaurantUser.objects.get(username=username)

    tableno=tableno


    return render(request, "customer/restaurant_menucard.html",{"rest":restaurant,"tableno":tableno})


def restaurant_card(request,tableno):

    tableno=tableno
    print("tableno :",tableno)

    return redirect('restaurant_menucard')