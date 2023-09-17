# Flask

- Para correr y depurar la aplicación se utiliza el siguiente comando:

```sh
# Correr
flask --app nombre_archivo_ejecutar run
# Depurar
flask --app nombre_archivo_ejecutar run --debug
```

## Instalaciones

- Crear y activar el entorno virtual.
- Instalar Flask.
- Instalar Flask-SQLAlchemy.
- Instalar PyMySQL
- Instalar Marshmallow
- Instalar Dotenv

```sh
# Instalar entorno virtual
py -m venv env
# Activar entorno virtual
.\env\Scripts\activate
# Instalar Flask
pip install Flask
# Instalar SQLAlchemy
pip install -U Flask-SQLAlchemy
# Instalar PyMySQL
pip install pymysql
# Instalar Marshmallow
pip install flask_marshmallow marshmallow-sqlalchemy
# Instalar Dotenv
pip install python-dotenv
```

## Procedimiento

- Se realizó todo en un solo archivo `main.py`.
- Se procedió a separar el código en carpetas y archivos

### DB

- Client: se crearon las variables de SQLAlchemy y Marshmallow.
- Models:

  - User: modelo de usuario para que cree automáticamente la tabla en la BD.
- Schemas:

  - User: formato a las respuestas de los apis.

### Flask (principal)

- config: se realizó las configuraciones para la BD (conexión y evitar errores).
- main: configuración del sistema.
- __init__: configuración cuando inicia del sitema.

### Routers

- Users: rutas (path) de las apis de usuario.
