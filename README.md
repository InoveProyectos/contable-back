# contable-back

# Lanzar el backend
Desde docker:
```sh
docker-compose up
```

Desde django instalado en nuestra PC:
```sh

```

# Realizar las migraciones
```python
python manage.py migrate
python manage.py makemigrations
```

# Agregar datos mock
```bash
python manage.py shell < ../mock_data/mock1.py
```

# Django admin
Si lanzó el script de agregar datos ya contará con el siguiente usario creado en la DB:
```
usuario: admin
password: contable1234
```
Luego ingresar a:
```
http://127.0.0.1:8000/admin/
```

# Swager:
Ingresar a:
```
http://127.0.0.1:8000/api-docs/swagger
```

# APIs:
Todos los endpoints creados hasta el momento son para realizar el "CRUD" de la base de datos, y su URL base comienza con:
```
http://127.0.0.1:8000/api/v1.0/registros/crud/
```

Para mayor facilidad se puede explorar desde Swager o utilizando el administrador de Django.


# Autenticación
En teoría todas las APIs están libres, no se requieren algún tipo de autenticación para poder consultarlas tanto pode Swagger como por HTTP.