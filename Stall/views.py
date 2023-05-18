from django.shortcuts import render,HttpResponse
from Stall.models import Stall
# Create your views here.
def Menu(request):
    return HttpResponse ('This is Menu')

def Stalls(request):
    stalls = Stall.objects.all()

    context = {'stalls':stalls}

    return render(request,'Stall/restaurantView.html',context)

def tracker(request):
    return HttpResponse ('This is tracker')


def checkout(request):
    return HttpResponse ('This is checkout')

