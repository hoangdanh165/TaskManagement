from django import template

register = template.Library()

@register.filter
def progress(project):
    total_tasks = project.tasks.count()
    if total_tasks == 0:
        return 0
    
    completed_tasks = project.tasks.filter(completed=True).count()
    return int(completed_tasks / total_tasks * 100)
    