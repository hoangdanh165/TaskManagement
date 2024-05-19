from django import template

register = template.Library()

@register.filter
def circle_class_type(progress):
    if progress < 25:
        return 'secondary'
    if progress < 50:
        return 'warning'
    if progress < 75:
        return 'primary'
    return 'success'
    