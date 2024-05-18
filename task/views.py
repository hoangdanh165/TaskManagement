from django.shortcuts import render

from project.models import Project
from .models import Task

def tasks(request, project_id):
    project = Project.objects.get(id=project_id)
    
    tasks = project.tasks.all()
    context = { 
        'project': project, 
        'tasks': tasks,
        'actived_page': 'tasks',
    }
    
    return render(request, 'task/page-task.html', context)

