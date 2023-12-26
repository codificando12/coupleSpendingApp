from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from . import views
from .models import PersonalSpending

# Create your views here.
def home(request):
    return render(request, 'home.html')

def useraccounts(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'useraccounts.html', {'user': user})

def personalSpendings(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    allSpendings = PersonalSpending.objects.filter(user=user)
    month = request.GET.get('month', None)
    total_amount = sum(spendings.spendingAmount for spendings in allSpendings)
    if month:
        # Filtra los gastos por el mes especificado y el usuario
        allSpendings = allSpendings.filter(
            spendingDate__month=month
        )
        total_amount = sum(spendings.spendingAmount for spendings in allSpendings)
    if 'show_all' in request.GET:
        allSpendings = PersonalSpending.objects.filter(user=user)
        total_amount = sum(spendings.spendingAmount for spendings in allSpendings)
    return render(request, 'personalSpendings.html', {'user': user, 'allSpendings': allSpendings, 'selectedMonth': month, 'total_amount': total_amount})


