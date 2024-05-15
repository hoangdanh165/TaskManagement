from django.contrib import admin
from django.urls import include, path
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_home),
    
    path('', include('project.urls'))
]
