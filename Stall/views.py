from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from Stall.models import Stall,Product,Order,OrderItem,DeliveryInfo
from django.http import JsonResponse
import json
from django.contrib import messages
import datetime
from .utils import cartData

# Create your views here.
def Stalls(request):
    #fetching cart items to display in header

    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems=data['cartItems']

    #to fetch stalls
    stalls = Stall.objects.all()

    context = {'stalls':stalls,'cartItems':cartItems,'items' :items ,'order' : order}

    return render(request,'stall/restaurantView.html',context)

def Menu(request,url):
    #fetching cart items to display in header

    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems=data['cartItems']

    
   # To fetch products 
    StallName=Stall.objects.get(url=url)
    food=Product.objects.filter(StallName=StallName)
    context2 = {
        'StallName': StallName,
        'food':food,  
        'cartItems':cartItems,
        'items' :items ,
        'order' : order
    }
    return render(request,'Stall/MenuView.html',context2)




def cart(request):
    #fetching cart items to display in header & cart

    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems=data['cartItems']
    context={'items' :items ,'order' : order,'cartItems':cartItems}
    return render(request,'stall/cart.html',context)


def updateItem(request):
    if request.method == 'POST':
        # Get the incoming JSON Data
        d = request.body.decode('utf-8')
        data = json.loads(d)
        productId = data['productId']
        action = data['action']

        print('Action:',action)
        print('ProductId:',productId)

        customer = request.user
        product = Product.objects.get(id = productId)

        order , created = Order.objects.get_or_create(user=customer,complete=False)

        orderItem, created =OrderItem.objects.get_or_create(order=order,product=product)

        if action=='add':
            orderItem.quantity = (orderItem.quantity +1)
        elif action=='remove':
            orderItem.quantity = (orderItem.quantity -1)
        orderItem.save()

        if action=='remove-item':
            orderItem.delete()

        if  orderItem.quantity <= 0:
            orderItem.delete()



    return JsonResponse ('item was added' ,safe=False)


def checkout(request):
    #fetching cart items to display in header & checkout page

    data = cartData(request)
    items = data['items']
    order = data['order']
    cartItems=data['cartItems']
    context={'items' :items ,'order' : order,'cartItems':cartItems}
    return render(request, 'stall/checkout.html',context) 


def processOrder(request):
    transaction_id=datetime.datetime.now().timestamp()
    data=json.loads(request.body)

    if request.user.is_authenticated:
        customer=request.user
        order,created =Order.objects.get_or_create(user = customer ,complete =False)
        total = int(data['form']['total'])
        order.transactionId =transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        DeliveryInfo.objects.create(
            customer=customer,
            order=order,
            email=data['form']['email'],
            ClassNo=data['form']['room'],
            Phone=data['form']['phone'],
        )

    else:
        messages.warning(request, "User is Not Logged In")


    return JsonResponse ('Payment Complete' ,safe=False)

