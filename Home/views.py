from django.shortcuts import render,HttpResponse
from  .models import Contact
# Create your views here.
def home(request):
    # return HttpResponse("harsh is here")
    return render(request,'Home/home.html')

def contact(request):
    if request.method == 'POST':
        first_name = str(request.POST['firstname'])
        last_name = str(request.POST['lastname'])
        email = str(request.POST['email'])
        phone_no = str(request.POST['phone'])
        message = str(request.POST['message'])
        contact = Contact(first_name=first_name, last_name=last_name, email=email, phone_no=phone_no, message=message)
        contact.save()
    return render(request,'Home/contact.html')
