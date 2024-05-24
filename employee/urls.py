from django.contrib import admin
from django.urls import path
from employee import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('registration', views.registration, name='registration'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_out', views.sign_out, name='sign_out'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('view_user_profile', views.view_user_profile, name='view_user_profile'),
    path('edit_user_profile', views.edit_user_profile, name='edit_user_profile'),
    path('change_password', views.change_password, name='change_password'),
    path('change_contact', views.change_contact, name='change_contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
