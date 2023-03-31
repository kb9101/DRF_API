from django.db.models import fields
from rest_framework import serializers
from api.models import *
 
class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = ['company_name']

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ['first_name', 'last_name', 'company_id', 'email_address']