from django.contrib import admin
from django.urls import path, include

# Se importa modelos
from ..models import *
# Se importa serializadores
from .serializers import *
from .viewsets import *


urlpatterns = [
    #path('admin/', admin.site.urls),

    # Ejemplo registro API Viewsets:
    path('', include('apps.registros.api.routers')), 
        
]