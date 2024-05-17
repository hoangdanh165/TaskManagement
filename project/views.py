from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from django.contrib import messages

from employee.models import User
from .forms import ProjectForm
from .models import Project

def store_form(request, form):
    request.session['form_data'] = form.data
    request.session['form_errors'] = form.errors

def get_stored_form_or_create_one(request, form_class):
    form_data = request.session.pop('form_data', None)
    form_errors = request.session.pop('form_errors', None)

    if form_data is not None:
        form = form_class(form_data)
        form.is_valid()  # Populate form.errors
        # form.errors.update(form_errors)
    else:
        form = form_class()

    return form

def projects(request):
    projects = Project.objects.all()
    form = get_stored_form_or_create_one(request, ProjectForm)
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
    
    store_form(request, form)
    return redirect('projects')

@require_POST
def updateProject(request, id):
    project = Project.objects.get(id=id)
    
    form = ProjectForm(request.POST, instance=project)
    
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
