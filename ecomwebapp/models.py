
from django.db import models
# importing user(user table) from admin or django.contrib.auth
from django.contrib.auth.models import User 
from django.core.validators import MaxValueValidator,MinLengthValidator

# Create your models here.
STATE_CHOICES = (
    ('Andaman & Nicobar Islands' , 'Andaman & Nicobar Islands'),
    ('Andhra Pradesh' , 'Andhra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chandigarh','Chandigarh'),
    ('Chhattisgarh' , 'Chhattisgarh'),
    ('Dadra & Nagar Haveli' , ' Dadra & Nagar Haveli' ),
    ('Daman and Diu' , 'Daman and Diu'),
    ('Delhi','Delhi'),
    ('Goa','Goa'),
    ('Gujarat','Gujarat' ),
    ('Haryana','Haryana'),
    ('Himachal Pradesh' , 'Himachal Pradesh'),
    ('Jammu & Kashmir' , ' Jammu & Kashmir'),
    ('Jharkhand','Jharkhand'),
    ('Karnataka','Karnataka'),
    ('Kerala','Kerala'),
    ('Lakshadweep' , ' Lakshadweep'),
    ('Madhya Pradesh' , 'Madhya Pradesh'),
    ('Maharashtra','Maharashtra'),
    ('Manipur','Manipur'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram','Mizoram' ),
    ('Nagaland', 'Nagaland'),
    ('Odisha','Odisha'),
    ('Puducherry', 'Puducherry'),
    ('Punjab','Punjab' ),
    ('Rajasthan', 'Rajasthan' ),
    ('Sikkim','Sikkim' ),
    ('Tamil Nadu', 'Tamil Nadu'),
    ('Meghalaya', 'Meghalaya'),
    ('Mizoram','Mizoram'),
    ('Nagaland', 'Nagaland' ),
    ('Odisha','Odisha' ),
    ('Puducherry','Puducherry'),
    ('Punjab','Punjab'),
    ('Rajasthan','Rajasthan'),
    ('Sikkim','Sikkim' ),
    ('Tamil Nadu' , 'Tamil Nadu' ),
    ('Telangana', 'Telangana'),
    ('Tripura','Tripura'),
    ('Uttarakhand', 'Uttarakhand'),
    ('Uttar Pradesh' , 'Uttar Pradesh'),
    ('West Bengal', 'West Bengal' ),

)

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    name = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES,max_length=50)

    def __str__(self):
        return str(self.id)

CATAGORY_CHOICES = (
    ('M', 'Mobile'),
    ('L', 'Laptop'),
    ('TW', 'Top Wear'),
    ('BW', 'Bottom Wear'),
)

class Product(models.Model):
    title = models.CharField(max_length = 255)
    selling_price = models.FloatField() 
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length = 255)
    catagoty = models.CharField(choices = CATAGORY_CHOICES,max_length = 2)
    stock = models.PositiveIntegerField()
    product_image = models.ImageField(upload_to = 'productimg')
    
    def __str__(self) :
        return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default =1)#it means either 0 or positive all numbers not negative anything.anf default vaule 1


    def __str__(self):
        return str(self.id)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
           

STATUS_CHOICES= (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel','Cancel')
)
class OrderPlaces(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE)
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField(default = 1)
    order_date = models.DateTimeField(auto_now_add = True)
    status = models.CharField(choices = STATUS_CHOICES,max_length = 255,default = 'Pending')
    razor_pay_order_id = models.CharField(max_length = 100 , null=True , blank=True)
    razor_pay_payment_id = models.CharField(max_length = 100 , null=True , blank=True)
    razor_pay_payment_signature = models.CharField(max_length = 100 , null=True , blank=True)


    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price







            
