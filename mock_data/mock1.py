from apps.registros.models import *
from django.contrib.auth.models import User
from datetime import datetime

admin = User.objects.create_user("admin", password="contable1234", is_staff=True, is_superuser=True)

Rubro.objects.create(
    name="Activo"
)

Rubro.objects.create(
    name="Pasivo"
)

Rubro.objects.create(
    name="Perdidas"
)

Rubro.objects.create(
    name="Ganancias"
)

Categoria.objects.create(
    name="Disponibilidades",
)

Categoria.objects.create(
    name="Inversiones",
)

Categoria.objects.create(
    name="Deudores a Cobrar",
)

Categoria.objects.create(
    name="Cursos",
)

Categoria.objects.create(
    name="Cuentas a Pagar",
)

Categoria.objects.create(
    name="Gastos",
)

Categoria.objects.create(
    name="Alumnos",
)

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
    name="Responsable Inscripto",
    )

TipoIdentificacion.objects.create(
    name="DNI",
)

TipoIdentificacion.objects.create(
    name="CBU",
)

Moneda.objects.create(
    denominacion="Ars",
)

Moneda.objects.create(
    denominacion="u$s",
)

TipoComprobante.objects.create(
    name="A",
)

TipoComprobante.objects.create(
    name="B",
)

Entidad.objects.create(
    name="Inove",
    personeria=Personeria.objects.get(name="Juridica"),
    condicion_impositiva=CondicionImpositiva.objects.get(name="Responsable Inscripto"),
)


