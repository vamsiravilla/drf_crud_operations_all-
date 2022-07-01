from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    domain = models.CharField(max_length=15)
    