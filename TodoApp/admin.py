from django.contrib import admin
from .models import Task
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display=('task_content','is_completed','user_id','updated_at')
    search_fields=('user_id',)

admin.site.register(Task,TaskAdmin)