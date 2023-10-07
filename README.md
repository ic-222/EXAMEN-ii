![image](https://github.com/ic-222/EXAMEN-ii/assets/136537533/21152cf5-bc1f-413e-b881-857bb39b33c3)



Esta lista de tareas es una aplicación web simple construida con Flask, un marco de desarrollo web de Python. Permite a los usuarios crear tareas, marcarlas como completadas y eliminarlas de la lista. La aplicación utiliza una base de datos MS Access para almacenar las tareas.

# Requisitos
Será necesario tener instalado en el sistema pip, Python y *añadirlo al path*, git y un editor de código para poder configurar la app.

## Pasos para usarla

### Clonar el repositorio
Para comenzar, clona el repositorio de GitHub a tu máquina local usando el siguiente comando en una terminal o línea de comandos de git bash que abras dentro de la ubicación de tu preferencia:

```bash
git clone https://github.com/ic-222/EXAMEN-ii
```

### Instalar Requerimientos
Ubícate en la carpeta donde clonaste el repositorio y ejecuta el siguiente comando, así conseguiras todos los módulos usados para que funcione la app

```bash
pip install -r requirements.txt
```

## Configuración de la app
Cambia la Ruta de la Base de Datos:
Abre el archivo config.py en el directorio raíz del proyecto. Encuentra la línea que contiene DATABASE_CONNECTION_STRING y cambia la ruta del archivo .accdb para que coincida con la ubicación de tu base de datos MS Access en tu sistema local.

```python
DATABASE_CONNECTION_STRING = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=TU_RUTA.accdb;'
```

# Ejecutando la aplicación...

En la terminal usa el siguiente comando:

``` bash
python __init__.py
```

La aplicación se ejecutará en http://localhost:5000/. Abre tu navegador web y visita esa dirección para ver la aplicación de Lista de Tareas en acción.


*_Ivanna S. Cervantes A. 2023*_
