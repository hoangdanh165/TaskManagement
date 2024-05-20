from django.urls import path
from . import views

urlpatterns = [
    path('project/<int:project_id>/tasks/', views.tasks, name='tasks'),
    path('update-task/<int:id>', views.update_task, name='update-task'),
    path('project/<int:project_id>/create-task/', views.create_task, name='create-task'),
    path('your-tasks', views.your_task, name='your-tasks'),
    path('turn-in-task', views.turn_in_task, name='turn-in-task'),
    path('undone-task', views.undone_task, name='undone-task'),
    
    
]