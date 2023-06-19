from Utils.rw_data import get_data
from Utils.change_data import transform_data_class
from Class.Alumnos_Tutores import Alumnos_Tutores
from Class.Alumno import Alumno
from Class.Tutor import Tutor
from Class.Alumnos import Alumnos
from Class.Tutores import Tutores
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
    texto1 = "Alumnos primer año antes de tolerancia: " + str(len(alumnos_1ro)) + "\n"
    alumnos_tolerance = alumnos_1ro[int(len(alumnos_1ro) - len(alumnos_1ro)*tolerance):]
    alumnos_1ro = alumnos_1ro[:int(len(alumnos_1ro) - len(alumnos_1ro)*tolerance)]
    print("Alumnos primer año despues de tolerancia: ", len(alumnos_1ro))
    print("Alumnos primer año sacados por tolerancia: ", len(alumnos_tolerance))

    
    texto2 = "Alumnos primer año despues de tolerancia: " + str(len(alumnos_1ro)) + "\n"
    texto3 = "Alumnos primer año sacados por tolerancia: " + str(len(alumnos_tolerance))


    # ? ------------------------ Arbol de decisión ---------------------------
    #* Se crea la lista de alumnos que se van a asignar a tutores de primer año que necesiten acompañamiento en matematicas
    Alumnos_Asignacion = Alumnos()
    Alumnos_Asignacion_Solicitudes = Alumnos()

    for alumno in alumnos_1ro:
        if "NO ASIGNADO" not in alumno.get_solicitud_esp():
            Alumnos_Asignacion.add_alumno(alumno)
    
    for alumno in alumnos_segundo.get_alumnos():
        if "NO ASIGNADO" not in alumno.get_solicitud_esp():
            Alumnos_Asignacion.add_alumno(alumno)

    for alumno in alumnos_solicitudes.get_alumnos():
        if "NO ASIGNADO" not in alumno.get_solicitud_esp():
            Alumnos_Asignacion_Solicitudes.add_alumno(alumno)


    # Alumnos_Asignacion.print_alumnos()
    Alumnos_Asignacion.to_csv("Resource\Alumnos_Asignacion.csv")
    print("--------------------------------------------------------------------")
    # Alumnos_Asignacion_Solicitudes.print_alumnos()
    Alumnos_Asignacion_Solicitudes.to_csv("Resource\Alumnos_Asignacion_Solicitudes.csv")
    print("Total alumnos en asignación primer y segundo semestre: ", Alumnos_Asignacion.get_total())
    print("Total alumnos en asignación Solicitudes: ", Alumnos_Asignacion_Solicitudes.get_total())

    tutoresMate = tutoresC.get_AMate()
    tutoresAignacion = Tutores()

    for tutor in tutoresMate:
        tutoresAignacion.add_tutor(tutor)

    tutoresAignacion.to_csv("Resource\TutoresAsignacion.csv")

    print("Total tutores en asignación: ", tutoresAignacion.get_total())
    print("Total de Asignaciones: ", Alumnos_Asignacion.get_total() + Alumnos_Asignacion_Solicitudes.get_total())

    # Alumnos_Asignacion.print_alumnos()

    # i = 0
    # for alumno in Alumnos_Asignacion:
    #     alumno.print_alumno()
    #     i += 1
    #     if i == 10:
    #         break
    
    
    #* Se comienza el ciclo del arbol de desición

    # for alumno in Alumnos_Asignacion:


    return texto1 + texto2 + texto3