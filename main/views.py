from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'main/index.html')

def menu(request):
    return render(request, 'main/menu.html')