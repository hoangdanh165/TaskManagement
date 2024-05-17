from django.db import models
# from employee.models import User

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey('employee.User', on_delete=models.CASCADE, related_name='owned_projects')
    due_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

