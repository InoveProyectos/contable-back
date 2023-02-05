# Se importa los viewsets
from .viewsets import *
# Se importa la clase DefaultRouter
from rest_framework.routers import DefaultRouter

# Se crea una instancia de la clase DefaultRouter para que se haga cargo de las rutas
router = DefaultRouter()

# Registrar las vistas

# Primer ejemplo---> GET /registros/api/tipo_entidad_vs/
router.register(r'tipo_entidad_vs', viewset=TipoEntidadViewSet, basename='tipo_entidad_vs') 
router.register(r'condicion_impositiva', viewset=CondicionImpositivaViewSet, basename='condicion_impositiva') 
router.register(r'entidad', viewset=EntidadViewSet, basename='entidad') # Necesita que esté registrados los valores de FK 

urlpatterns = router.urls