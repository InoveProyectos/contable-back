# Se importa los viewsets
from .viewsets import *
# Se importa la clase DefaultRouter
from rest_framework.routers import DefaultRouter

# Se crea una instancia de la clase DefaultRouter para que se haga cargo de las rutas
router = DefaultRouter()

# Registrar las vistas
# Primer ejemplo
router.register(r'modelviewset/registro', RegistroViewSet)


urlpatterns = router.urls