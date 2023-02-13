# Se imporat modelos
from ..models import *
# Se importa los serializadores de Django
from rest_framework import serializers, status
from rest_framework.response import Response


class RegistroSerializer(serializers.ModelSerializer):
    #Atributos relacionados, cuyos valores representan un foreingkey
    cuenta = serializers.PrimaryKeyRelatedField(write_only=True, queryset= Cuenta.objects.all())
    asiento = serializers.PrimaryKeyRelatedField(write_only=True, queryset= Asiento.objects.all())
    tipo_comprobante = serializers.PrimaryKeyRelatedField(write_only=True, queryset= TipoComprobante.objects.all())
    comprobante = serializers.PrimaryKeyRelatedField(write_only=True, queryset= Comprobante.objects.all())


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



class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ('id','name')

    
class CondicionImpositivaSerializer(serializers.ModelSerializer):

    class Meta:
        model = CondicionImpositiva
        fields = ('id','name')


class EntidadSerializer(serializers.ModelSerializer):
    #Atributos relacionados, cuyos valores representan un foreingkey
    categoria = serializers.PrimaryKeyRelatedField(write_only=True, queryset= Categoria.objects.all())
    condicion_impositiva = serializers.PrimaryKeyRelatedField(write_only=True, queryset= CondicionImpositiva.objects.all())
    
    class Meta:
        model = Entidad
        fields = ('id', 
                  'name',
                  'categoria', 
                  'condicion_impositiva')


class TipoIdentificacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoIdentificacion
        fields = ('id','name')


class IdentificacionSerializer(serializers.ModelSerializer):
    #Atributos relacionados, cuyos valores representan un foreingkey
    tipo_identificacion = serializers.PrimaryKeyRelatedField(write_only=True, queryset= TipoIdentificacion.objects.all())
    entidad = serializers.PrimaryKeyRelatedField(write_only=True, queryset= Entidad.objects.all())
    
    class Meta:
        model = Identificacion
        fields = ('id', 
                  'identificador',
                  'tipo_identificacion', 
                  'entidad')


class TipoCuentaSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoCuenta
        fields = ('id','name')

    
class MonedaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Moneda
        fields = ('id','denominacion')

    
class CuentaSerializer(serializers.ModelSerializer):
    #Atributos relacionados, cuyos valores representan un foreingkey
    entidad = serializers.PrimaryKeyRelatedField(write_only=True, queryset= Entidad.objects.all())
    tipo_cuenta = serializers.PrimaryKeyRelatedField(write_only=True, queryset= TipoCuenta.objects.all())
    moneda = serializers.PrimaryKeyRelatedField(write_only=True, queryset= Moneda.objects.all())
    
    class Meta:
        model = Cuenta
        fields = ('id', 
                  'name',
                  'entidad', 
                  'tipo_cuenta',
                  'moneda')


class RetencionesSerializer(serializers.ModelSerializer):
    #Atributos relacionados, cuyos valores representan un foreingkey
    cuenta = serializers.PrimaryKeyRelatedField(write_only=True, queryset= Cuenta.objects.all())

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
        fields = ('id','descipcion', 'fecha_registro')

    
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
    cuenta_asociente = serializers.PrimaryKeyRelatedField(write_only=True, queryset= Cuenta.objects.all())
    cuenta_asociada = serializers.PrimaryKeyRelatedField(write_only=True, queryset= Cuenta.objects.all())

    class Meta:
        model = CuentasAsociadas
        fields = ('id','cuenta_asociente', 'cuenta_asociada')