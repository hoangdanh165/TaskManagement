from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator

from project.models import Project

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    dob = models.DateField(max_length=20)

    gender_selections = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=gender_selections)

    age = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(99)
        ]
    )
    address = models.CharField(max_length=200)

    paticipated_project = models.ManyToManyField(Project, blank=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=300)
    due_date = models.DateTimeField()
    status = models.BooleanField(default=False)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    belongs_to = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.name


class Invitation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    invited_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_invitations')
    invited_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_invitations')
    message = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f'Invitation from {self.invited_by.name} to {self.invited_user.name} for project {self.project.name}'
