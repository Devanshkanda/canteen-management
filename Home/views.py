from django.shortcuts import render,HttpResponse,redirect
from  .models import Contact,FamousItems
import hashlib as hashh
from django.contrib.auth  import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    # return HttpResponse("harsh is here")
    cou = FamousItems.objects.all()

    data = {
        'cous': cou
    }

    return render(request,'Home/home.html',data)

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



def search(request):
    return HttpResponse ('This is search')

#authentication api's

def SignUp(request):
    if request.method=="POST":
        # Get the post parameters
       
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['uname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        # check for errorneous input
         # check for errorneous input

        if not username.isalnum():
            messages.warning(request, " User name should only contain letters and numbers")
            return redirect('login')

        if (pass1!= pass2):
             messages.warning(request, " Passwords do not match")
             return redirect('login')

        if User.objects.filter(username = username).first():
            messages.warning(request, "This Username is already taken")
            return redirect('login')

        if User.objects.filter(email = email).first():
            messages.warning(request, "This Email is already taken")
            return redirect('login')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your account has been successfully created")
        return redirect('login')



def Login(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("login")

    return render(request,'Home/login.html')
   


def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')