from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import Task
from django.contrib.auth.decorators import login_required
from .models import Task 
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@login_required
def list_task(request):
    current_user_id=request.user.id 
    # print(current_user_id)
    incomplete_tasks=Task.objects.filter(user_id=current_user_id,is_completed=False).order_by('-updated_at')
    completed_tasks=Task.objects.filter(user_id=current_user_id,is_completed=True).order_by('-updated_at')
    # print(task_list)
    context={
        'incompleted_tasks':incomplete_tasks,
        'completed_tasks':completed_tasks,
    }
    return render(request,'todo_app.html',context)

@login_required
def add_task(request):
    if request.method == 'POST':
        task_content = request.POST.get('task')  
        if task_content:
            Task.objects.create(task_content=task_content,user_id=request.user)
    return redirect('dashboard')

@login_required
def completed_task(request,pk):
    task=Task.objects.get(task_id=pk)
    if task:
        task.is_completed=True 
        task.save()
    return redirect('dashboard')

@login_required
def delete_task(request,pk):
    task=get_object_or_404(Task,task_id=pk)
    if task:
        task.delete()
    else:
        return HttpResponse('Bad Request 404')
    
    return redirect('dashboard')

@login_required
def undo_task(request,pk):
    task=get_object_or_404(Task,task_id=pk)
    if task:
        task.is_completed=False
        task.save()
    else:
        HttpResponse('Bad Request 404')
    return redirect('dashboard')

# @csrf_exempt  # Disable CSRF for now (Use middleware for security)
@login_required
def edit_task(request, pk):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # ✅ Read JSON request
            new_content = data.get("task_content")  # ✅ Extract task content
            print("Received Task Content:", new_content)  # Debugging

            task = Task.objects.get(pk=pk)
            task.task_content = new_content
            task.save()

            return JsonResponse({"success": True})
        except Exception as e:
            print("Error:", str(e))
            return JsonResponse({"success": False, "error": str(e)})
    
    return JsonResponse({"success": False, "error": "Invalid request"})