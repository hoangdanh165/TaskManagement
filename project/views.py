from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.core.paginator import Paginator

from .forms import ProjectForm
from .models import Project

from decorators.custom_decorator import identify_project_owner, required_project_owner
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='/employee/sign_in')
def projects(request):
    filter_by = request.GET.get('filter_by', 'all')
    if filter_by == 'participated':
        projects_list = request.user.participated_projects.all()
    elif filter_by == 'mine':
        projects_list = request.user.owned_projects.all()
    else:
        projects_list = Project.objects.all()
    
    # Continue filtering by search query
    search_query = request.GET.get('search', '')
    projects_list = projects_list.filter(name__icontains=search_query)
    
    paginator = Paginator(projects_list, 6)

    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    
    view_option = request.GET.get('view_option', 'grid')

    form = get_stored_form_or_create_one(request, ProjectForm)
    context = {
        'title': 'Projects',
        'page': page, 
        'form': form,
        'filter_by': filter_by,
        'search_query': search_query,
        'view_option': view_option,
        'page_name': 'Project'
    }    
    return render(request, 'project/page-project.html', context)

@login_required(login_url='/employee/sign_in')
@identify_project_owner
def project(request, id):
    project = Project.objects.get(id=id)
    form = get_stored_form(request, ProjectForm)
    if form is None:
        form = ProjectForm(instance=project)
    
    context = {
        'title': 'Projects',
        'project': project,
        'form': form,
        'actived_page': 'details'
    }
    return render(request, 'project/single-project.html', context)

@require_POST
@login_required(login_url='/employee/sign_in')
def createProject(request):
    form = ProjectForm(request.POST, request.FILES)
    
    if form.is_valid():
        project = form.save(commit=False)
        project.owner = request.user
        project.save()
        project.participants.add(request.user)
        messages.success(request, 'Created project successfully!')
        return redirect('project:projects')
    
    messages.error(request, 'Failed to create new project!')
    
    store_form(request, form)
    return redirect('project:projects')


@require_POST
@login_required(login_url='/employee/sign_in')
@identify_project_owner
@required_project_owner
def updateProject(request, id):
    project = Project.objects.get(id=id)
    form = ProjectForm(request.POST, request.FILES, instance=project)
    
    if form.is_valid():
        form.save()
        messages.success(request, 'Updated project successfully!')
        return redirect('project:project', id=id)
    
    messages.error(request, 'Failed to update this project!')
    store_form(request, form)
    return redirect('project:project', id=id)

@require_POST
@login_required(login_url='/employee/sign_in')
@identify_project_owner
@required_project_owner
def deleteProject(request, id):
    project = Project.objects.get(id=id)
    project_name = project.name
    
    project.delete()
    messages.success(request, 'Deleted project "%s" successfully!' % project_name)
    
    return redirect('project:projects')

# Get participants in the project that has id
@login_required(login_url='/employee/sign_in')
def get_participants(request, id):
    project = Project.objects.get(id=id)
    
    context = {
        'title': 'Projects',
        'project': project,
        'actived_page': 'participated employees'
    }
    
    return render(request, 'project/participated-employees.html', context)