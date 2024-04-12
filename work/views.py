from django.shortcuts import render,HttpResponse
from datetime import datetime
from work.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    messages.success(request, "Data has worked in index sucessfully.")
    # return HttpResponse("This is home page")
    #context is used to pass set of variables primarily used to fetch and send data from modules
    context={
        'name':"Vasu varma"
    }
    return render(request,'index.html',context)
def about(request):
    # return HttpResponse("This is about page")
       return render(request,'about.html')
def services(request):
    # return HttpResponse("This is  services page")
       return render(request,'services.html')
def contact(request):
    if request.method== 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')
        ### creating object of data 
        contact= Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        
        
        ### To showcase the success message imported from message framework
        
        ##### saving this data in contact is done through
        contact.save()
        messages.success(request, "Data has been saved sucessfully.")
    # return HttpResponse("This is contact page")
    return render(request,'contact.html')


################################################
# Anything can be run using python manage.py shell
## provide database access with using from models.database import database
### perform operations such as  database.object.all() shows all objects in form of array 
