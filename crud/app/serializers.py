from re import T
from rest_framework import serializers
from app.models import Task
class Taskserializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields="__all__"