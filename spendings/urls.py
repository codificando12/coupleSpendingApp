from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/useraccounts/', views.useraccounts, name='useraccounts'),
    path('<int:user_id>/useraccounts/personalSpendings', views.personalSpendings, name='personalSpendings'),
    path('<int:user_id>/useraccounts/createPersonalCategories', views.createPersonalCategories, name='createPersonalCategories'),
    path('<int:user_id>/useraccounts/personalSpendings/categories', views.categoriesView, name='categoriesView'),
    path('<int:user_id>/useraccounts/personalSpendings/<int:category_id>', views.updateCategory, name='updateCategory'),
    path('<int:user_id>/useraccounts/personalSpendings/<int:category_id>/delete', views.deleteCategory, name='deleteCategory'),
    path('<int:user_id>/useraccounts/addPersonalSpending', views.addPersonalSpending, name='addPersonalSpending'),
    path('<int:user_id>/useraccounts/personalSpendings/<int:spending_id>/delete-personal-spending', views.deletePersonalSpending, name='deletePersonalSpending'),
]