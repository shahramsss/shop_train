import email
from urllib import request
from django import forms
from django.shortcuts import redirect, render , HttpResponseRedirect
from .froms import UserLoginForm , UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from .models import User


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['email'], password=cd['password'])
            if user is not None:
                login(request , user)
                messages.success(request, 'you logged in successfully', 'success')
                return redirect('shop:home')
            else:
                messages.error(
                    request, 'email or password is wwrong', 'danger')
    else:
        form = UserLoginForm()
    return render(request, "accounts/login.html", {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'you are logged out', 'success')
    return redirect("accounts:login")
    

def user_register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if  cd['confirm_password'] and  cd['password'] and  cd['confirm_password']!= cd['password']:
                messages.error(request, "Passwords don't match", 'danger')
                return redirect('accounts:register')

            user = User.objects.create_user(email = cd['email'], full_name = cd['full_name'], phone = cd['phone'] , password = cd['confirm_password'])
            user.save()
            messages.success(request, 'you registered successfully', 'success')
            return redirect('accounts:login')
    else:
        form = UserRegisterForm()
    return render(request , 'accounts/register.html', {'form':form})
