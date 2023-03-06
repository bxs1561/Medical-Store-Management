from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from DjangoMedicalApp.models import Company
from DjangoMedicalApp.serializer import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
