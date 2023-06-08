from Utils.rw_data import get_data
from Utils.change_data import transform_data_class
import pandas as pd
import matplotlib.pyplot as plt

def tree(tolerance=0.1):
    data = get_data("Resource\data.xlsx")
    #* Alumnos primer año, Alumnos segundo año, Alumnos solicitudes, Tutores
    alumnos_primero, alumnos_segundo, alumnos_solicitudes, tutoresC = transform_data_class(data)

    # ! Se cuenta la cantidad de alumnos que tiene ingreso PACE independiente de su año de ingreso
    # Recurso_paiepPace = alumnos_vae.get_PACE() + alumnos_pace.get_PACE() + alumnos_solicitudes.get_PACE()
    # print("Recursos Alumnos Pace: ", Recurso_paiepPace)

    #* Se cuentan la cantidad de Tutores que hacen acompañamiento a los alumnos PACE en area de matematicas
    Recurso_tutoresPace = tutoresC.get_AMate()
    # print("Recurso Tutores Matematica: ", len(Recurso_tutoresPace))

    #* Recurso Alumnos PACE Solicitudes
    Recurso_PaceExtra = alumnos_solicitudes.get_PACE()

    # Se quitan de los alumnos de primer año el tolerance% y se guardan los alumnos que se sacan en una lista
    alumnos_tolerance = []
    alumnos_1ro = alumnos_primero.get_alumnos()
    print("Alumnos primer año antes de tolerancia: ", len(alumnos_1ro))
    alumnos_tolerance = alumnos_1ro[int(len(alumnos_1ro) - len(alumnos_1ro)*tolerance):]
    alumnos_1ro = alumnos_1ro[:int(len(alumnos_1ro) - len(alumnos_1ro)*tolerance)]
    print("Alumnos primer año despues de tolerancia: ", len(alumnos_1ro))
    print("Alumnos primer año sacados por tolerancia: ", len(alumnos_tolerance))

    # alumnos_1ro[0].print_alumno()
    # alumnos_1ro[-1].print_alumno()

    # alumnos_tolerance[0].print_alumno()
    # alumnos_tolerance[-1].print_alumno()

    