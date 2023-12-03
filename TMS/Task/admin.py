from django.contrib import admin
from .models import Task, CommonTask

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(CommonTask)
class CommonTaskAdmin(admin.ModelAdmin):
    pass
