from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/useraccounts/', views.useraccounts, name='useraccounts')
]