from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import EmployeeModel
from app.serializers import EmployeeSerializer
from rest_framework import status


# Create your views here.
@api_view(['GET'])
def taskList(request):
    task = EmployeeModel.objects.all()
    serializers = EmployeeSerializer(task,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def taskDetails(request,pk):
    task = EmployeeModel.objects.get(id=pk)
    print(task)
    serializers = EmployeeSerializer(task,many=False)
    return Response(serializers.data)

@api_view(['POST'])
def taskCreate(request):
    serializers = EmployeeSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data,status=status.HTTP_201_CREATED)
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def taskUpdate(request,pk):
    task = EmployeeModel.objects.get(id=pk)
    print(task)
    serializers = EmployeeSerializer(instance=task,data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data,status=status.HTTP_201_CREATED) 
    
    return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def taskDelete(request,pk):
    task = EmployeeModel.objects.get(id=pk)
    task.delete()
    return Response("Item deleted successfully......")                   


