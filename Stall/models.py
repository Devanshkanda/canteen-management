from django.db import models

# Create your models here.
#stalls modals
class Stall(models.Model):
    StallId = models.AutoField
    canteenStallName=models.CharField(max_length=50)
    StallDesc=models.CharField(max_length=20,default='')
    StallImg=models.ImageField(upload_to='StallImage',default='')
    Url=models.CharField(max_length=50 ,default='')
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
