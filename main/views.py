from django.shortcuts import render, redirect
from .models import CreateMenuItem
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from pizza.settings import EMAIL_HOST_USER
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request, 'main/index.html')

def menu(request):
    items = CreateMenuItem.objects.all()
    return render(request, 'main/menu.html', {'items':items})



@login_required(login_url = '/login')
def contact(request):
    
    if request.method == "GET":
        form = ContactForm()
    else:
        
        form = ContactForm(request.POST)
        
        if form.is_valid() :
            
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message'] 
            from_email = form.cleaned_data['from_email']
            try:
                send_mail( subject , message + "--This order has been placed by this person " + from_email , from_email, ['hassandjango14@gmail.com'])
            except BadHeaderError:
                return HttpResponse("Invalid header found")
            return redirect('success')
    return render(request, 'main/email.html', {"form": form})

def success(request):
    return HttpResponse("Success")