from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm


# Create your views here.
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
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            name = user.name
            return render(request, 'employee/employee-page.html', {'name': name})
        else:
            error_message = "Invalid username or password."
            messages.error(request, error_message)
            return render(request, 'employee/login-page.html', {'error_message': error_message})

    return render(request, 'employee/login-page.html')


def main(request):
    return render(request, 'employee/employee-page.html')
