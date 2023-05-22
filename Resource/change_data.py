import sys
import os

# Obtiene la ruta absoluta de la carpeta actual
current_folder = os.path.dirname(os.path.abspath(__file__))
# print(current_folder)
# Construye la ruta de la carpeta Class
class_folder = os.path.abspath(os.path.join(current_folder, '..', 'Class'))
# print(class_folder)
# Agrega la ruta de la carpeta Class al sistema de búsqueda de módulos
sys.path.append(class_folder)

import pandas as pd


# Se importan las clases que se van a utilizar
from Alumno import Alumno
from Alumnos import Alumnos
from Tutor import Tutor
from Tutores import Tutores
  
""" transform_data_class """
"""
Definición: Transforma la lista que contiene los DataFrames leidos a los objetos de las clases correspondientes
Entrada: data (lista de DataFrames donde 0: VAE, 1: PACE, 2: Solicitudes, 3: Tutores)
Salida: alumnos (objeto Alumnos) y tutores (objeto Tutores)
"""
def transform_data_class(data):
    vae = data[0]
    pace = data[1]
    solicitudes = data[2]
    tutores = data[3]

    for index, fila in vae.iterrows():
        print(index)
        print(fila["RUT"])
        



