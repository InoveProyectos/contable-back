from django.db import models


# Create your models here.
class TipoEntidad(models.Model):
    '''Esta clase hereda de Django models.Model y crea una tabla llamada
    tipo_entidad'''

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60)   

    class Meta:
        db_table = 'tipo_entidad'

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
    tipo_entidad = models.ForeignKey(TipoEntidad, on_delete=models.CASCADE)
    condicion_impositiva = models.ForeignKey(CondicionImpositiva, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'entidad'

    def __str__(self):
        return f'{self.name}, {self.tipo_entidad}, {self.condicion_impositiva}'


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


class TipoCuenta(models.Model):
    '''Esta clase hereda de Django models.Model y crea una tabla llamada
    tipo_cuenta'''

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60)   

    class Meta:
        db_table = 'tipo_cuenta'

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


# Clase que tiene foreingkey de la clase Entidad, TipoCuenta y Moneda.
class Cuenta(models.Model):
    '''Esta clase hereda de Django models.Model y crea una tabla llamada
    cuenta'''

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60)     
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    tipo_cuenta = models.ForeignKey(TipoCuenta, on_delete=models.CASCADE)
    moneda = models.ForeignKey(Moneda, on_delete=models.CASCADE)
   
    class Meta:
        db_table = 'cuenta'

    def __str__(self):
        return f'{self.name}, {self.entidad}, {self.tipo_cuenta}, {self.moneda}'


class Asiento(models.Model):
    '''Esta clase hereda de Django models.Model y crea una tabla llamada
    asiento'''

    id = models.BigAutoField(primary_key=True)
    descripcion = models.CharField(max_length=300)
    fecha_registro = models.DateTimeField()
  
    class Meta:
        db_table = 'asiento'

    def __str__(self):
        return f'{self.descripcion}, {self.fecha_registro}'


class TipoComprobante(models.Model):
    '''Esta clase hereda de Django models.Model y crea una tabla llamada
    tipo_comprobante'''

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60)     
       
    class Meta:
        db_table = 'tipo_comprobante'

    def __str__(self):
        return f'{self.name}'


class Comprobante(models.Model):
    '''Esta clase hereda de Django models.Model y crea una tabla llamada
    comprobante'''

    id = models.BigAutoField(primary_key=True)
    link_comprobante = models.CharField(default=None)     
       
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
    asiento = models.ForeignKey(Asiento, on_delete=models.CASCADE, default=None)
    numero_operacion = models.PositiveIntegerField(default="") 
    concepto = models.CharField(max_length=150)
    tipo_comprobante = models.ForeignKey(TipoComprobante, on_delete=models.CASCADE)
    debe = models.FloatField(default=0)
    haber = models.FloatField(default=0)
    fecha_registro = models.DateTimeField()
    fecha_efectiva = models.DateTimeField()
    comprobante = models.ForeignKey(Comprobante, on_delete=models.CASCADE)    
    observaciones = models.CharField(max_length=300, default='')        

    class Meta:
        db_table = 'registro'

    def __str__(self):
        return f'{self.cuenta}, {self.asiento}, {self.numero_operacion}, {self.concepto},{self.tipo_comprobante}, {self.debe}, {self.haber}, {self.fecha_registro}, {self.fecha_efectiva}'


