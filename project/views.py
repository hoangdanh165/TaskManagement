from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.core.paginator import Paginator

from .forms import ProjectForm
from .models import Project

def store_form(request, form):
    request.session['form_data'] = form.data
    request.session['form_errors'] = form.errors

def get_stored_form_or_create_one(request, form_class):
    form = get_stored_form(request, form_class)
    
    if form is None:
        form = form_class()
        
    return form

def get_stored_form(request, form_class):
    form_data = request.session.pop('form_data', None)
    form_errors = request.session.pop('form_errors', None)

    if form_data is not None:
        form = form_class(form_data)
        form.is_valid()  # Populate form.errors
        # form.errors.update(form_errors)
        return form
    
    return None
    
def projects(request):
    search_query = request.GET.get('search', '')
    projects_list = Project.objects.filter(name__icontains=search_query)
    paginator = Paginator(projects_list, 6) # Show 10 projects per page.

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    
    view_option = request.GET.get('view_option', 'grid')

    form = get_stored_form_or_create_one(request, ProjectForm)
    context = { 
        'page': page, 
        'form': form, 
        'search_query': search_query,
        'view_option': view_option,
    }    
    return render(request, 'project/page-project.html', context)


def project(request, id):
    project = Project.objects.get(id=id)
    form = get_stored_form(request, ProjectForm)
    if form is None:
        form = ProjectForm(instance=project)
    
    context = { 'project': project, 'form': form, 'actived_page': 'details' }
    return render(request, 'project/single-project.html', context)

@require_POST
def createProject(request):
    form = ProjectForm(request.POST, request.FILES)
    
    if form.is_valid():
        project = form.save(commit=False)
        project.owner = request.user
        project.save()
        messages.success(request, 'Created project successfully!')
        return redirect('projects')
    
    messages.error(request, 'Failed to create new project!')
    
    store_form(request, form)
    return redirect('projects')

@require_POST
def updateProject(request, id):
    project = Project.objects.get(id=id)
    form = ProjectForm(request.POST, request.FILES, instance=project)
    
    if form.is_valid():
        form.save()
        messages.success(request, 'Updated project successfully!')
        return redirect('project', id=id)
    
    messages.error(request, 'Failed to update this project!')
    store_form(request, form)
    return redirect('project', id=id)

@require_POST
def deleteProject(request, id):
    project = Project.objects.get(id=id)
    project_name = project.name
    
    project.delete()
    messages.success(request, 'Deleted project "%s" successfully!' % project_name)
    
    return redirect('projects')