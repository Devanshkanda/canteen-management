from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from Stall.models import Stall,Product,Order,OrderItem,DeliveryInfo
from django.http import JsonResponse
import json
# Create your views here.
def Stalls(request):
    stalls = Stall.objects.all()

    context = {'stalls':stalls}

    return render(request,'Stall/restaurantView.html',context)

def Menu(request,url):
   # To fetch products 
    StallName=Stall.objects.get(url=url)
    food=Product.objects.filter(StallName=StallName)
    context2 = {
        'StallName': StallName,
        'food':food,  
    }
    return render(request,'Stall/MenuView.html',context2)




def cart(request):
    if request.user.is_authenticated:
        customer =request.user
        order,created =Order.objects.get_or_create(user = customer ,complete =False)
        items =order.orderitem_set.all()
    else:
        items =[]
        order ={'get_cart_total':0,'get_cart_items':0}
    context={'items' :items ,'order' : order}
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

        if  orderItem.quantity <= 0:
            orderItem.delete()



    return JsonResponse ('item was added' ,safe=False)


def checkout(request):
    return render(request, 'stall/checkout.html') 

