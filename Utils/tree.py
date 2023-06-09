from Utils.rw_data import get_data
from Utils.change_data import transform_data_class
import pandas as pd
import matplotlib.pyplot as plt

def tree(tolerance=0.1):

    # ? ------------------------------ Carga de datos ------------------------------
    data = get_data("Resource\data.xlsx")
    #* Alumnos primer año, Alumnos segundo año, Alumnos solicitudes, Tutores
    alumnos_primero, alumnos_segundo, alumnos_solicitudes, tutoresC = transform_data_class(data)

    #* Se cuentan la cantidad de Tutores que hacen acompañamiento a los alumnos PACE en area de matematicas
    Recurso_tutoresMATE = tutoresC.get_AMate()
    # print("Recurso Tutores Matematica: ", len(Recurso_tutoresPace))

    #* Recurso Alumnos PACE Solicitudes
    Recurso_PaceExtra = alumnos_solicitudes.get_PACE()

    # ? ------------------------ Creación de entrada para el arbol de desición ---------------------------
    # Se quitan de los alumnos de primer año el tolerance% y se guardan los alumnos que se sacan en una lista
    alumnos_tolerance = []
    alumnos_1ro = alumnos_primero.get_alumnos()
    print("Alumnos primer año antes de tolerancia: ", len(alumnos_1ro))
    alumnos_tolerance = alumnos_1ro[int(len(alumnos_1ro) - len(alumnos_1ro)*tolerance):]
    alumnos_1ro = alumnos_1ro[:int(len(alumnos_1ro) - len(alumnos_1ro)*tolerance)]
    print("Alumnos primer año despues de tolerancia: ", len(alumnos_1ro))
    print("Alumnos primer año sacados por tolerancia: ", len(alumnos_tolerance))

    # ? ------------------------ Arbol de decisión ---------------------------
    #* Se crea la lista de alumnos que se van a asignar a tutores
    Alumnos_Asignacion = alumnos_1ro

    for alumno in alumnos_segundo.get_alumnos():
        Alumnos_Asignacion.append(alumno)
    
    # i = 0
    # for alumno in Alumnos_Asignacion:
    #     alumno.print_alumno()
    #     i += 1
    #     if i == 10:
    #         break
    
    
    #* Se comienza el ciclo del arbol de desición

        

