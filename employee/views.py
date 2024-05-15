from django.shortcuts import render


# Create your views here.
def registration(request):
    return render(request, 'employee/register-page.html')


def main_page(request):
    return render(request, 'employee/employee-page.html')