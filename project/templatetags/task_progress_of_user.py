from task.models import Task
from django import template

register = template.Library()

# Compute the progress of a user on all projects
@register.filter
def task_progress_of_user(user):
    tasks_of_user = Task.objects.filter(assigned_to=user)
    total_tasks = tasks_of_user.count()
    completed_tasks = tasks_of_user.filter(completed=True).count()
    return int(completed_tasks / total_tasks * 100) if total_tasks > 0 else 100