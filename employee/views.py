from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegistrationForm, ProfileUpdateForm, PasswordUpdateForm
from django.contrib.auth.decorators import login_required


# Authentication
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            messages.success(request, "SUCCESSFULLY SUBMITTED!")
            return render(request, 'employee/login-page.html', {'new_username': new_user.name})
        else:
            return render(request, 'employee/register-page.html', {'form': form})
    else:
        return render(request, 'employee/register-page.html')


def sign_in(request):
    if request.user.is_authenticated:
        user = request.user
        name = user.name
        return render(request, 'employee/dashboard.html', {'name': name})

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            name = user.name
            return render(request, 'employee/dashboard.html', {'name': name})
        else:
            error_message = "Invalid username or password."
            messages.error(request, error_message)
            return render(request, 'employee/login-page.html', {'error_message': error_message})

    return render(request, 'employee/login-page.html')


@login_required
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
    new_password = request.POST['new_password']
    confirm_password = request.POST['confirm_password']
    form = PasswordUpdateForm(request.POST, instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('view_user_profile')
    else:
        return render(request, 'employee/edit-user-profile.html')


@login_required()
def dashboard(request):
    title = "Dashboard"
    if request.user.is_authenticated:
        return render(request, 'employee/dashboard.html', {'name': request.user.name, 'title': title})
