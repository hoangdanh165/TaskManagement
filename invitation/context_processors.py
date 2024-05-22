from .models import Invitation


def invitations_processor(request):
    if request.user.is_authenticated:
        invitations = Invitation.objects.filter(invited_user=request.user, accepted=False)
    else:
        invitations = []
    return {'invitations': invitations}
