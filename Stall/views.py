from django.shortcuts import render,HttpResponse
from Stall.models import Stall,Product
# Create your views here.
def Stalls(request):
    stalls = Stall.objects.all()

    context = {'stalls':stalls}

    return render(request,'Stall/restaurantView.html',context)

def Menu(request,url):
   
    StallName=Stall.objects.get(url=url)
    food=Product.objects.filter(StallName=StallName)
    context2 = {
        'StallName': StallName,
        'food':food,
    }
    return render(request,'Stall/MenuView.html',context2)

def tracker(request):
    return HttpResponse ('This is tracker')


def checkout(request):
    return HttpResponse ('This is checkout')

