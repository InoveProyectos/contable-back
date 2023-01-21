# Se importa los viewsets
from .viewsets import TipoEntidadViewSet
# Se importa la clase DefaultRouter
from rest_framework.routers import DefaultRouter

# Se crea una instancia de la clase DefaultRouter para que se haga cargo de las rutas
router = DefaultRouter()

# Registrar las vistas

# Primer ejemplo---> GET /registros/api/modelviewset/tipo_entidad/
router.register(r'modelviewset/tipo_entidad', viewset=TipoEntidadViewSet) 


urlpatterns = router.urls