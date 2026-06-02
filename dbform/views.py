from django.shortcuts import render
from .models import *         
from .forms import *

def login(request):
    context={
        'login_form':login_form()
    }
    if request.method=="POST":
       login_Form=login_form(request.POST)
       if login_Form.is_valid():
           login_Form.save()
    return render(request,'login.html',context)
         

# Create your views here.
