from django.shortcuts import render, redirect, HttpResponse
from .forms import RegistrationForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('/')
            

            
    else:
        form = RegistrationForm()

        args = {
            'form': form,
            
        }

        return render(request, 'main/register.html', args)