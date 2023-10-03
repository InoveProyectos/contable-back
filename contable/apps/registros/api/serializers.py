# Se imporat modelos
from ..models import *
# Se importa los serializadores de Django
from rest_framework import serializers, status
from rest_framework.response import Response


class RegistroSerializer(serializers.ModelSerializer):
    #Atributos relacionados, cuyos valores representan un foreingkey
    cuenta = serializers.PrimaryKeyRelatedField(queryset= Cuenta.objects.all())
    asiento = serializers.PrimaryKeyRelatedField(queryset= Asiento.objects.all())
    tipo_comprobante = serializers.PrimaryKeyRelatedField(queryset= TipoComprobante.objects.all())
    comprobante = serializers.PrimaryKeyRelatedField(queryset= Comprobante.objects.all())


    class Meta:
        model = Registro
        fields = ('id', 
                  'cuenta',
                  'asiento', 
                  'numero_operacion',  
                  'concepto', 
                  'tipo_comprobante', 
                  'debe', 
                  'haber', 
                  'fecha_registro', 
                  'fecha_efectiva', 
                  'comprobante', 
                  'observaciones')
        

class PersoneriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Personeria
        fields = ('id','name')

    
class CondicionImpositivaSerializer(serializers.ModelSerializer):

    class Meta:
        model = CondicionImpositiva
        fields = ('id','name')


class EntidadSerializer(serializers.ModelSerializer):
    #Atributos relacionados, cuyos valores representan un foreingkey
    personeria = serializers.PrimaryKeyRelatedField(queryset= Personeria.objects.all())
    condicion_impositiva = serializers.PrimaryKeyRelatedField(queryset= CondicionImpositiva.objects.all())
    
    class Meta:
        model = Entidad
        fields = ('id', 
                  'name',
                  'personeria', 
                  'condicion_impositiva')


class TipoIdentificacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoIdentificacion
        fields = ('id','name')


class IdentificacionSerializer(serializers.ModelSerializer):
    #Atributos relacionados, cuyos valores representan un foreingkey
    tipo_identificacion = serializers.PrimaryKeyRelatedField(queryset= TipoIdentificacion.objects.all())
    entidad = serializers.PrimaryKeyRelatedField(queryset= Entidad.objects.all())
    
    class Meta:
        model = Identificacion
        fields = ('id', 
                  'identificador',
                  'tipo_identificacion', 
                  'entidad')


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ('id','name')

    
class MonedaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Moneda
        fields = ('id','denominacion')

    
class CuentaSerializer(serializers.ModelSerializer):
    #Atributos relacionados, cuyos valores representan un foreingkey
    entidad = serializers.PrimaryKeyRelatedField(queryset= Entidad.objects.all())
    categoria = serializers.PrimaryKeyRelatedField(queryset= Categoria.objects.all())
    moneda = serializers.PrimaryKeyRelatedField(queryset= Moneda.objects.all())
    
    class Meta:
        model = Cuenta
        fields = ('id', 
                  'name',
                  'entidad', 
                  'categoria',
                  'moneda')


class CuentaAsociadaSerializer(serializers.ModelSerializer):
    #Atributos relacionados, cuyos valores representan un foreingkey
    cuenta_asociente = serializers.PrimaryKeyRelatedField(queryset= Cuenta.objects.all())
    cuenta_asociada = serializers.PrimaryKeyRelatedField(queryset= Cuenta.objects.all())

    class Meta:
        model = CuentasAsociadas
        fields = ('id',
                  'cuenta_asociente',
                  'cuenta_asociada')


class RegistrosSerializer(serializers.ModelSerializer):
    #Atributos relacionados, cuyos valores representan un foreingkey
    cuenta = serializers.PrimaryKeyRelatedField(queryset=Cuenta.objects.all())

    class Meta:
        model = Retenciones
        fields = ('id',
                  'cuenta',
                  'valor',
                  'unidad',
                  'ultima_modificacion',
                  )


class RetencionesSerializer(serializers.ModelSerializer):
    #Atributos relacionados, cuyos valores representan un foreingkey
    cuenta = serializers.PrimaryKeyRelatedField(queryset= Cuenta.objects.all())

    class Meta:
        model = Retenciones
        fields = ('id', 
                  'cuenta',
                  'valor', 
                  'unidad',
                  'ultima_modificacion')


class AsientoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asiento
        fields = ('id','descripcion', 'fecha_registro')

    
class TipoComprobanteSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoComprobante
        fields = ('id','name')


class ComprobanteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comprobante
        fields = ('id','link_comprobante')


class CuentasAsociadasSerializer(serializers.ModelSerializer):
    #Atributos relacionados, cuyos valores representan un foreingkey
    cuenta_asociente = serializers.PrimaryKeyRelatedField(queryset= Cuenta.objects.all())
    cuenta_asociada = serializers.PrimaryKeyRelatedField(queryset= Cuenta.objects.all())

    class Meta:
        model = CuentasAsociadas
        fields = ('id','cuenta_asociente', 'cuenta_asociada')