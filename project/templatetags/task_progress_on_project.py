from task.models import Task
from django import template

register = template.Library()

@register.filter
def task_progress_percentage(project, user):
    tasks_of_user_on_project = Task.objects.filter(belongs_to=project, assigned_to=user)
    total_tasks = tasks_of_user_on_project.count()
    completed_tasks = tasks_of_user_on_project.filter(completed=True).count()
    return int(completed_tasks / total_tasks * 100) if total_tasks > 0 else 100

@register.filter
def task_progress_text(project, user):
    tasks_of_user_on_project = Task.objects.filter(belongs_to=project, assigned_to=user)
    total_tasks = tasks_of_user_on_project.count()
    completed_tasks = tasks_of_user_on_project.filter(completed=True).count()
    return f'{completed_tasks}/{total_tasks} tasks'