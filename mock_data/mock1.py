from apps.registros.models import *
from django.contrib.auth.models import User
from datetime import datetime

admin = User.objects.create_user("admin", password="contable1234", is_staff=True, is_superuser=True)

Personeria.objects.create(
    name="Fisica",
    )

Personeria.objects.create(
    name="Juridica",
    )

CondicionImpositiva.objects.create(
    name="Consumidor Final",
    )

CondicionImpositiva.objects.create(
    name="Responsable inscripto",
    )

Entidad.objects.create(
    name="Hernan Contigiani",
    personeria=Personeria.objects.get(name="Fisica"),
    condicion_impositiva=CondicionImpositiva.objects.get(name="Consumidor Final"),
)

Entidad.objects.create(
    name="BBVA",
    personeria=Personeria.objects.get(name="Juridica"),
    condicion_impositiva=CondicionImpositiva.objects.get(name="Responsable inscripto"),
)


TipoIdentificacion.objects.create(
    name="DNI",
)

TipoIdentificacion.objects.create(
    name="CBU",
)

Identificacion.objects.create(
    identificador="11222333",
    tipo_identificacion=TipoIdentificacion.objects.get(name="DNI"),
    entidad=Entidad.objects.get(name="Hernan Contigiani"),
)

Identificacion.objects.create(
    identificador="0021154922154587",
    tipo_identificacion=TipoIdentificacion.objects.get(name="CBU"),
    entidad=Entidad.objects.get(name="BBVA"),
)

Categoria.objects.create(
    name="Alumno",
)

Categoria.objects.create(
    name="Banco",
)

Moneda.objects.create(
    denominacion="ARS",
)

Cuenta.objects.create(
    name="Alumno Hernan Contigiani",
    entidad=Entidad.objects.get(name="Hernan Contigiani"),
    categoria=Categoria.objects.get(name="Alumno"),
    moneda=Moneda.objects.get(denominacion="ARS"),
)

Cuenta.objects.create(
    name="Banco BBVA",
    entidad=Entidad.objects.get(name="BBVA"),
    categoria=Categoria.objects.get(name="Banco"),
    moneda=Moneda.objects.get(denominacion="ARS"),
)


