from Utils.rw_data import get_data, asiganacion_to_excel, warning_data
from Utils.change_data import transform_data_class
from Class.Alumnos_Tutores import Alumnos_Tutores
from Class.Alumno import Alumno
from Class.Tutor import Tutor
from Class.Alumnos import Alumnos
from Class.Tutores import Tutores
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import os

def tree(tolerance=0.1, opcion = False, opcion2 = False, opcion3 = False, path = "Resource\data.xlsx"):
    error = ""
    # ? ------------------------------ Carga de datos ------------------------------
    try:
        data = get_data(path, opcion1= opcion2)
    except:
        if not os.path.exists("Resource"):
            os.makedirs("Resource")
        return ["", "", "Error al cargar los datos, modifique la ruta del archivo o agregue excel a la carpeta Resource"]
    if opcion2:
        
        if not os.path.exists("Resource\PACE"):
            os.makedirs("Resource\PACE")
        if not os.path.exists("Resource\Tutores"):
            os.makedirs("Resource\Tutores")
        if not os.path.exists("Resource\VAE"):
            os.makedirs("Resource\VAE")
        if not os.path.exists("Resource\Solicitudes"):
            os.makedirs("Resource\Solicitudes")    
    
        # Se transforman los datos en csv
        data[0].to_csv("Resource\Alumnos.csv")
        data[1].to_csv("Resource\AlumnosSegundo.csv")
        data[2].to_csv("Resource\AlumnosSolicitudes.csv")
        data[3].to_csv("Resource\Tutores.csv")
    #* Alumnos primer año, Alumnos segundo año, Alumnos solicitudes, Tutores

    warnings = ""
    if opcion3:
        warnings = warning_data(data)


    alumnos_primero, alumnos_segundo, alumnos_solicitudes, tutoresC = transform_data_class(data)

    # ? ------------------------ Creación de entrada para el arbol de desición (tolerancia)---------------------------
    # Se crea la tolerancia en tutores
    if (tolerance > 0):
        tutores_tolerance = []
        tutoresMate = Tutores()
        for tutor in tutoresC.get_AMate():
            tutoresMate.add_tutor(tutor)
        tutoresMate.get_TutoresBH()
        tutoresMate = tutoresMate.get_tutores()
        
        # Se calcula la cantidad de tutores que se van a sacar por tolerancia
        tutores_tolerance = tutoresMate[int(len(tutoresMate) - len(tutoresMate)*tolerance):]
        
        tutoresMate = tutoresMate[:int(len(tutoresMate) - len(tutoresMate)*tolerance)]


    else:
        tutoresMate = tutoresC.get_AMate()

    # ? ------------------------ Arbol de decisión ---------------------------
    #* Se crea la lista de alumnos que se van a asignar a tutores de primer año que necesiten acompañamiento en matematicas
    Alumnos_Asignacion_primerSem = Alumnos()
    Alumnos_Asignacion_segundoSem = Alumnos()
    Alumnos_Asignacion_Solicitudes = Alumnos()

    for alumno in alumnos_primero.get_alumnos():
        if "NO ASIGNADO" not in alumno.get_solicitud_esp():
            Alumnos_Asignacion_primerSem.add_alumno(alumno)
    
    for alumno in alumnos_segundo.get_alumnos():
        if "NO ASIGNADO" not in alumno.get_solicitud_esp():
            Alumnos_Asignacion_segundoSem.add_alumno(alumno)

    for alumno in alumnos_solicitudes.get_alumnos():
        if "NO ASIGNADO" not in alumno.get_solicitud_esp():
            Alumnos_Asignacion_Solicitudes.add_alumno(alumno)

    
    tutoresAsignacion = Tutores()

    for tutor in tutoresMate:
        tutoresAsignacion.add_tutor(tutor)


    #* Se comienza el ciclo del arbol de desición
    asignaciones_primerSem = Alumnos_Tutores()
    asignaciones_segundoSem = Alumnos_Tutores()
    asignaciones_solicitudes = Alumnos_Tutores()

    for alumno in Alumnos_Asignacion_primerSem.get_alumnos():
        if alumno.get_estado() == 0:
            # Se crea el grupo de tutores para la persona
            grupo_tutores = Tutores()
            for tutor in tutoresAsignacion.get_tutores():
                if (alumno.get_solicitud_esp()[0] in tutor.get_subarea()) and (tutor.get_asign() != 2):
                    grupo_tutores.add_tutor(tutor)
            # Se ordena de menor a mayor los tutores segun el largo de su lista de subareas
            grupo_tutores.sort_tutores()
            
            for tutor in grupo_tutores.get_tutores():
                if (len(tutor.get_ramosAsignados()) < 2):
                    if tutor.get_carrera() == alumno.get_carrera():
                        if tutor.get_cantTutorados() > 0:
                            alumno.change_asignado()
                            tutor.agregar_ramo(alumno.get_solicitud_esp()[0])
                            tutor.set_cantTutorados(tutor.get_cantTutorados() - alumno.get_peso())
                            tutor.asign()
                            asignaciones_primerSem.add_alumno_tutor(alumno, tutor)

                            break
                        else:
                            continue
                    else:
                        if tutor.get_facultad() == alumno.get_facultad():
                            if tutor.get_cantTutorados() > 0:
                                alumno.change_asignado()
                                tutor.agregar_ramo(alumno.get_solicitud_esp()[0])
                                tutor.set_cantTutorados(tutor.get_cantTutorados() - alumno.get_peso())
                                tutor.asign()
                                asignaciones_primerSem.add_alumno_tutor(alumno, tutor)
                                break
                            else:
                                continue
                        else:
                            alumno.change_espera()
                            break
                else:
                    if (alumno.get_solicitud_esp()[0] in tutor.get_ramosAsignados()):
                        if tutor.get_carrera() == alumno.get_carrera():
                            if tutor.get_cantTutorados() > 0:
                                alumno.change_asignado()
                                tutor.agregar_ramo(alumno.get_solicitud_esp()[0])
                                tutor.set_cantTutorados(tutor.get_cantTutorados() - alumno.get_peso())
                                tutor.asign()
                                asignaciones_primerSem.add_alumno_tutor(alumno, tutor)
                                
                                break
                            else:
                                continue
                        else:
                            if tutor.get_facultad() == alumno.get_facultad():
                                if tutor.get_cantTutorados() > 0:
                                    alumno.change_asignado()
                                    tutor.agregar_ramo(alumno.get_solicitud_esp()[0])
                                    tutor.set_cantTutorados(tutor.get_cantTutorados() - alumno.get_peso())
                                    tutor.asign()
                                    asignaciones_primerSem.add_alumno_tutor(alumno, tutor)
                                    
                                    break
                                else:
                                    continue
                            else:
                                alumno.change_espera()
                                break
                    else:
                        continue
                    

    
   
    for almuno in Alumnos_Asignacion_primerSem.get_alumnos():
        if almuno.get_estado() == 2:
            grupo_tutores_espera = Tutores()
            for tutor in tutoresAsignacion.get_tutores():
                if almuno.get_solicitud_esp()[0] in tutor.get_subarea() and (tutor.get_asign() != 2):
                    grupo_tutores_espera.add_tutor(tutor)
            # Se ordena de menor a mayor los tutores segun el largo de su lista de subareas
            grupo_tutores_espera.sort_tutores()

            for tutor in grupo_tutores_espera.get_tutores():
                if tutor.get_cantTutorados() > 0:
                    almuno.change_asignado()
                    tutor.set_cantTutorados(tutor.get_cantTutorados() - alumno.get_peso())
                    tutor.asign()
                    asignaciones_primerSem.add_alumno_tutor(almuno, tutor)
                    
                    break
                else:
                    continue
                
    
    for almuno in Alumnos_Asignacion_primerSem.get_alumnos():
        if alumno.get_estado() == 0:
            asignaciones_primerSem.add_alumno(almuno)
        elif alumno.get_estado() == 2:
            asignaciones_primerSem.add_alumno(almuno)
            

    asignaciones_primerSem.to_csv("Resource\AsignacionesPrimero.csv")   


    for alumno in Alumnos_Asignacion_segundoSem.get_alumnos():
        if alumno.get_estado() == 0:
            # Se crea el grupo de tutores para la persona
            grupo_tutores = Tutores()
            for tutor in tutoresAsignacion.get_tutores():
                if alumno.get_solicitud_esp()[0] in tutor.get_subarea() and (tutor.get_asign() != 2):
                    grupo_tutores.add_tutor(tutor)
            # Se ordena de menor a mayor los tutores segun el largo de su lista de subareas
            grupo_tutores.sort_tutores()

            for tutor in grupo_tutores.get_tutores():
                if (len(tutor.get_ramosAsignados()) < 2):
                    if tutor.get_carrera() == alumno.get_carrera():
                        if tutor.get_cantTutorados() > 0:
                            alumno.change_asignado()
                            tutor.agregar_ramo(alumno.get_solicitud_esp()[0])
                            tutor.set_cantTutorados(tutor.get_cantTutorados() - alumno.get_peso())
                            tutor.asign()
                            asignaciones_segundoSem.add_alumno_tutor(alumno, tutor)
                            
                            break
                        else:
                            continue
                    else:
                        if tutor.get_facultad() == alumno.get_facultad():
                            if tutor.get_cantTutorados() > 0:
                                alumno.change_asignado()
                                tutor.agregar_ramo(alumno.get_solicitud_esp()[0])
                                tutor.set_cantTutorados(tutor.get_cantTutorados() - alumno.get_peso())
                                tutor.asign()
                                asignaciones_segundoSem.add_alumno_tutor(alumno, tutor)
                                
                                break
                            else:
                                continue
                        else:
                            alumno.change_espera()
                            break
                else:
                    if (alumno.get_solicitud_esp()[0] in tutor.get_ramosAsignados()):
                        if tutor.get_carrera() == alumno.get_carrera():
                            if tutor.get_cantTutorados() > 0:
                                alumno.change_asignado()
                                tutor.agregar_ramo(alumno.get_solicitud_esp()[0])
                                tutor.set_cantTutorados(tutor.get_cantTutorados() - alumno.get_peso())
                                tutor.asign()
                                asignaciones_segundoSem.add_alumno_tutor(alumno, tutor)
                            
                                break
                            else:
                                continue
                        else:
                            if tutor.get_facultad() == alumno.get_facultad():
                                if tutor.get_cantTutorados() > 0:
                                    alumno.change_asignado()
                                    tutor.agregar_ramo(alumno.get_solicitud_esp()[0])
                                    tutor.set_cantTutorados(tutor.get_cantTutorados() - alumno.get_peso())
                                    tutor.asign()
                                    asignaciones_segundoSem.add_alumno_tutor(alumno, tutor)
                                    
                                    break
                                else:
                                    continue
                            else:
                                alumno.change_espera()
                                break
                    else:
                        continue


    for almuno in Alumnos_Asignacion_segundoSem.get_alumnos():
        if almuno.get_estado() == 2:
            grupo_tutores_espera = Tutores()
            for tutor in tutoresAsignacion.get_tutores():
                if almuno.get_solicitud_esp()[0] in tutor.get_subarea() and (tutor.get_asign() != 2):
                    grupo_tutores_espera.add_tutor(tutor)
            # Se ordena de menor a mayor los tutores segun el largo de su lista de subareas
            grupo_tutores_espera.sort_tutores()

            for tutor in grupo_tutores_espera.get_tutores():
                if tutor.get_cantTutorados() > 0:
                    almuno.change_asignado()
                    tutor.set_cantTutorados(tutor.get_cantTutorados() - alumno.get_peso())
                    tutor.asign()
                    asignaciones_segundoSem.add_alumno_tutor(almuno, tutor)
                    
                    break
                else:
                    continue

    for almuno in Alumnos_Asignacion_segundoSem.get_alumnos():
        if alumno.get_estado() == 0:
            asignaciones_segundoSem.add_alumno(almuno)
        elif alumno.get_estado() == 2:
            asignaciones_segundoSem.add_alumno(almuno)

    asignaciones_segundoSem.to_csv("Resource\AsignacionesSegundo.csv")


    if opcion:
        for alumno in Alumnos_Asignacion_Solicitudes.get_alumnos():
            if alumno.get_estado() == 0:
                # Se crea el grupo de tutores para la persona 
                grupo_tutores = Tutores()
                for tutor in tutoresAsignacion.get_tutores():
                    if alumno.get_solicitud_esp()[0] in tutor.get_subarea() and (tutor.get_asign() != 2):
                        grupo_tutores.add_tutor(tutor)
                # Se ordena de menor a mayor los tutores segun el largo de su lista de subareas
                grupo_tutores.sort_tutores()

                for tutor in grupo_tutores.get_tutores():
                    if (len(tutor.get_ramosAsignados()) < 2):
                        if tutor.get_carrera() == alumno.get_carrera():
                            if tutor.get_cantTutorados() > 0:
                                alumno.change_asignado()
                                tutor.agregar_ramo(alumno.get_solicitud_esp()[0])
                                tutor.set_cantTutorados(tutor.get_cantTutorados() - alumno.get_peso())
                                tutor.asign()
                                asignaciones_solicitudes.add_alumno_tutor(alumno, tutor)
                                
                                break
                            else:
                                continue
                        else:
                            if tutor.get_facultad() == alumno.get_facultad():
                                if tutor.get_cantTutorados() > 0:
                                    alumno.change_asignado()
                                    tutor.agregar_ramo(alumno.get_solicitud_esp()[0])
                                    tutor.set_cantTutorados(tutor.get_cantTutorados() - alumno.get_peso())
                                    tutor.asign()
                                    asignaciones_solicitudes.add_alumno_tutor(alumno, tutor)
                                    
                                    break
                                else:
                                    continue
                            else:
                                alumno.change_espera()
                                break
                    else:
                        if (alumno.get_solicitud_esp()[0] in tutor.get_ramosAsignados()):
                            if tutor.get_carrera() == alumno.get_carrera():
                                if tutor.get_cantTutorados() > 0:
                                    alumno.change_asignado()
                                    tutor.agregar_ramo(alumno.get_solicitud_esp()[0])
                                    tutor.set_cantTutorados(tutor.get_cantTutorados() - alumno.get_peso())
                                    tutor.asign()
                                    asignaciones_solicitudes.add_alumno_tutor(alumno, tutor)
                                    
                                    break
                                else:
                                    continue
                            else:
                                if tutor.get_facultad() == alumno.get_facultad():
                                    if tutor.get_cantTutorados() > 0:
                                        alumno.change_asignado()
                                        tutor.agregar_ramo(alumno.get_solicitud_esp()[0])
                                        tutor.set_cantTutorados(tutor.get_cantTutorados() - alumno.get_peso())
                                        tutor.asign()
                                        asignaciones_solicitudes.add_alumno_tutor(alumno, tutor)
                                    
                                        break
                                    else:
                                        continue
                                else:
                                    alumno.change_espera()
                                    break
                        else:
                            continue


        for almuno in Alumnos_Asignacion_Solicitudes.get_alumnos():
            if almuno.get_estado() == 2:
                grupo_tutores_espera = Tutores()
                for tutor in tutoresAsignacion.get_tutores():
                    if almuno.get_solicitud_esp()[0] in tutor.get_subarea() and (tutor.get_asign() != 2):
                        grupo_tutores_espera.add_tutor(tutor)
                # Se ordena de menor a mayor los tutores segun el largo de su lista de subareas
                grupo_tutores_espera.sort_tutores()

                for tutor in grupo_tutores_espera.get_tutores():
                    if tutor.get_cantTutorados() > 0:
                        almuno.change_asignado()
                        tutor.set_cantTutorados(tutor.get_cantTutorados() - alumno.get_peso())
                        tutor.asign()
                        asignaciones_solicitudes.add_alumno_tutor(almuno, tutor)
                        
                        break
                    else:
                        continue

        for almuno in Alumnos_Asignacion_Solicitudes.get_alumnos():
            if alumno.get_estado() == 0:
                asignaciones_solicitudes.add_alumno(almuno)
            elif alumno.get_estado() == 2:
                asignaciones_solicitudes.add_alumno(almuno)

        asignaciones_solicitudes.to_csv("Resource\AsignacionesSolicitudes.csv")


    # ? ------------------------ Escritura de los datos ---------------------------
    # Se crea una lista con las asignaciones
    lista_asignaciones = [asignaciones_primerSem, asignaciones_segundoSem, asignaciones_solicitudes, tutoresAsignacion]
    fecha =  str(datetime.datetime.now().strftime("%Y%m%d"))
    asiganacion_to_excel(lista_asignaciones, "Resource\Asignaciones" + fecha + ".xlsx")
    nombre = "Resource\Asignaciones" + fecha + ".xlsx"


    return [warnings, nombre, error]