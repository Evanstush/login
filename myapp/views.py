from django.shortcuts import render, redirect
from myapp.models import my_user
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from.forms import SignUpForm
from django import forms


# Create your views here.
def home(request):
    return render(request,'index.html')
def sign_up(request):
    if request.method == 'POST':
        user=my_user(
        username = request.POST['username'],
        email = request.POST['email'],
        password = request.POST['password'],
        )
        user.save()
        return redirect('login')
    else:
        return render(request,'sign_up.html')

def login_user(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'You are now logged in')
            return redirect('home')
        else:
            messages.error(request,'Invalid username or password')
            return redirect('login')
    else:
        return render(request,'login.html')
def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have registered successfully')
            return redirect('home')
        else:
            messages.error(request, 'oops!! there was an error')
            return redirect('register')
    else:
        return render(request,'register.html',{'form':form})





