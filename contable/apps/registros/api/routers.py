# Se importa los viewsets
from .viewsets import *
# Se importa la clase DefaultRouter
from rest_framework.routers import DefaultRouter

# Se crea una instancia de la clase DefaultRouter para que se haga cargo de las rutas
router = DefaultRouter()

# Registrar las vistas

# Primer ejemplo---> GET /registros/api/tipo_entidad_vs/

# Rutas que deben permitir almacenar los datos para generar una entidad
router.register(r'categoria-vs', viewset=CategoriaViewSet, basename='categoria-vs') 
router.register(r'condicion-impositiva', viewset=CondicionImpositivaViewSet, basename='condicion-impositiva') 

# Rutas que deben permitir almacenar los datos para generar una cuenta
router.register(r'entidad', viewset=EntidadViewSet, basename='entidad') # Necesita que estén registrados los valores de FK 
router.register(r'tipo-cuenta', viewset=TipoCuentaViewSet, basename='tipo-cuenta')
router.register(r'moneda', viewset=MonedaViewSet, basename='moneda')

# Ruta que debe permitir almacenar los datos para generar una cuentas asociadas
router.register(r'cuenta', viewset=CuentaViewSet, basename='cuenta') 
router.register(r'cuentas-asociadas', viewset=CuentasAsociadasViewSet, basename='cuentas-asociadas') 


urlpatterns = router.urls