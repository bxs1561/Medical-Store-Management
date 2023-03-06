
from rest_framework import serializers

from DjangoMedicalApp.models import Company, CompanyBank,Medicine,MedicalDetails,Employee,Customer,CustomerRequest,Bill,BillDetails,CompanyAccount,EmployeeBank,EmployeeSalary


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields=["name","license_no","address","contact_no","email","description"]