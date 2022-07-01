from rest_framework import serializers
from app.models import EmployeeModel


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = '__all__' 