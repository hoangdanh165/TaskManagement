from django.contrib import admin
from employee.models import User
from project.models import Project
from task.models import Task
from invitation.models import Invitation


# Register your models here.
admin.site.register(User)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Invitation)

