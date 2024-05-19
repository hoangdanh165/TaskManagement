from django import template
import os

register = template.Library()

@register.filter
def filename(path):
    return os.path.basename(path)