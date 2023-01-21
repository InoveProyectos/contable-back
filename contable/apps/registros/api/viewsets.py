# Se importa modelos
from ..models import *
# Se importa serializadores
from .serializers import *
# Se importa el módulo ViewSets que ofrece DRF
from rest_framework import viewsets
from rest_framework.response import Response

class RegistroViewSet(viewsets.ModelViewSet):
    permission_classes = [] # Falta autenticación
    serializer_class = RegistroSerializer
    queryset = serializer_class.Meta.model.objects.all()


class TipoEntidadViewSet(viewsets.ModelViewSet):
    permission_classes = [] # Falta autenticación
    serializer_class = TipoEntidadSerializer
    queryset = serializer_class.Meta.model.objects.all()

    # def create(self, request, *args, **kwargs):
    #     data = request.data

    #     new_tipo_entidad = TipoEntidad.objects.create(data['name'])
    #     new_tipo_entidad.save()

    #     # Serializar el nuevo objeto creado
    #     serializer = TipoEntidadSerializer(new_tipo_entidad)

    #     return Response(serializer.data)

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
