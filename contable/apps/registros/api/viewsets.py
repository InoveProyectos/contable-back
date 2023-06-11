# Se importa modelos
from ..models import *
# Se importa serializadores
from .serializers import *
# Se importa el módulo ViewSets que ofrece DRF
from rest_framework import viewsets
from rest_framework.decorators import action


class RegistroViewSet(viewsets.ModelViewSet):
    permission_classes = [] # Falta autenticación
    serializer_class = RegistroSerializer
    queryset = serializer_class.Meta.model.objects.all()


    def get_serializer_class(self):
        if self.action == 'registro':
            return RegistroSerializer
        
        if self.action == 'asiento_registro':
            return RegistroAsientoSerializer
        
        else:
            return self.serializer_class

    # action, permite marcar acciones adicionales para el enrutamiento.
    # Cuando se haga un post desde la url_path indicado recibir por request los datos
    # ¿Cómo asignar un valor a asiento?
    @action(detail=True,methods=['post'], url_path='asiento_registro', permission_classes = [])
    def asiento_registro(self, request, pk:int):
        data = {'id':pk, 
                  'cuenta':request.data.get("cuenta"),
                  'asiento':request.data.get("asiento"), 
                  'numero_operacion':request.data.get("numero_operacion"),  
                  'concepto':request.data.get("concepto"), 
                  'tipo_comprobante':request.data.get("tipo_comprobante"), 
                  'debe':request.data.get("debe"), 
                  'haber':request.data.get("habe"), 
                  'fecha_registro':request.data.get("fecha_registro"), 
                  'fecha_efectiva':request.data.get("fecha_efectiva"), 
                  'comprobante':request.data.get("comprobante"), 
                  'observaciones':request.data.get("observaciones")}
        
        # Serializar la data recibida
        serializer = self.get_serializer_class()(data=data)
        # Verificar si la serialización en válida.
        serializer.is_valid(raise_exception=True)
        serializer.save()
       
        return Response(data, status=status.HTTP_200_OK)
  
    
    
class PersoneriaViewSet(viewsets.ModelViewSet):
    permission_classes = [] # Falta autenticación
    serializer_class = PersoneriaSerializer
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


class CategoriaViewSet(viewsets.ModelViewSet):
    permission_classes = [] # Falta autenticación
    serializer_class = CategoriaSerializer
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

class RetencionesViewSet(viewsets.ModelViewSet):
    permission_classes = [] # Falta autenticación
    serializer_class = RetencionesSerializer
    queryset = serializer_class.Meta.model.objects.all()


class CuentasAsociadasViewSet(viewsets.ModelViewSet):
    permission_classes = [] # Falta autenticación
    serializer_class = CuentasAsociadasSerializer
    queryset = serializer_class.Meta.model.objects.all()

