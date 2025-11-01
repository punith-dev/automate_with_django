from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistertionFrom
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth import logout as auth_logout, login as auth_login

def home(request):
    return render(request, 'home.html')

def celery_test(request):
    return HttpResponse('<h3>Successfully</h3>')

def register(request):
    if request.method == 'POST':
        form = RegistertionFrom(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registerstion successfully.')
            return redirect('register')
        else:
            context = {'form': form}
            return render(request, 'register.html', context)
    else:
        form = RegistertionFrom()
        context = {
            'form': form
        }
    return render(request, 'register.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user  = auth.authenticate(username=username, password=password)
            
            if user is not None:
                auth_login(request, user)
                return redirect('home')
        
        else:
            messages.error(request, 'Invalid username or password.')
        # else:
        #     # form invalid (e.g. missing fields) — AuthenticationForm will handle errors
        #     messages.error(request, 'Please correct the errors below')
        # Render the form again with errors
        context = {'form': form}
        return render(request, 'login.html', context)
    else:
        form = AuthenticationForm()
        context = {
            'form': form
        }
        return render(request, 'login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('home')