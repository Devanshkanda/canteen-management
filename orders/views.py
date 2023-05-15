from django.shortcuts import render,HttpResponse

# Create your views here.
def prodView(request):
    return HttpResponse ('This is prodView')

def tracker(request):
    return HttpResponse ('This is tracker')


def checkout(request):
    return HttpResponse ('This is checkout')

