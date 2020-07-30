from django.shortcuts import render
from .models import CreateMenuItem
# Create your views here.

def home(request):
    return render(request, 'main/index.html')

def menu(request):
    items = CreateMenuItem.objects.all()
    return render(request, 'main/menu.html', {'items':items})