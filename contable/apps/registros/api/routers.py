# Se importa los viewsets
from .viewsets import *
# Se importa la clase DefaultRouter
from rest_framework.routers import DefaultRouter

# Se crea una instancia de la clase DefaultRouter para que se haga cargo de las rutas
router = DefaultRouter()

# Registrar las vistas

# Primer ejemplo---> GET /registros/api/tipo_entidad_vs/

# Rutas que deben permitir almacenar los datos para generar una entidad
router.register(r'crud/personeria', viewset=PersoneriaViewSet, basename='personeria') 
router.register(r'crud/condicion-impositiva', viewset=CondicionImpositivaViewSet, basename='condicion-impositiva') 

# Rutas que deben permitir almacenar los datos para generar una cuenta
router.register(r'crud/entidad', viewset=EntidadViewSet, basename='entidad') # Necesita que estén registrados los valores de FK 
router.register(r'crud/categoria', viewset=CategoriaViewSet, basename='categoria')
router.register(r'crud/moneda', viewset=MonedaViewSet, basename='moneda')

# Ruta que debe permitir almacenar los datos para generar una cuentas asociadas
router.register(r'crud/cuenta', viewset=CuentaViewSet, basename='cuenta') 

# Ruta que debe permitir almacenar los datos para registro
router.register(r'crud/registro', viewset=RegistroViewSet, basename='registro') 
router.register(r'asiento/registro', viewset=RegistroViewSet, basename='asiento_registro')

# Ruta que debe permitir crear un asiento
router.register(r'crud/asiento', viewset=AsientoViewSet, basename='asiento') 

# Ruta que debe permitir crear un tipo_comprobante
router.register(r'crud/tipo_comprobante', viewset=TipoComprobanteViewSet, basename='tipo_comprobante') 

# Ruta que debe permitir crear un comprobante
router.register(r'crud/comprobante', viewset=ComprobanteViewSet, basename='comprobante') 

urlpatterns = router.urls