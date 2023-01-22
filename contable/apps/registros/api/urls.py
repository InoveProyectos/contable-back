from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('admin/', admin.site.urls),


    # Ejemplo registro API Viewsets:
    path('', include('apps.registros.api.routers')), 
]