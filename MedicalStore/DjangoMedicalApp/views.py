from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from DjangoMedicalApp.models import Company, CompanyBank
from DjangoMedicalApp.serializer import CompanySerializer, CompanyBankSerializer


class CompanyViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def list(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True, context={"request": request})
        response_dict = {"error": False, "message": "Company data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = CompanySerializer(data=request.data, context={"request": request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "Company Data saved success"}
        except:
            dict_response = {"error": True, "message": "Error"}
        return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = Company.objects.all()
            company = get_object_or_404(queryset, pk=pk)
            serializer = CompanySerializer(company, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "company data successfully updated"}

        except:
            dict_response = {"error": False, "message": "error updating"}
        return Response(dict_response)

class CompanyBankViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        company_bank = CompanyBank.objects.all()
        serializer = CompanyBankSerializer(company_bank, many=True, context={"request": request})
        response_dict = {"error": False, "message": "Company data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = CompanyBankSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Company bank Data saved success"}
        except:
            dict_response = {"error": True, "message": "Error"}
        return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = CompanyBank.objects.all()
            company_bank = get_object_or_404(queryset, pk=pk)
            serializer = CompanyBankSerializer(company_bank, data=request.data, context={"request": request})
            serializer.is_valid()
            serializer.save()
            dict_response = {"error": False, "message": "company bank data successfully updated"}

        except:
            dict_response = {"error": False, "message": "error updating"}
        return Response(dict_response)


company_get = CompanyViewSet.as_view({"get": "list"})
company_create = CompanyViewSet.as_view({"post": "create"})
company_update = CompanyViewSet.as_view({"put": "update"})
