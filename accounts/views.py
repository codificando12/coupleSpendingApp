from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from .forms import UserCreateForm,UserLoginForm



# Create your views here.
def signupaccount(request):
    if request.method == 'GET':
        return render(request, 'signupaccount.html', {'form': UserCreateForm})
    else:
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        try:
            validate_email(email)
        except ValidationError:
            return render(request, 'signupaccount.html', {'form': UserCreateForm, 'error': 'Please enter a valid email'})
        
        if User.objects.filter(email = email).exists():
            return render(request, 'signupaccout.html', {'form':UserCreateForm, 'error': 'Email already taken, please choose a new email or recover your password.'})
        if len(password1) < 8:
            return render(request, 'signupaccount.html', {'form': UserCreateForm, 'error':'Password too short. Password must be at least 8 characters'})
        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save
                login(request, user)
                return redirect('useraccounts', user_id=user.id)
            except IntegrityError:
                return render(request, 'signupaccount.html', {'form': UserCreateForm, 'error': 'Username already taken. Please choose a new username'})
        else:
            return render(request, 'signupaccount.html', {'form': UserCreateForm, 'error': 'Password did not match'})
        
def logoutaccount(request):
    logout(request)
    return redirect('home')

def loginaccount(request):
    if request.method == 'GET':
        return render(request, 'loginaccount.html', {'form': UserLoginForm})
    else:
        user = authenticate(request,username = request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'loginaccount.html', {'form': UserLoginForm(),
                                                         'error': 'Username and password not match'})
        else:
            login(request, user)
            return redirect('useraccounts', user_id=user.id)