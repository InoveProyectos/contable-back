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
    

@admin.register(Retenciones)
class RetencionesAdmin(admin.ModelAdmin):
    # Campos en la tabla de registros
    list_display = ('id', 
                  'cuenta',
                  'valor', 
                  'unidad',
                  'ultima_modificacion')


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


@admin.register(CuentasAsociadas)
class CuentasAsociadasAdmin(admin.ModelAdmin):
    # Campos en la tabla de registros
    list_display = ('id','cuenta_asociente', 'cuenta_asociada')


