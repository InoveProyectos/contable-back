from django.contrib import admin
from django.urls import path, include
from .api_views import *

# Se importa modelos
from ..models import *
# Se importa serializadores
from .serializers import *
from .viewsets import *


urlpatterns = [
    #path('admin/', admin.site.urls),

    # Ejemplo registro API Viewsets:
    path('', include('apps.registros.api.routers')), 
    path(f'user/', RegistroAsientoAPIView.as_view(), name="registro_asiento"),
        
]