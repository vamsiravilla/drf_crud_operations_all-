from urllib import response
from django.shortcuts import render
from app.models import Task
from app.serializers import Taskserializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

class Employee(APIView):
    def get(self,request):
        emp=Task.objects.all()
        serializer=Taskserializer(emp,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=Taskserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class EmployeeUpdate(APIView):
    def get(self,request,pk):
        emp=Task.objects.get(id=pk)
        serializers=Taskserializer(emp)
        return Response(serializers.data) 

    def put(self,request,pk):
        emp=Task.objects.get(id=pk)
        serializers=Taskserializer(instance=emp,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        emp=Task.objects.get(id=pk)
        emp.delete()
        return Response("Deleted sucessfully...........")                           

                                                                                                                                                     
