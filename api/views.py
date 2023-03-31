from api.models import *
from api.serializers import *
from rest_framework import generics
from rest_framework.response import Response

class CompanyList(generics.ListAPIView):
    serializer_class = CompaniesSerializer
    queryset = Companies.objects.all()

class CompanyCreate(generics.CreateAPIView):
    serializer_class = CompaniesSerializer
    queryset = Companies.objects.all()

class CompanyUpdate(generics.UpdateAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Company Name Updated Successfully!"})

        else:
            return Response({"message": "failed", "details": serializer.errors})

class CompanyDelete(generics.DestroyAPIView):
    queryset = Companies.objects.all()
    serializer_class = CompaniesSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Company Deleted Successfully!"})

        else:
            return Response({"message": "failed", "details": serializer.errors})

class EmployeeList(generics.ListAPIView):
    serializer_class = EmployeesSerializer
    queryset = Employees.objects.all()

class EmployeeCreate(generics.CreateAPIView):
    serializer_class = EmployeesSerializer
    queryset = Employees.objects.all()

class EmployeeUpdate(generics.UpdateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Employee Updated Successfully!"})

        else:
            return Response({"message": "failed", "details": serializer.errors})
        
class EmployeeDelete(generics.DestroyAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Employee Successfully!"})

        else:
            return Response({"message": "failed", "details": serializer.errors})