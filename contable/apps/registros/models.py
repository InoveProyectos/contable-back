from django.db import models


# Create your models here.
class Personeria(models.Model):
    '''Esta clase hereda de Django models.Model y crea una tabla llamada
    personaria'''

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60)   

    class Meta:
        db_table = 'personeria'

    def __str__(self):
        return f'{self.name}'


class CondicionImpositiva(models.Model):
    '''Esta clase hereda de Django models.Model y crea una tabla llamada
    condicion_impositiva'''

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60)   

    class Meta:
        db_table = 'condicion_impositiva'

    def __str__(self):
        return f'{self.name}'


class Entidad(models.Model):
    '''Esta clase hereda de Django models.Model y crea una tabla llamada
    entidad'''

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60) 
    personeria = models.ForeignKey(Personeria, on_delete=models.CASCADE)
    condicion_impositiva = models.ForeignKey(CondicionImpositiva, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'entidad'

    def __str__(self):
        return f'{self.name}, {self.personeria}, {self.condicion_impositiva}'


class TipoIdentificacion(models.Model):
    '''Esta clase hereda de Django models.Model y crea una tabla llamada
    tipo_identificacion'''

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60)   

    class Meta:
        db_table = 'tipo_identificacion'

    def __str__(self):
        return f'{self.name}'


# Clase que tiene foreingkey de la clase Entidad y TipoIdentificacion.
class Identificacion(models.Model):
    '''Esta clase hereda de Django models.Model y crea una tabla llamada
    identificacion'''

    id = models.BigAutoField(primary_key=True)
    identificador = models.CharField(max_length=60) 
    tipo_identificacion = models.ForeignKey(TipoIdentificacion, on_delete=models.CASCADE)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'identificacion'

    def __str__(self):
        return f'{self.identificador}, {self.tipo_identificacion}, {self.entidad}'


class Categoria(models.Model):
    '''Esta clase hereda de Django models.Model y crea una tabla llamada
    categoria: 
                Alumno
                Empleado
                Banco
                Proveedor
    '''

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60)   

    class Meta:
        db_table = 'categoria'

    def __str__(self):
        return f'{self.name}'


class Moneda(models.Model):
    '''Esta clase hereda de Django models.Model y crea una tabla llamada
    moneda'''

    id = models.BigAutoField(primary_key=True)
    denominacion = models.CharField(max_length=60)   

    class Meta:
        db_table = 'moneda'

    def __str__(self):
        return f'{self.denominacion}'


# Clase que tiene foreingkey de la clase Entidad, Categoria y Moneda.
class Cuenta(models.Model):
    '''Esta clase hereda de Django models.Model y crea una tabla llamada
    cuenta'''

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60)     
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)
   
    class Meta:
        db_table = 'cuenta'

    def __str__(self):
        return f'{self.id},{self.name}, {self.entidad}, {self.categoria}, {self.moneda}'


class Retenciones(models.Model):
    '''Esta clase hereda de Django models.Model y crea una tabla llamada
    retenciones'''

    id = models.BigAutoField(primary_key=True)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    valor = models.FloatField(default=0) 
    unidad = models.CharField(max_length=10)
    ultima_modificacion = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = 'retenciones'

    def __str__(self):
        return f'{self.cuenta}, {self.valor}, {self.unidad}, {self.ultima_modificacion}'


class Asiento(models.Model):
    '''Esta clase hereda de Django models.Model y crea una tabla llamada
    asiento'''

    id = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=300, default="", blank=True)
    fecha_registro = models.DateTimeField()
  
    class Meta:
        db_table = 'asiento'

    def __str__(self):
        return f'{self.descripcion}, {self.fecha_registro}'


class TipoComprobante(models.Model):
    '''Esta clase hereda de Django models.Model y crea una tabla llamada
    tipo_comprobante'''

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60, default=None, blank=True, null=True)     
       
    class Meta:
        db_table = 'tipo_comprobante'

    def __str__(self):
        return f'{self.name}'


class Comprobante(models.Model):
    '''Esta clase hereda de Django models.Model y crea una tabla llamada
    comprobante'''

    id = models.BigAutoField(primary_key=True)
    link_comprobante = models.CharField(max_length=350, default=None, blank=True, null=True)  # Add max_length
       
    class Meta:
        db_table = 'comprobante'

    def __str__(self):
        return f'{self.link_comprobante}'


# Clase que tiene foreingkey de la clase Cuenta, Asiento, TipoComprobante y Comprobante.
class Registro(models.Model):
    '''Esta clase hereda de Django models.Model y crea una tabla llamada
    registro'''

    id = models.BigAutoField(primary_key=True)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    asiento = models.ForeignKey(Asiento, on_delete=models.CASCADE)
    numero_operacion = models.CharField(max_length=100, default="") 
    concepto = models.CharField(max_length=150)
    tipo_comprobante = models.ForeignKey(TipoComprobante, on_delete=models.CASCADE, default=None, blank=True, null=True)
    debe = models.FloatField(default=0)
    haber = models.FloatField(default=0)
    fecha_registro = models.DateTimeField()
    fecha_efectiva = models.DateTimeField()
    comprobante = models.ForeignKey(Comprobante, on_delete=models.CASCADE, default=None, blank=True, null=True)    
    observaciones = models.CharField(max_length=300, default='')        
     
    class Meta:
        db_table = 'registro'

    def __str__(self):
        return f'{self.cuenta}, {self.asiento}, {self.numero_operacion}, {self.concepto},{self.tipo_comprobante}, {self.debe}, {self.haber}, {self.fecha_registro}, {self.fecha_efectiva}'


# Tabla auxiliar, relación |muchos --> muchos|
class CuentasAsociadas(models.Model):
    '''Esta clase hereda de Django models.Model y crea una tabla llamada
    cuentas_asociadas'''

    id = models.BigAutoField(primary_key=True)
    cuenta_asociente = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='cuenta_asociente_set') # _set debe estar siempre
    cuenta_asociada = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='cuena_asociada_set')


    def save(self, *args, **kwargs):
        # Verificar si cuenta_asociente_id es diferente a cuenta_asociada_id

        if self.cuenta_asociente != self.cuenta_asociada:
            # Guardar los cambios
            super().save(*args, **kwargs)
        else:
            raise ValueError('cuenta_asociente_id es igual a cuenta_asociada_id')

    class Meta:
        db_table = 'cuentas_asociadas'

    def __str__(self):
        return f'{self.cuenta_asociente}, {self.cuenta_asociada}'