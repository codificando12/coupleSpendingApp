from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from . import views
from .models import PersonalSpending, Categories
from .forms import CategoryForm
from django.db.models import Sum

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
    year = request.GET.get('year', None)
    total_amount = sum(spendings.spendingAmount for spendings in allSpendings)
    if month:
        # Filtra los gastos por el mes especificado y el usuario
        allSpendings = allSpendings.filter(
            spendingDate__month=month
        )
        total_amount = sum(spendings.spendingAmount for spendings in allSpendings)
    if year:
        allSpendings = allSpendings.filter(
            spendingDate__year = year
        )
        total_amount = sum(spendings.spendingAmount for spendings in allSpendings)
    if 'show_all' in request.GET:
        allSpendings = PersonalSpending.objects.filter(user=user)
        total_amount = sum(spendings.spendingAmount for spendings in allSpendings)
    return render(request, 'personalSpendings.html', {'user': user, 'allSpendings': allSpendings, 'selectedMonth': month, 'total_amount': total_amount})

def createPersonalCategories(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'GET':
        return render(request, 'createpersonalcategory.html', {'form': CategoryForm(), 'user': user})
    else:
        try:
            form = CategoryForm(request.POST)
            new_category = form.save(commit=False)
            new_category.user = request.user
            new_category.save()
            return redirect('categoriesView', user_id=user_id)
        except ValueError:
            return render(request, 'createpersonalcategory.html', {'form': CategoryForm(), 
                                                                   'error': 'Bad data passed in. Try again.', 
                                                                   'user': user})
        
def categoriesView(request, user_id):
    user = get_object_or_404(User, pk=user_id)

    categories = Categories.objects.filter(personalspending__user=user).distinct()
    total_by_category = {}

    for category in categories:
        total = PersonalSpending.objects.filter(user=user, category=category).aggregate(Sum('spendingAmount')).get('spendingAmount__sum') or 0
        total_by_category[category] = total
    return render(request, 'categories.html', {'user': user, 'total_by_category': total_by_category})

def updateCategory(request, category_id, user_id):
    updateCategory = get_object_or_404(Categories, pk=category_id)
    if request.method == 'GET':
        form = CategoryForm(instance= updateCategory)
        return render(request, 'updatecategory.html', {'form': form, 'category': updateCategory})
    else:
        try:
            form = CategoryForm(request.POST, instance=updateCategory)
            form.save()
            return redirect('categoriesView', user_id=request.user.id)
        except ValueError:
            return render(request, 'updatecategory.html', {'form': form, 'category': updateCategory, 'error': 'Bad data in form'})

def deleteCategory(request, category_id, user_id):
    category = get_object_or_404(Categories, pk=category_id, user=request.user)
    category.delete()
    return redirect('categoriesView', user_id=user_id)

