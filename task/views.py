from django.shortcuts import redirect, render

from project.models import Project
from task.forms import TaskForm
from .models import Task

from django.views.decorators.http import require_POST
from django.contrib import messages

def tasks(request, project_id):
    project = Project.objects.get(id=project_id)
    
    task_range = request.GET.get('task_range', 'all')
    if task_range == 'mine':
        tasks = project.tasks.filter(assigned_to=request.user)
    else:
        tasks = project.tasks.all()
    
    task_status = request.GET.get('task_status', 'all')
    if task_status == 'completed':
        tasks = tasks.filter(completed=True)
    elif task_status == 'in progress':
        tasks = tasks.filter(completed=False)
    
    context = { 
        'project': project, 
        'tasks': tasks,
        'actived_page': 'tasks',
        'task_range': task_range,
        'task_status': task_status,
    }
    
    return render(request, 'task/page-task.html', context)

@require_POST
def createTask(request, project_id):
    form = TaskForm(request.POST)
    
    if form.is_valid():
        task = form.save(commit=False)
        task.belongs_to = Project.objects.get(id=project_id)
        task.save()
        messages.success(request, 'Created new Task successfully!')
        return redirect('tasks', task.belongs_to.id)
        
    messages.error(request, 'Failed to create new Task!')
    return redirect('tasks', task.belongs_to.id)

@require_POST
def updateTask(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(request.POST, instance=task)
    
    if form.is_valid():
        form.save()
        messages.success(request, 'Task updated successfully!')
        return redirect('tasks', task.belongs_to.id)
        
    messages.error(request, 'Failed to update this Task!')
    return redirect('tasks', task.belongs_to.id)

