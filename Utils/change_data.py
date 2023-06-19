import sys
import os

from Utils.rw_data import get_data

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
        aux = especialidades(fila)

        alumno = Alumno(fila["RUT"], 
                        fila["NOMBRE COMPLETO"], 
                        fila["CARRERA"], 
                        fila["FACULTAD"], 
                        fila["VÍA PAIEP"], 
                        fila["IES ACOMPAÑAMIENTO"], 
                        fila["CORREO USACH"], 
                        fila["CORREO PERSONAL"], 
                        fila["TELÉFONO 1"], 
                        fila["TELÉFONO 2"], 
                        fila["MATRICULADOS 1s2023"],
                        [fila["ÁREA TUTOR 1"], fila["ÁREA TUTOR 2"], fila["ÁREA TUTOR 3"]],
                        [fila["SUBÁREA TUTOR 1"], fila["SUBÁREA TUTOR 2"], fila["SUBÁREA TUTOR 3"]],
                        aux)
        alumno.change_nivel(1)

        alumnos_vae.add_alumno(alumno)

    # alumnos_vae.print_alumnos()

    # alumnos_vae.get_alumno("21705466").print_alumno()

    for index, fila in pace.iterrows():

        aux = especialidades(fila)

        alumno = Alumno(fila["RUT"], 
                        fila["NOMBRE COMPLETO"], 
                        fila["CARRERA"], 
                        fila["FACULTAD"], 
                        fila["VÍA PAIEP"], 
                        fila["IES ACOMPAÑAMIENTO"], 
                        fila["CORREO USACH"], 
                        fila["CORREO PERSONAL"], 
                        fila["TELÉFONO 1"], 
                        fila["TELÉFONO 2"], 
                        fila["MATRICULADOS 1s2023"],
                        [fila["ÁREA TUTOR 1"], fila["ÁREA TUTOR 2"], fila["ÁREA TUTOR 3"]],
                        [fila["SUBÁREA TUTOR 1"], fila["SUBÁREA TUTOR 2"], fila["SUBÁREA TUTOR 3"]],
                        aux)
        alumnos_pace.add_alumno(alumno)
    # alumnos_pace.print_alumnos()

    for index, fila in solicitudes.iterrows():

        aux = especialidades(fila)


        alumno = Alumno(fila["RUT"], 
                        fila["NOMBRE COMPLETO"], 
                        fila["CARRERA"], 
                        fila["FACULTAD"],
                        fila["VÍA PAIEP"], 
                        fila["IES ACOMPAÑAMIENTO"], 
                        fila["CORREO USACH"], 
                        fila["CORREO PERSONAL"], 
                        fila["TELÉFONO 1"], 
                        fila["TELÉFONO 2"], 
                        fila["MATRICULADOS 1s2023"],
                        [fila["ÁREA TUTOR 1"], fila["ÁREA TUTOR 2"], fila["ÁREA TUTOR 3"]],
                        [fila["SUBÁREA TUTOR 1"], fila["SUBÁREA TUTOR 2"], fila["SUBÁREA TUTOR 3"]],
                        aux)
        alumnos_solicitudes.add_alumno(alumno)
    # alumnos_solicitudes.print_alumnos()

    for index, fila in tutores.iterrows():
        tutor = Tutor(fila["RUT"], 
                      fila["NOMBRE COMPLETO"], 
                      fila["CARRERA"], 
                      fila["FACULTAD"], 
                      fila["CORREO USACH"], 
                      fila["TELÉFONO 1"], 
                      fila["CORREO PERSONAL"], 
                      fila["ÁREA"], 
                      fila["SUB-ÁREA"], 
                      fila["HORAS"])
        tutoresC.add_tutor(tutor)
    # tutoresC.print_tutores()

    # tutoresC.get_tutor("20780420").print_tutor()

    return [alumnos_vae, alumnos_pace, alumnos_solicitudes, tutoresC]



def especialidades(fila):
    aux = []
    aux2 = []
    for i in range(1,4):
        # ! Aqui se pude editar para agregar mas especialidades
        # ? ------------------ ALGEBRA I Y CALCULO I ------------------
        if (fila["ESPECIALIDAD " + str(i)] == "ALGEBRA" 
                or fila["ESPECIALIDAD " + str(i)] == "ALGEBRA I" 
                or fila["ESPECIALIDAD " + str(i)] == "ALGEBRA I PARA INGENIERIA"
                or fila["ESPECIALIDAD " + str(i)] == "CALCULO I, ALGEBRA I"):
            aux.append("ALGEBRA I Y CALCULO I")
        
        # ? ----------------------- CALCULO I -------------------------
        elif (fila["ESPECIALIDAD " + str(i)] == "CALCULO" 
                or fila["ESPECIALIDAD " + str(i)] == "CALCULO I" 
                or fila["ESPECIALIDAD " + str(i)] == "CALCULO I PARA INGENIERIA"
                or fila["ESPECIALIDAD " + str(i)] == "CALCULO TECNO"):
            aux.append("CALCULO I") 

        # ? ----------------- ALGEBRA II Y CALCULO II -----------------
        elif (fila["ESPECIALIDAD " + str(i)] == "ALGEBRA II"
                or fila["ESPECIALIDAD " + str(i)] == "ALGEBRA II PARA INGENIERIA"
                or fila["ESPECIALIDAD " + str(i)] == "ALGEBRA LINEAL"):
            aux.append("ALGEBRA II Y CALCULO II")

        # ? ----------------------- CALCULO II ------------------------
        elif (fila["ESPECIALIDAD " + str(i)] == "CALCULO II"
                or (fila["ESPECIALIDAD " + str(i)] == "CALCULO AVANZADO" and fila["FACULTAD"] == "FACULTAD TECNOLOGICA")
                or fila["ESPECIALIDAD " + str(i)] == "CALCULO II PARA INGENIERIA"):
            aux.append("CALCULO II")

        # ? ----------------------- CALCULO III -----------------------
        elif ((fila["ESPECIALIDAD " + str(i)] == "CALCULO AVANZADO" and fila["FACULTAD"] != "FACULTAD TECNOLOGICA")
                or fila["ESPECIALIDAD " + str(i)] == "CALCULO III"
                or fila["ESPECIALIDAD " + str(i)] == "CALCULO III PARA INGENIERIA"):
            aux.append("CALCULO III")

        # ? ----------------------- MATEMATICAS I ------------------------
        elif (fila["ESPECIALIDAD " + str(i)] == "MATEMATICAS I"
                or fila["ESPECIALIDAD " + str(i)] == "MATEMATICAS PARA LA ADM. Y ECONOMIA I"
                or fila["ESPECIALIDAD " + str(i)] == "MATEMATICAS PARA LA ADMINISTRACION Y ECONOMIA I"):
            aux.append("MATEMATICA I")

        # ? ----------------------- MATEMATICAS II ------------------------
        elif (fila["ESPECIALIDAD " + str(i)] == "MATEMATICA PARA LA ADM. Y ECONOMIA II"
                or fila["ESPECIALIDAD " + str(i)] == "MATEMATICAS II"
                or fila["ESPECIALIDAD " + str(i)] == "MATEMATICAS PARA LA ADM. Y ECONOMIA II"
                or fila["ESPECIALIDAD " + str(i)] == "MATEMATICAS PARA LA ADMINISTRACION II"
                or fila["ESPECIALIDAD " + str(i)] == "MATEMATICAS PARA LA ADMINISTRACION Y ECONOMIA II"):
            aux.append("MATEMATICA II")

        # ? ----------------------- MATEMATICAS III ------------------------
        elif (fila["ESPECIALIDAD " + str(i)] == "MATEMATICA III"
                or fila["ESPECIALIDAD " + str(i)] == "MATEMATICAS III"
                or fila["ESPECIALIDAD " + str(i)] == "MATEMATICAS PARA LA ADM. Y ECONOMIA III"):
            aux.append("MATEMATICA III")

        # ? ----------------------- ECUACIONES DIFERENCIALES ------------------------
        elif (fila["ESPECIALIDAD " + str(i)] == "ECUACIONES DIFERENCIALES"
                or fila["ESPECIALIDAD " + str(i)] == "ECUACIONES DIFERENCIALES PARA INGENIERIA"
                or fila["ESPECIALIDAD " + str(i)] == "ECUACIONES DIFERENCIALES Y METODOS NUMERICOSA"):
            aux.append("ECUACIONES DIFERENCIALES")

        # ? ----------------------- ESTADISTICA Y PROBABILIDAD ------------------------
        elif (fila["ESPECIALIDAD " + str(i)] == "ANALISIS ESTADISTICO"
                or fila["ESPECIALIDAD " + str(i)] == "ANALISIS ESTADISTICO PARA INGENIERIA"
                or fila["ESPECIALIDAD " + str(i)] == "ESTADISTICA DESCRIPTIVA"
                or fila["ESPECIALIDAD " + str(i)] == "ESTADISTICA II"
                or fila["ESPECIALIDAD " + str(i)] == "ESTATICA APLICADA"):
            aux.append("ESTADISTICA Y PROBABILIDAD")

        # ? ----------------------- PENSAMIENTO MATEMATICO ------------------------
        elif (fila["ESPECIALIDAD " + str(i)] == "PENSAMIENTO MATEMATICO"):
            aux.append("PENSAMIENTO MATEMATICO")

        # ? ----------------------- ASIGNACIONES MANUALES ------------------------
        elif (fila["ESPECIALIDAD " + str(i)] == "PENSAMIENTO LOGICO MATEMATICO"
                or fila["ESPECIALIDAD " + str(i)] == "RAZONAMIENTO LOGICO-MATEMATICO"):
            aux.append("ASIGNAR MANUALMENTE")
        else:
            aux.append("NO ASIGNADO")
        
    # Eliminar repetidos en la lista auxiliar
    for i in aux:
        if (i not in aux2 and not(len(aux2) > 0 and i == "NO ASIGNADO")):
            aux2.append(i)

    return aux2



def test():
    data = get_data("Resource\data.xlsx")
    data2 = transform_data_class(data)
    
