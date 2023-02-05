# Se importa modelos
from ..models import *
# Se importa serializadores
from .serializers import *
# Se importa el módulo ViewSets que ofrece DRF
from rest_framework import viewsets


class RegistroViewSet(viewsets.ModelViewSet):
    permission_classes = [] # Falta autenticación
    serializer_class = RegistroSerializer
    queryset = serializer_class.Meta.model.objects.all()
    
    
class TipoEntidadViewSet(viewsets.ModelViewSet):
    permission_classes = [] # Falta autenticación
    serializer_class = TipoEntidadSerializer
    queryset = serializer_class.Meta.model.objects.all()

    
class CondicionImpositivaViewSet(viewsets.ModelViewSet):
    permission_classes = [] # Falta autenticación
    serializer_class = CondicionImpositivaSerializer
    queryset = serializer_class.Meta.model.objects.all()


class EntidadViewSet(viewsets.ModelViewSet):
    permission_classes = [] # Falta autenticación
    serializer_class = EntidadSerializer
    queryset = serializer_class.Meta.model.objects.all()  


class TipoIdentificacionViewSet(viewsets.ModelViewSet):
    permission_classes = [] # Falta autenticación
    serializer_class = TipoIdentificacionSerializer
    queryset = serializer_class.Meta.model.objects.all()


class IdentificacionViewSet(viewsets.ModelViewSet):
    permission_classes = [] # Falta autenticación
    serializer_class = IdentificacionSerializer
    queryset = serializer_class.Meta.model.objects.all()


class TipoCuentaViewSet(viewsets.ModelViewSet):
    permission_classes = [] # Falta autenticación
    serializer_class = TipoCuentaSerializer
    queryset = serializer_class.Meta.model.objects.all()


class MonedaViewSet(viewsets.ModelViewSet):
    permission_classes = [] # Falta autenticación
    serializer_class = MonedaSerializer
    queryset = serializer_class.Meta.model.objects.all()


class CuentaViewSet(viewsets.ModelViewSet):
    permission_classes = [] # Falta autenticación
    serializer_class = CuentaSerializer
    queryset = serializer_class.Meta.model.objects.all()


class AsientoViewSet(viewsets.ModelViewSet):
    permission_classes = [] # Falta autenticación
    serializer_class = AsientoSerializer
    queryset = serializer_class.Meta.model.objects.all()


class TipoComprobanteViewSet(viewsets.ModelViewSet):
    permission_classes = [] # Falta autenticación
    serializer_class = TipoComprobanteSerializer
    queryset = serializer_class.Meta.model.objects.all()


class ComprobanteViewSet(viewsets.ModelViewSet):
    permission_classes = [] # Falta autenticación
    serializer_class = ComprobanteSerializer
    queryset = serializer_class.Meta.model.objects.all()
