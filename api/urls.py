from django.urls import path
from api import views

urlpatterns = [
    path('', views.CompanyList.as_view()),
    path('create_company', views.CompanyCreate.as_view()),
    path('update_company/<int:id>', views.CompanyUpdate.as_view()),
    path('delete_company/<int:id>', views.CompanyDelete.as_view()),
    path('employee', views.EmployeeList.as_view()),
    path('create_employee', views.EmployeeCreate.as_view()),
    path('update_employee/<int:id>', views.EmployeeUpdate.as_view()),
    path('delete_employee/<int:id>', views.EmployeeDelete.as_view()),
]