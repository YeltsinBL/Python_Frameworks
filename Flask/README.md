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
```

## Procedimiento

- Se realizó todo en un solo archivo `main.py`.
