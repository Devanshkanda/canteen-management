from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#stalls modals
class Stall(models.Model):
    StallId = models.AutoField
    canteenStallName=models.CharField(max_length=50)
    StallDesc=models.CharField(max_length=20,default='')
    StallImg=models.ImageField(upload_to='StallImage',default='')
    url=models.CharField(max_length=50 ,default='')
    def __str__(self):
        return  self.canteenStallName

#products modals
class Product(models.Model):
    productId = models.AutoField
    StallName=models.ForeignKey( Stall,on_delete=models.CASCADE)
    StallName2=models.CharField(max_length=50 ,default='')
    productName=models.CharField(max_length=50, default='')
    productDesc=models.CharField(max_length=300, default='')
    category=models.CharField( max_length=50, default='')
    publishDate=models.DateField()
    price= models.IntegerField(default='')
    productImg=models.ImageField(upload_to="ProductImage" ,default="")
    
    def __str__(self):
        return  self.StallName2 + " " +self.productName


# order models

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transactionId=models.CharField(null=True, max_length=50)

    def __str__(self):
        return str(self.user) + " " + str(self.transactionId)
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)
    order =models.ForeignKey(Order,on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.product) +" "+str(self.order.user) +" "+str(self.date_added)
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    

STATUS_CHOICES = (
    ("Preparing", "Preparing"),
    ("Out for Delivery", "Out for Delivery"),
    ("Delivered", "Delivered"),
)
    
class DeliveryInfo(models.Model):
    customer=models.ForeignKey(User, on_delete=models.SET_NULL ,null=True)
    order =models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    email=models.CharField(default='', max_length=50)
    ClassNo=models.IntegerField(default='')
    Phone=models.IntegerField(default='')
    amount=models.IntegerField(default=0)
    status= models.CharField(
        max_length = 20,
        choices = STATUS_CHOICES,
        default = 'Preparing'
        )
    
    def __str__(self):
        return "class no: "+str(self.ClassNo)  + "Phone-no: " + str(self.Phone) + " order :  " + str(self.order)
    

