from asyncio import mixins
from django.shortcuts import render
from requests import delete
from app.models import EmployeeModel
from app.serializers import EmployeeSerializer
from rest_framework import mixins,generics

# Create your views here.

class EmployeeListMixins(mixins.ListModelMixin,generics.GenericAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class EmployeeDetailMixins(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


