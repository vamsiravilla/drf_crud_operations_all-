from django.contrib import admin
from app.models import EmployeeModel 
# Register your models here.
 
@admin.register(EmployeeModel) 
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','age','domain']
