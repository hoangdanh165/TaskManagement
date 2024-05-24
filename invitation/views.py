from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Add this import
from .models import Invitation
from .forms import InvitationForm
from project.models import Project
from employee.models import User
from django.utils import timezone

@login_required
def send_invitation(request):
    project_id = request.POST['project_id']
    project = Project.objects.get(id=project_id)
    
    if request.method == 'POST':
        form = InvitationForm(request.POST)
        if form.is_valid():
            # project_name = request.POST['project_name']
            # project = get_object_or_404(Project, name=project_name)

            invited_user_name = request.POST['invited_user']
            invited_user = get_object_or_404(User, username=invited_user_name)

            message = request.POST['message']

            invitation = form.save(commit=False)
            invitation.project = project
            invitation.invited_user = invited_user
            invitation.message = message
            invitation.invited_by = request.user
            invitation.timestamp = timezone.datetime.now()
            invitation.save()
            
            messages.success(request, 'Invitation sent successfully!')
            # Optionally, send notification to the invited user here
            return redirect('project:get-participants', id=project.id)

    return redirect('project:get-participants', id=project.id)


@login_required
def receive_invitation(request):
    invitations = Invitation.objects.filter(invited_user=request.user)
    return render(request, 'base.html', {'invitations': invitations})


@login_required
def accept_invitation(request, invitation_id):
    invitation = get_object_or_404(Invitation, id=invitation_id, invited_user=request.user)
    if request.method == 'POST':
        invitation.accepted = True
        invitation.delete()
        # Optionally, you can add the user to the project participants here
        project = invitation.project
        project.participants.add(request.user)
        project.save()
        return redirect('project:get-participants', id=project.id)

