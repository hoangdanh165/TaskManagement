from django import template

register = template.Library()

@register.filter
def filter_by_to_label(filter_by):
    if filter_by == 'mine':
        return 'My Projects'
    
    if filter_by == 'participated':
        return 'Participated'
    
    return 'All Projects'
    
    