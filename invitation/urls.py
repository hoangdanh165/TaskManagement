from django.urls import path
from invitation import views


app_name = 'invitation'
urlpatterns = [
    path('send_invitation', views.send_invitation, name='send_invitation'),
    path('receive_invitation', views.receive_invitation, name='receive_invitation'),
    path('accept_invitation/<int:invitation_id>/', views.accept_invitation, name='accept_invitation'),
]
