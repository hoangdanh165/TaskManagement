from django.urls import path
from . import views

urlpatterns = [
    path('project/<int:project_id>/tasks/', views.tasks, name='tasks'),
    
]