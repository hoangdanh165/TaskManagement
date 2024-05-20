from django.shortcuts import redirect, render
from django.urls import reverse

from project.models import Project
from task.forms import TaskForm
from .models import Task

from django.views.decorators.http import require_POST
from django.contrib import messages

def filter_task(request, tasks, task_range='all', task_status='all'):
    if task_range == 'mine':
        tasks = tasks.filter(assigned_to=request.user)
    else:
        tasks = tasks.all()
    
    tasks = filter_tasks_by_status(tasks, task_status)
    
    return tasks

def filter_tasks_by_status(tasks, task_status='all'):
    if task_status == 'completed':
        tasks = tasks.filter(completed=True)
    elif task_status == 'in progress':
        tasks = tasks.filter(completed=False)
    
    return tasks

def tasks(request, project_id):
    project = Project.objects.get(id=project_id)
    
    task_range = request.GET.get('task_range', 'all')
    task_status = request.GET.get('task_status', 'all')
    
    tasks = filter_task(request, project.tasks, task_range, task_status)
    
    context = { 
        'project': project, 
        'tasks': tasks,
        'actived_page': 'tasks',
        'task_range': task_range,
        'task_status': task_status,
    }
    return render(request, 'task/page-task.html', context)

def your_task(request):
    project_id = request.GET.get('project_id')
    
    if project_id is None:
        # Display the overview tasks of all participated_projects
        participated_projects = request.user.participated_projects.all()
        
        context = {
            'title': 'Tasks',
            'participated_projects': participated_projects,
            'actived_view': 'projects',
        }
        
        return render(request, 'task/your-tasks.html', context)
    
    # Display the tasks of a specific project
    project = Project.objects.get(id=project_id)
    your_tasks = Task.objects.filter(belongs_to=project, assigned_to=request.user)
    
    completed_tasks = filter_tasks_by_status(your_tasks, 'completed')
    num_completed_tasks = completed_tasks.count()
    
    in_progress_tasks = filter_tasks_by_status(your_tasks, 'in progress')
    num_in_progress_tasks = in_progress_tasks.count()
    
    context = {
        'title': 'Tasks',
        'completed_tasks': completed_tasks,
        'num_completed_tasks': num_completed_tasks,
        
        'in_progress_tasks': in_progress_tasks,
        'num_in_progress_tasks': num_in_progress_tasks,
        
        'project_name': project.name,
        'project_id': project_id,
        
        'actived_view': 'tasks',
    }
    return render(request, 'task/your-tasks.html', context)

@require_POST
def create_task(request, project_id):
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
def update_task(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(request.POST, instance=task)
    
    if form.is_valid():
        form.save()
        messages.success(request, 'Task updated successfully!')
        return redirect('tasks', task.belongs_to.id)
        
    messages.error(request, 'Failed to update this Task!')
    return redirect('tasks', task.belongs_to.id)

@require_POST
def turn_in_task(request):
    task_id = request.POST.get('task_id')
    
    task_obj = Task.objects.get(id=task_id)
    task_obj.completed = True
    task_obj.save()
    
    project_id = task_obj.belongs_to.id 
    
    url = reverse('your-tasks') + f'?project_id={project_id}'
    return redirect(url)

@require_POST
def undone_task(request):
    task_id = request.POST.get('task_id')
    
    task_obj = Task.objects.get(id=task_id)
    task_obj.completed = False
    task_obj.save()
    
    project_id = task_obj.belongs_to.id 
    
    url = reverse('your-tasks') + f'?project_id={project_id}'
    return redirect(url)
    
    
    
