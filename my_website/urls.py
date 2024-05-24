from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from employee.views import dashboard as index

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', index, name='index'),
    
    path('employee/', include('employee.urls')),
    path('employee/', include('django.contrib.auth.urls')),
    path('', include('project.urls', namespace='project')),
    path('', include('task.urls')),
    path('', include('invitation.urls', namespace='invitation')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
