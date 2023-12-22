from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_name>/useraccounts/', views.home, name='useraccounts')
]