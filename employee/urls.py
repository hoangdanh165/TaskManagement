from django.contrib import admin
from django.urls import path
from employee import views

urlpatterns = [
    # path('sign_in', views.registration, name='sign_in')
    path('registration', views.registration, name='registration')
]
