from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from django.contrib import messages

from employee.models import User
from .forms import ProjectForm
from .models import Project

def projects(request):
    projects = Project.objects.all()
    form = ProjectForm()
    context = { 'projects': projects, 'form': form }    
    return render(request, 'project/page-project.html', context)


def project(request, id):
    project = Project.objects.get(id=id)
    
    context = { 'project': project }
    return render(request, 'project/single-project.html', context)

@require_POST
def createProject(request):
    form = ProjectForm(request.POST)
    
    if form.is_valid():
        project = form.save(commit=False)
        # owner_id = request.POST.get('owner')
        # signed_in_user = request.user
        project.owner = User.objects.get(username='tienze')
        project.save()
        messages.success(request, 'Created project successfully!')
        return redirect('projects')
    
    messages.error(request, 'Failed to create new project!')
    
    return render(request, 'project/page-project.html', {'form': form})
