from django.http import HttpResponseForbidden
from functools import wraps
from project.models import Project

# Identitfy if the user is the owner of the project
def identify_project_owner(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        project = Project.objects.get(id=kwargs['id'])
        request.user.is_project_owner = (request.user == project.owner)
        
        return view_func(request, *args, **kwargs)
    return _wrapped_view

def required_project_owner(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_project_owner:
            return HttpResponseForbidden()
        
        return view_func(request, *args, **kwargs)
    return _wrapped_view

# def required_project_owner(view_func):
#     @wraps(view_func)
#     def _wrapped_view(request, *args, **kwargs):
#         project = Project.objects.get(id=kwargs['id'])
#         if request.user != project.owner:
#             request.user._is_owner = False
#             return HttpResponseForbidden()
        
#         request.user._is_owner = True
#         return view_func(request, *args, **kwargs)
#     return _wrapped_view