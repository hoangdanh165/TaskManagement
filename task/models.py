from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=300)
    due_date = models.DateTimeField()
    description = models.TextField()
    completed = models.BooleanField(default=False)
    
    assigned_to = models.ForeignKey('employee.User', on_delete=models.CASCADE, related_name='tasks')
    belongs_to = models.ForeignKey('project.Project', on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.name
