from django.urls import path
from . import views

urlpatterns = [
    path('project/<int:project_id>/tasks/', views.tasks, name='tasks'),
    path('update-task/<int:id>', views.updateTask, name='update-task'),
    
]