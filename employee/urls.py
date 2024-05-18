from django.contrib import admin
from django.urls import path
from employee import views

urlpatterns = [
    path('registration', views.registration, name='registration'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('employee_page', views.main, name='employee_page'),
]
