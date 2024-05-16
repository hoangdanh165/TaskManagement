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
