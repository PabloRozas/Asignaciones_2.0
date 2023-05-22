import sys
import os

from rw_data import get_data

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

    alumnos_vae = Alumnos()
    alumnos_pace = Alumnos()
    alumnos_solicitudes = Alumnos()
    tutoresC = Tutores()


    for index, fila in vae.iterrows():
        alumno = Alumno(fila["RUT"], fila["NOMBRE COMPLETO"], fila["CARRERA"], fila["FACULTAD"], fila["VÍA DE ACCESO"], fila["VÍA PAIEP"], fila["IES ACOMPAÑAMIENTO"], fila["CORREO USACH"], fila["CORREO PERSONAL"], fila["TELÉFONO 1"], fila["TELÉFONO 2"], fila["MATRICULADOS 1s2023"])
        alumnos_vae.add_alumno(alumno)
    # alumnos_vae.print_alumnos()

    for index, fila in pace.iterrows():
        alumno = Alumno(fila["RUT"], fila["NOMBRE COMPLETO"], fila["CARRERA"], fila["FACULTAD"], fila["VÍA DE ACCESO"], fila["VÍA PAIEP"], fila["IES ACOMPAÑAMIENTO"], fila["CORREO USACH"], fila["CORREO PERSONAL"], fila["TELÉFONO 1"], fila["TELÉFONO 2"], fila["MATRICULADOS 1s2023"])
        alumnos_pace.add_alumno(alumno)
    # alumnos_pace.print_alumnos()

    for index, fila in solicitudes.iterrows():
        alumno = Alumno(fila["RUT"], fila["NOMBRE COMPLETO"], fila["CARRERA"], fila["FACULTAD"], fila["VÍA DE ACCESO"], fila["VÍA PAIEP"], fila["IES ACOMPAÑAMIENTO"], fila["CORREO USACH"], fila["CORREO PERSONAL"], fila["TELÉFONO 1"], fila["TELÉFONO 2"], fila["MATRICULADOS 1s2023"])
        alumnos_solicitudes.add_alumno(alumno)
    # alumnos_solicitudes.print_alumnos()

    for index, fila in tutores.iterrows():
        tutor = Tutor(fila["RUT"], fila["NOMBRE COMPLETO"], fila["CARRERA"], fila["FACULTAD"], fila["CORREO USACH"], fila["TELÉFONO 1"], fila["CORREO PERSONAL"], fila["ÁREA"], fila["SUB-ÁREA"], fila["HORAS"])
        tutoresC.add_tutor(tutor)
    # tutoresC.print_tutores()



def test():
    data = get_data("Resource\data.xlsx")
    transform_data_class(data)

test()