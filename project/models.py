from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=300)
    owner = models.ForeignKey('User', on_delete=models.CASCADE, related_name='owned_projects')

    def __str__(self):
        return self.name

