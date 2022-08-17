from django.db import models

from hotel.models import HotelUsers

# Create your models here.
ApproveStatus = (
    ("approved", "Approved"),
    ("rejected", "Reject"),
    ("waiting", "Waiting for Approval")
)

Package = (
    ("filter", "Filter"),
    ("without_filter", "Without Filter"),
   
)
ActiveStatus = (
    ("active", "Active"),
    ("inactive", "Inactive"),
    ("deactivated", "Deactivated"),
    ("waiting", "Waiting for Approval")
)

class Checkin(models.Model):
    grc_no = models.CharField(max_length=50, null=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    hotel = models.ForeignKey(HotelUsers, on_delete=models.CASCADE)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=200)
    id_proof = models.ImageField(upload_to='document')
    id_proof_back = models.ImageField(upload_to='document', null=True)
    id_proof_1 = models.ImageField(upload_to='document')
    id_proof_2 = models.ImageField(upload_to='document')
    id_proof_3 = models.ImageField(upload_to='document')
    # other_doc = models.ImageField(upload_to='document')
    nationality = models.CharField(max_length=50, null=True)
    payment_type = models.CharField(max_length=50, null=True)
    passport_no = models.CharField(max_length=100, null=True)
    date_of_issue = models.DateField(null=True, blank=True)
    date_of_expiry = models.DateField(null=True, blank=True)
    date_of_arrival = models.DateField(null=True, blank=True)
    visa_no = models.CharField(max_length=100, null=True)
    date_of_expiry_visa = models.DateField(null=True, blank=True)
    date_of_issue_visa = models.DateField(null=True, blank=True)
    employed_india = models.BooleanField(null=True)
    duration_stay_india = models.CharField(max_length=50, null=True)
    check_in = models.DateField(auto_now_add=True)
    check_out = models.DateField(null=True)
    no_of_adult = models.IntegerField()
    room = models.CharField(max_length=20, null=True)
    no_of_children = models.IntegerField()
    remark = models.CharField(max_length=200, null=True)
    amount = models.FloatField(null=True)
    plan = models.CharField(max_length=200, null=True)
    booking_agency = models.CharField(max_length=50, null=True)
    selfi = models.ImageField(upload_to='media/selfi')
    mobile = models.CharField(max_length=15)
    status = models.CharField(choices=ApproveStatus, max_length=20, null=True)
    signature = models.ImageField(upload_to='media/sign')
    purpose_of_visit = models.CharField(max_length=70, null=True)

    class Meta:
        ordering = ('-id',)

class OtherDocuments(models.Model):

    id_proofs = models.FileField(upload_to='document')
    id_proofs_back = models.FileField(upload_to='document', null=True)
    checkins = models.ForeignKey(to=Checkin, on_delete=models.CASCADE)

# google QR model
class GoogleQr(models.Model):

    qr_code = models.ImageField(upload_to='qr')
    link = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    name = models.CharField(max_length=20)
    mobile = models.CharField(max_length=12)
    start_date = models.DateField(auto_now_add=True)
    place_id = models.CharField(max_length=200)
    duration = models.IntegerField()
    end_date = models.DateField(null=True)
    status = models.CharField(choices=ActiveStatus, max_length=20, null=True)
    package = models.CharField(choices=Package, max_length=20, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=50, null=True)
    amount = models.CharField(max_length=50, null=True)
    agreement = models.FileField(upload_to="media", null=True)
    new = models.CharField(null=True, max_length=10)

#     def save(self,*args,**kwargs):
#         qrcode = segno.make('JULIA')
# # Save the QR code with transparent background and use dark blue for
# # the dark modules
#         out = io.BytesIO()
#         qrcode.save(out, kind='png', dark='#00008b', light=None, scale=10)
        
#         self.qr_code.save('JULIA.png', ContentFile(out.getvalue()), save=False)
        
        

class Ratings(models.Model):

    name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=12, null=True)
    rating = models.IntegerField()
    property = models.ForeignKey(GoogleQr,null=True, on_delete=models.SET_NULL)