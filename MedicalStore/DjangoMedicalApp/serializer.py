from rest_framework import serializers

from DjangoMedicalApp.models import Company, CompanyBank, Medicine, MedicalDetails, Employee, Customer, CustomerRequest, \
    Bill, BillDetails, CompanyAccount, EmployeeBank, EmployeeSalary


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class CompanyBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBank
        fields = "__all__"
