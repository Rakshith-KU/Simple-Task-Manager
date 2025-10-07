from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'deadline', 'completed', 'created_at')
    list_filter = ('completed', 'deadline')
    search_fields = ('title', 'description')
