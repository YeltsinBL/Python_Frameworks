# Python_Frameworks

Ejercicios de los diferentes frameworks que se utilizan con Python: Django vs Flask vs FastApi

## Fast API

Para  inciar el servidor se usa el comando:

```sh
uvicorn main:app --reload
```

Dependiendo el nombre del archivo y la intancia que hace referiencia al FastApi, cambian las palabras en el comando.

> Nota: En la consola entregará el puerto local:  `http://127.0.0.1:8000` y si se quiere ver la documentación se agrega al final el path "docs" quedando `http://127.0.0.1:8000/docs`.

Para realizar la encriptación del token se tuvo que instalar:

```sh
pip install "python-jose[cryptography]"
pip install "passlib[bcrypt]"
```

> Nota: El primero es necesario para verificar y generar los tokens de JWT. El segundo es para manejar los hashes de las contraseñas, los códigos de los algoritmos.

En la terminal del sistema se ejecuta lo siguiente:

```sh
openssl rand -hex 32
```

> Nota: se obtiene un número random que servirá como clave secreta para el JWT.
