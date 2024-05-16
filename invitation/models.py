from django.db import models


# Create your models here.
class Invitation(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    invited_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_invitations')
    invited_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_invitations')
    message = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f'Invitation from {self.invited_by.name} to {self.invited_user.name} for project {self.project.name}'
