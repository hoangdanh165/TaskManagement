from django.urls import path
from . import views


app_name = 'project'
urlpatterns = [
    path('projects/', views.projects, name='projects'),
    path('project/<int:project_id>/', views.project, name='project'),
    path('create-project/', views.createProject, name='create-project'),
    path('update-project/<int:project_id>', views.updateProject, name='update-project'),
    path('delete-project/<int:project_id>', views.deleteProject, name='delete-project'),
    path('project/<int:id>/participants/', views.get_participants, name='get-participants'),
]