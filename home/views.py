from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    # messages.success(request,"thi is a text")
    return render(request,'index.html')
    # return HttpResponse('hello')

def about(request):
    return render(request,'about.html')
    # return HttpResponse('Aout')

def home(request):
    context={
        'variable':'A'
    }
    
    return render(request,'index.html',context)

def services(request):
    return render(request,'services.html')

def order(request):
    return render(request,'order.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('mailname')
        description = request.POST.get('desc')
        contact = Contact(name = name, email =email , description = description , date=datetime.today())
        contact.save()
        messages.success(request, 'ur msg has been sent!!!')
    return render(request,'contact.html')
