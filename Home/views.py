from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("harsh is here")
    return render(request,'Home/home.html')

def contact(request):
    return render(request,'Home/contact.html')
