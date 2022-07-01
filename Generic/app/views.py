from django.shortcuts import render
from app.models import EmployeeModel
from app.serializers import EmployeeSerializer
from rest_framework import generics
# Create your views here.

class EmployeeListGenerics(generics.ListAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeCreateGenerics(generics.CreateAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailsGenerics(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeListCreateGenerics(generics.ListCreateAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeAllGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer        
