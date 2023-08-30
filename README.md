# Asignaciones_2.0

## Instalación

Se deben instalar los siguientes paquetes de python para que el proyecto funcione correctamente:

```bash
pip install numpy
pip install matplotlib
pip install pandas
pip install pyqt5
pip install openpyxl

```

## Uso

Para ejecutar el programa se debe correr el archivo main.py

```bash
python main.py
```

## Estrucutra del proyecto

El proyecto se divide en 4 carpetas principales:

- **Resource**: Este directorio contiene los archivos .xlsx y .csv que se utilizan para la extracción de datos.
- **Class**: Este directorio contiene las clases que se utilizan para el almacenamiento de los datos extraidos desde el directorio de Resource.
- **Interface**: Este directorio contiene los archivos python que se dedican a la interfaz grafica
- **Utils**: Este directorio contiene los archivos python puramente funcional que se dedican a lectura, escritura y procesamiento de datos.

## Estructura de los datos Ingresados

El excel de donde se leerán los datos debe seguir el siguiente formato (Se debe Seguir el nombre de los encabezados de las columnas, no es necesario que se llamen de la misma forma):

En el caso para los datos de los estudiantes:

|RUT_USACH|DV|NOMBRE COMPLETO|NOMBRE SOCIAL|CARRERA|UNIDAD ACADÉMICA|VÍA DE ACCESO|VÍA PAIEP|IES ACOMPAÑAMIENTO|CORREO USACH|CORREO PERSONAL|TELÉFONO 1|TELÉFONO 2|MATRICULADO 1s2023 (SI/NO)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|

y seguido de estas columnas, en las columnas con indice de la 14 a la 16, 23 a la 25 y 32 a la 34, se deben ingresar los datos de la solicitud de los tutores, en el siguiente formato:

|ÁREA TUTOR/A *N*|SUBÁREA TUTOR/A *N*|ESPECIALIDAD|
|---|---|---|

donde *N* debe ser un numero entero que va desde 1 hasta 3.

Para el caso de los tutores, el excel debe seguir el siguiente formato:

|RUT|NOMBRE COMPLETO|CARRERA|FACULTAD|CORREO USACH|TELÉFONO TUTOR/A|CORREO PERSONAL|ÁREA|Subárea|N° de horas|
|---|---|---|---|---|---|---|---|---|---|

