from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from . import views

# Create your views here.
def home(request):
    return render(request, 'home.html')

def userAccounts(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'useraccounts.html', {'user': user})
