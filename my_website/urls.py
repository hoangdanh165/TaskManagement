from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employee.urls'))
=======
from django.urls import include, path
from employee import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_home),
    
    path('', include('project.urls'))
>>>>>>> 09c60702f27f1ba96ec66d61a0885f43cd659a95
]
