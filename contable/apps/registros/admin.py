from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Personeria)
class PersoneriaAdmin(admin.ModelAdmin):
    # Campos en la tabla de personeria de la app registros
    list_display = ('id','name')

   
@admin.register(CondicionImpositiva)
class CondicionImpositivaAdmin(admin.ModelAdmin):
    # Campos en la tabla condicion_impositiva de la app registros
    list_display = ('id', 'name')

    
@admin.register(Entidad)
class EntidadAdmin(admin.ModelAdmin):
    # Campos en la tabla entidad de la app registros
    list_display = ('id', 
                  'name',
                  'personeria', 
                  'condicion_impositiva')


@admin.register(TipoIdentificacion)
class TipoIdentificacionAdmin(admin.ModelAdmin):
    # Campos en la tabla tipo_identificacion de la app registros
    list_display = ('id', 'name')

    
@admin.register(Identificacion)
class IdentificacionAdmin(admin.ModelAdmin):
    # Campos en la tabla identificacion de la app registros
    list_display = ('id', 
                  'identificador',
                  'tipo_identificacion', 
                  'entidad')
 

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    # Campos en la tabla categoria de la app registros
    list_display = ('id', 'name')

   
@admin.register(Moneda)
class MonedaAdmin(admin.ModelAdmin):
    # Campos en la tabla moneda de la app registros
    list_display = ('id', 'denominacion')


@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    # Campos en la tabla cuentade de la app registros
    list_display = ('id', 
                  'name',
                  'entidad', 
                  'categoria',
                  'moneda')
    

@admin.register(Retenciones)
class RetencionesAdmin(admin.ModelAdmin):
    # Campos en la tabla retenciones de la app registros
    list_display = ('id', 
                  'cuenta',
                  'valor', 
                  'unidad',
                  'ultima_modificacion')


@admin.register(Asiento)
class AsientoAdmin(admin.ModelAdmin):
    # Campos en la tabla asiento de la app registros
    list_display = ('id', 'descripcion', 'fecha_registro')


@admin.register(TipoComprobante)
class TipoComprobanteAdmin(admin.ModelAdmin):
    # Campos en la tabla tipo_comprobante de la app registros
    list_display = ('id', 'name')


@admin.register(Comprobante)
class ComprobanteAdmin(admin.ModelAdmin):
    # Campos en la tabla comprobante de la app registros
    list_display = ('id', 'link_comprobante')


@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    # Campos en la tabla registro de la app registros
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


@admin.register(CuentasAsociadas)
class CuentasAsociadasAdmin(admin.ModelAdmin):
    # Campos en la tabla cuentas_asociadas de la app registros
    list_display = ('id','cuenta_asociente', 'cuenta_asociada')


