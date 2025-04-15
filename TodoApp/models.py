from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_content = models.TextField(max_length=250)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1) 
    def __str__(self):
        return f"Id : {self.task_id}, Content:{self.task_content},is_Completed :{self.is_completed},updated_at :{self.updated_at}"
