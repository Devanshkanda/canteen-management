from django.db import models

# Create your models here.
class Product(models.Model):
    product_id =models.AutoField
    canteenStall_name=models.CharField(max_length=50, default="")
    product_name=models.CharField(max_length=50, default="")
    product_desc=models.CharField(max_length=300, default="")
    category=models.CharField( max_length=50, default="")
    publish_date=models.DateField()
    price= models.IntegerField(default="0")
    product_img=models.ImageField(upload_to="ProductImage" ,default="")
    def __str_(self):
        return self.product_name