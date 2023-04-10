from django.shortcuts import render,HttpResponse,redirect
from  .models import Contact
import hashlib as hashh
from django.contrib.auth  import authenticate, login, logout
from django.contrib import messages

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

def signup(request):
    if request.method == 'POST':
        try:
            uname = str(request.POST['uname'])
            email=str(request.POST['email'])
            fname=str(request.POST['fname'])
            lname=str(request.POST['lname'])
            pass1=str(request.POST['pass1'])
            pass2=str(request.POST['pass2'])

            # check for errorneous input
            if len(uname)<5:
                messages.warning(request, " Your user name must not be under 10 characters")
                return redirect('home')

            if not uname.isalnum():
                messages.warning(request, " User name should only contain letters and numbers")
                return redirect('home')

            if (pass1!= pass2):
                messages.warning(request, " Passwords do not match")
                return redirect('home')

            if User.objects.filter(uname = uname).first():
                messages.warning(request, "This Username is already taken")
                return redirect('home')

            if User.objects.filter(email = email).first():
                messages.warning(request, "This Email is already taken")
                return redirect('home')

            # adding salt to the password
            salt = "this@#is&a3#salt" # random complex string
            adding_salt_To_password = pass1+salt 

            # converting password into hashed digest
            hashed_pass = hashh.md5(adding_salt_To_password.encode()).hexdigest()

            # Create the user
            myuser = User.objects.create_user(uname, email, hashed_pass)
            myuser.first_name= fname
            myuser.last_name= lname
            myuser.save()
            messages.success(request, " Your Account has been successfully created")
            return redirect('home')

        except Exception as e:
            return HttpResponse("404 - Not found")

def Login(request):

    try:
        if request.method=="POST":
            # Get the post parameters
            loginusername=str(request.POST['loginusername'])
            loginpassword=str(request.POST['loginpassword'])

            # adding salt to the password
            salt = "this@#is&a3#salt" # random complex string
            adding_salt_To_password = loginpassword+salt
            
            # converting password into hashed digest
            hashed_pass = hashh.md5(adding_salt_To_password.encode()).hexdigest()

            # authenticating the user
            user=authenticate(username= loginusername, password= hashed_pass)
            print(user)
            if user is not None:
                login(request, user)
                messages.success(request, "Successfully Logged In")
                return redirect("home")
            else:
                messages.warning(request, "Invalid credentials! Please try again")
                return redirect("home")
            
    except Exception as e:
        return HttpResponse("404- Not found")

def handelLogout(request):
    logout(request)
    messages.success(request," Successfully logged out")
    return redirect('home')