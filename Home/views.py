from django.shortcuts import render,HttpResponse,redirect
from  Home.models import Contact
from  Stall.models import Product
import hashlib as hashh
from django.contrib.auth  import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from Stall.utils import cartData


# Create your views here.
def home(request):
    #fetching cart items to display in header
    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems=data['cartItems']
    
    #to fetch  products 
    products = Product.objects.all()[:4]

    data = {
        'products': products ,'cartItems':cartItems,'items' :items ,'order' : order
    }

    return render(request,'Home/home.html',data)

def contact(request):
    #fetching cart items to display in header

    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems=data['cartItems']

    data = {
        'items' :items ,'order' : order,'cartItems':cartItems
    }
    #to send data to db
    if request.method == 'POST':
        first_name = str(request.POST['firstname'])
        last_name = str(request.POST['lastname'])
        email = str(request.POST['email'])
        phone_no = str(request.POST['phone'])
        message = str(request.POST['message'])
        cont = Contact(first_name=first_name, last_name=last_name, email=email, phone_no=phone_no, message=message)
        cont.save()
        messages.success(request, "Your response have been submitted")
    return render(request,'Home/contact.html',data)



def search(request):
    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems=data['cartItems']
    if request.method == 'GET':
        search = request.GET.get('search')

        if len(search)>20:
            item = Product.objects.none()
            messages.warning(request, "Sorry No Search Result Found ..")
            return render(request, 'Home/home.html')
        else:
            search_item_product = Product.objects.filter(productName__icontains = search)
            
            if search_item_product.count()==0:
                messages.warning(request, "Sorry No Search Result Found ..")
                return render(request, 'Home/home.html')
            
            # search_item_stallname = Product.objects.filter(StallName__icontains = search)
            print(search_item_product)
            item = {
                "productname" : search_item_product,'items' :items ,'order' : order,'cartItems':cartItems
            }
            
        return render(request, 'Home/search.html', item)
    else:
        return render(request, 'Home/home.html')

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