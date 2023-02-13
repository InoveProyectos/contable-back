from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    # Campos en la tabla de registros
    list_display = ('id','name')

   
@admin.register(CondicionImpositiva)
class CondicionImpositivaAdmin(admin.ModelAdmin):
    # Campos en la tabla de registros
    list_display = ('id', 'name')

    
@admin.register(Entidad)
class EntidadAdmin(admin.ModelAdmin):
    # Campos en la tabla de registros
    list_display = ('id', 
                  'name',
                  'categoria', 
                  'condicion_impositiva')

    def categoria_id(self, obj):
        return obj.categoria.id
        
    def condicion_impositiva_id(self, obj):
        return obj.condicion_impositiva.id


@admin.register(TipoIdentificacion)
class TipoIdentificacionAdmin(admin.ModelAdmin):
    # Campos en la tabla de registros
    list_display = ('id', 'name')

    
@admin.register(Identificacion)
class IdentificacionAdmin(admin.ModelAdmin):
    # Campos en la tabla de registros
    list_display = ('id', 
                  'identificador',
                  'tipo_identificacion', 
                  'entidad')

    def tipo_identificacion_id(self, obj):
        return obj.tipo_identificacion.id
        
    def entidad_id(self, obj):
        return obj.entidad.id
   

@admin.register(TipoCuenta)
class TipoCuentaAdmin(admin.ModelAdmin):
    # Campos en la tabla de registros
    list_display = ('id', 'name')

   
@admin.register(Moneda)
class MonedaAdmin(admin.ModelAdmin):
    # Campos en la tabla de registros
    list_display = ('id', 'denominacion')


@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    # Campos en la tabla de registros
    list_display = ('id', 
                  'name',
                  'entidad', 
                  'tipo_cuenta',
                  'moneda')

    def entidad_id(self, obj):
        return obj.entidad.id

    def tipo_cuenta_id(self, obj):
        return obj.tipo_cuenta.id

    def moneda_id(self, obj):
        return obj.moneda.id
    

@admin.register(Retenciones)
class RetencionesAdmin(admin.ModelAdmin):
    # Campos en la tabla de registros
    list_display = ('id', 
                  'cuenta',
                  'valor', 
                  'unidad',
                  'ultima_modificacion')

    def cuenta_id(self, obj):
        return obj.cuenta.id


@admin.register(Asiento)
class AsientoAdmin(admin.ModelAdmin):
    # Campos en la tabla de registros
    list_display = ('id', 'descripcion', 'fecha_registro')


@admin.register(TipoComprobante)
class TipoComprobanteAdmin(admin.ModelAdmin):
    # Campos en la tabla de registros
    list_display = ('id', 'name')


@admin.register(Comprobante)
class ComprobanteAdmin(admin.ModelAdmin):
    # Campos en la tabla de registros
    list_display = ('id', 'link_comprobante')


@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    # Campos en la tabla de registros
    list_display = ('id', 
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


    def cuenta_id(self, obj):
        return obj.cuenta.id


    def asiento_id(self, obj):
        return obj.asiento.id


    def tipo_comprobante_id(self, obj):
        return obj.tipo_comprobante.id


    def comprobante_id(self, obj):
        return obj.comprobante.id


@admin.register(CuentasAsociadas)
class CuentasAsociadasAdmin(admin.ModelAdmin):
    # Campos en la tabla de registros
    list_display = ('id','cuenta_asociente', 'cuenta_asociada')


    def cuenta_asociente_id(self, obj):
        return obj.cuenta_asociente.id


    def cuenta_asociada_id(self, obj):
        return obj.cuenta_asociada.id

