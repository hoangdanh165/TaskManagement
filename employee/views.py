from datetime import datetime
from json import dumps
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
import pytz


# Authentication
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            return render(request, 'employee/login-page.html')
        else:
            return render(request, 'employee/register-page.html', {'form': form})
    else:
        return render(request, 'employee/register-page.html')


def sign_in(request):
    if request.user.is_authenticated:
        user = request.user
        name = user.name
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            name = user.name
            return redirect('dashboard')
        else:
            error_message = "Invalid username or password."
            messages.error(request, error_message)
            return render(request, 'employee/login-page.html', {'error_message': error_message})

    return render(request, 'employee/login-page.html')


def sign_out(request):
    logout(request)
    return redirect('sign_in')


# USER'S PROFILE
@login_required
def edit_user_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('view_user_profile')
        else:
            return render(request, 'employee/edit-user-profile.html', {'form': form})

    return redirect('view_user_profile')


@login_required
def view_user_profile(request):
    return render(request, 'employee/edit-user-profile.html', {'user': request.user})


@login_required
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        if not request.user.check_password(current_password):
            messages.error(request, 'Current password is incorrect!')
        elif new_password != confirm_password:
            messages.error(request, 'Confirm password do not match!')
        else:
            request.user.set_password(new_password)
            request.user.save()
            # Keep user logged in
            update_session_auth_hash(request, request.user)
            messages.success(request, "Your password was successfully updated!")
            return redirect('edit_user_profile')

    return redirect('edit_user_profile')


@login_required()
def dashboard(request):
    if request.user.is_authenticated:
        title = "Dashboard"
        projects = request.user.participated_projects.all()
        nearest_due_timedelta = None
        nearest_due_project = None
        project_due_dates = []
        for project in projects:
            due_date = str(project.due_date).split(' ')[0]
            project_due_dates.append({
                'due_date': due_date,
                'name': project.name,
                'description': project.description
            })
        for project in projects:
            now_naive = datetime.now()
            now_aware = pytz.timezone('UTC').localize(now_naive)
            time_difference = now_aware - project.due_date

            if nearest_due_timedelta is None or time_difference < nearest_due_timedelta:
                nearest_due_timedelta = time_difference
                nearest_due_project = project

        data = dumps(project_due_dates)
        return render(request, 'employee/dashboard.html',
                      {'name': request.user.name, 'title': title, 'projects': projects,
                       'nearest_due_project': nearest_due_project, 'data': data})


# @login_required()
# def dashboard_calendar(request):
