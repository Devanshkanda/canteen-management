from django.db import models


from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    phone_no = PhoneNumberField(max_length=10)
    message = models.TextField(max_length=200)
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
          return "Message from " + self.first_name + ' - ' + self.email
    
