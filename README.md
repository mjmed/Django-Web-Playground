# Web Playground

## *Curso Práctico de Django con Python: Desarrollo Web Backend*

**Web Playground** un proyecto avanzado y de especialización, centrado puramente en el backend. Permite manejar autenticación y registro de usuarios, crear secciones internas sólo para usuarios identificados, perfiles de usuario y lo mejor de todo: un sistema de mensajería privada.

Incluye:
+ **Django Templates**
+ Entorno virtual con **Pipenv**
+ Personalización del panel administrador de _Django_
+ **CBV: _Class Based Views_**
+ **CRUD** con **_Generic Views_**
+ **_Mixin_** y **_Decorator_**
+ **_Signals_**
+ Pruebas unitarias
+ **TDD: Desarrollo Guiado por Pruebas**

### Librerías y paquetes utilizados:
- [**Django CKEditor**](https://django-ckeditor.readthedocs.io/en/latest/): editor de texto tipo _word_ para campos _TextField_.

### Versión: 1.0.0

### Notas:
Comando para activar el entorno virtual:
```
pipenv shell
```

Comando para ver todos los paquetes (con sus dependencias) instaladas:
```
pip list --local
```
o
```
pipenv graph
```

Comando para instalar las dependencias del proyecto desde el fichero requirements.txt (con el entorno virtual activado):
```
pip install -r requirements.txt
```

Comando para crear o actualizar el fichero requirements.txt (con el entorno virtual activado):
```
pip freeze > requirements.txt
```

Comando para ejecutar el servidor en desarrollo:
```
python manage.py runserver
```

Incluir en la raíz del directorio la carpeta **media** con la subcarpeta **profiles**.
```
˅ media
    > profiles
```
