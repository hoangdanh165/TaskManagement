from django.contrib import admin
from django.urls import path
from employee import views

urlpatterns = [
    path('registration', views.registration, name='registration'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_out', views.sign_out, name='sign_out'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('view_user_profile', views.view_user_profile, name='view_user_profile'),
    path('edit_user_profile', views.edit_user_profile, name='edit_user_profile'),
    path('change_password', views.change_password, name='change_password'),
    # path('dashboard_calendar', views.dashboard_calendar, name='dashboard_calendar'),
]
