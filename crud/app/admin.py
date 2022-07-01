from django.contrib import admin
from app.models import Task
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['name','age','phone']