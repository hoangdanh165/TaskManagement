from django.shortcuts import redirect, render

from employee.models import User

from .forms import ProjectForm
from .models import Project
from django.views.decorators.http import require_POST

def projects(request):
    projects = Project.objects.all()
    context = { 'projects': projects }    
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
        print('Created project')
        return redirect('projects')
    
    
    print('Failed to create project', form.errors.items())
    return redirect('projects')
