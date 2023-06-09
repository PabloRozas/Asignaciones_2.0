import pandas as pd
import numpy as np


""" get_data """
""" 
Descripción: Función que lee los datos de los alumnos y los tutrores de un archivo excel y estos son almacenados en una lista que es retornada, donde 
el index 0 es para VAE, 1 para PACE, 2 Solicitudes y 3 para los tutores
Entrada: name (nombre en string del archivo excel)
Salida: data (lista con los datos de los alumnos y tutores)
"""

def get_data(name):

    data = [] #Lista que almacenará los datos de los alumnos y tutores

    cambio_alumnos = [
        "RUT",
        "NOMBRE COMPLETO",
        "CARRERA",
        "FACULTAD",
        "VÍA DE ACCESO",
        "VÍA PAIEP",
        "IES ACOMPAÑAMIENTO",
        "CORREO USACH",
        "CORREO PERSONAL",
        "TELÉFONO 1",
        "TELÉFONO 2",
        "MATRICULADOS 1s2023"
    ]

    cambio_tutores = [
        "RUT",
        "NOMBRE COMPLETO",
        "CARRERA",
        "FACULTAD",
        "CORREO USACH",
        "TELÉFONO 1",
        "CORREO PERSONAL",
        "ÁREA",
        "SUB-ÁREA",
        "HORAS"
    ]



    # ? ----------------------------------------------------------------------------

    dfVAE2023 = pd.read_excel(name, sheet_name= 0) # Se lee la primera hoja del excel que contiene a los alumnos VAE 2023
    dfVAE2023asign_tut = dfVAE2023.iloc[:, 14:17]
    dfVAE2023asign_tut = pd.concat([dfVAE2023asign_tut, dfVAE2023.iloc[:, 23:26]], axis=1)
    dfVAE2023asign_tut = pd.concat([dfVAE2023asign_tut, dfVAE2023.iloc[:, 32:35]], axis=1)
    dfVAE2023asign_tut.columns = ["ÁREA TUTOR 1", "SUBÁREA TUTOR 1", "ESPECIALIDAD 1", "ÁREA TUTOR 2", "SUBÁREA TUTOR 2", "ESPECIALIDAD 2", "ÁREA TUTOR 3", "SUBÁREA TUTOR 3", "ESPECIALIDAD 3"]
    #Se transforman los tipos de la columna a string
    for col in dfVAE2023asign_tut.columns:
        dfVAE2023asign_tut[col] = dfVAE2023asign_tut[col].astype(str)
    dfVAE2023asign_tut = dfVAE2023asign_tut.replace("nan", "", regex=True) # Se reemplazan los nan por vacios
    dfVAE2023 = dfVAE2023.iloc[:, 0:14] # Se eliminan las columnas de los tutores que tienen asigandos los datos
    dfVAE2023.drop("NOMBRE SOCIAL", axis=1, inplace=True) # Se elimina la columna de nombre social
    dfVAE2023.drop("DV", axis=1, inplace=True) # Se elimina la columna de digito verificador
    
    dfVAE2023.columns = cambio_alumnos

    #Se dejan todas las columnas como tipo object
    for col in dfVAE2023.columns:
        dfVAE2023[col] = dfVAE2023[col].astype(str)

    dfVAE2023 = pd.concat([dfVAE2023, dfVAE2023asign_tut], axis=1)

    data.append(dfVAE2023) # Se agrega a la lista de datos

    # ? ----------------------------------------------------------------------------

    dfPACE2023 = pd.read_excel(name, sheet_name= 1) # Se lee la segunda hoja del excel que contiene a los alumnos PACE 2023
    dfPACE2023asign_tut = dfPACE2023.iloc[:, 14:17]
    dfPACE2023asign_tut = pd.concat([dfPACE2023asign_tut, dfPACE2023.iloc[:, 23:26]], axis=1)
    dfPACE2023asign_tut = pd.concat([dfPACE2023asign_tut, dfPACE2023.iloc[:, 32:35]], axis=1)
    dfPACE2023asign_tut.columns = ["ÁREA TUTOR 1", "SUBÁREA TUTOR 1", "ESPECIALIDAD 1", "ÁREA TUTOR 2", "SUBÁREA TUTOR 2", "ESPECIALIDAD 2", "ÁREA TUTOR 3", "SUBÁREA TUTOR 3", "ESPECIALIDAD 3"]
    #Se transforman los tipos de la columna a string
    for col in dfPACE2023asign_tut.columns:
        dfPACE2023asign_tut[col] = dfPACE2023asign_tut[col].astype(str)
    dfPACE2023asign_tut = dfPACE2023asign_tut.replace("nan", "", regex=True) # Se reemplazan los nan por vacios

    dfPACE2023 = dfPACE2023.iloc[:, 0:14] # Se eliminan las columnas de los tutores que tienen asigandos los datos
    dfPACE2023.drop("NOMBRE SOCIAL", axis=1, inplace=True) # Se elimina la columna de nombre social
    dfPACE2023.drop("DV", axis=1, inplace=True) # Se elimina la columna de digito verificador

    dfPACE2023.columns = cambio_alumnos

    #Se dejan todas las columnas como tipo object
    for col in dfPACE2023.columns:
        dfPACE2023[col] = dfPACE2023[col].astype(str)

    dfPACE2023 = pd.concat([dfPACE2023, dfPACE2023asign_tut], axis=1)
    data.append(dfPACE2023) # Se agrega a la lista de datos

    # ? ----------------------------------------------------------------------------

    dfSolicitudes = pd.read_excel(name, sheet_name= 2) # Se lee la tercera hoja del excel que contiene a los alumnos que solicitaron tutor
    dfSolicitudesasign_tut = dfSolicitudes.iloc[:, 14:17]
    dfSolicitudesasign_tut = pd.concat([dfSolicitudesasign_tut, dfSolicitudes.iloc[:, 23:26]], axis=1)
    dfSolicitudesasign_tut = pd.concat([dfSolicitudesasign_tut, dfSolicitudes.iloc[:, 32:35]], axis=1)
    dfSolicitudesasign_tut.columns = ["ÁREA TUTOR 1", "SUBÁREA TUTOR 1", "ESPECIALIDAD 1", "ÁREA TUTOR 2", "SUBÁREA TUTOR 2", "ESPECIALIDAD 2", "ÁREA TUTOR 3", "SUBÁREA TUTOR 3", "ESPECIALIDAD 3"]
    #Se transforman los tipos de la columna a string
    for col in dfSolicitudesasign_tut.columns:
        dfSolicitudesasign_tut[col] = dfSolicitudesasign_tut[col].astype(str)
    dfSolicitudesasign_tut = dfSolicitudesasign_tut.replace("nan", '', regex=True) # Se reemplazan los valores NaN por un string vacio

    dfSolicitudes = dfSolicitudes.iloc[:, 0:14] # Se eliminan las columnas de los tutores que tienen asigandos los datos
    dfSolicitudes.drop("NOMBRE SOCIAL", axis=1, inplace=True) # Se elimina la columna de nombre social
    dfSolicitudes.drop("DV", axis=1, inplace=True) # Se elimina la columna de digito verificador

    dfSolicitudes.columns = cambio_alumnos
    #Se dejan todas las columnas como tipo object
    for col in dfSolicitudes.columns:
        dfSolicitudes[col] = dfSolicitudes[col].astype(str)
    # dfPACE2023asign_tut.info()
    # print(dfPACE2023asign_tut.head())
    dfSolicitudes = pd.concat([dfSolicitudes, dfSolicitudesasign_tut], axis=1)
    data.append(dfSolicitudes) # Se agrega a la lista de datos
    
    # ? ----------------------------------------------------------------------------

    dfTutores = pd.read_excel(name, sheet_name= 4) # Se lee la cuarta hoja del excel que contiene a los tutores
    dfTutores = pd.concat([dfTutores.iloc[:, 0:9], dfTutores.iloc[:, 11]], axis=1) # Se concatenan las columnas de los tutores que tienen asigandos los datos

    dfTutores.columns = cambio_tutores

    #Se dejan todas las columnas como tipo object
    for col in dfTutores.columns:
        dfTutores[col] = dfTutores[col].astype(str)

    dfTutores["RUT"] = dfTutores["RUT"].str.replace("-", "") #De la columna rut se eliminan los guiones y el digito verificador
    dfTutores["RUT"] = dfTutores["RUT"].str[:-1] #Se quita el ultimo digito del rut

    data.append(dfTutores) # Se agrega a la lista de datos

    # ? ----------------------------------------------------------------------------

    return normalizar_data(data, 1) # Se retorna la lista de datos normalizada


def warning_data(data):

    # ! --------- Se lee el archivo de carrera, facultad y areas de VAE ---------- ! #

    dfCarreras = pd.read_csv("Resource\Carreras.csv", sep= ",")
    # todo: Se transforma la columna de carreras en una lista
    carreras = dfCarreras.iloc[:,0].tolist()
    
    dfFacultad = pd.read_csv("Resource\Facultades.csv", sep= ",")
    # todo: Se transforma la columna de facultad en una lista
    facultad = dfFacultad.iloc[:,0].tolist()

    dfAcceso = pd.read_csv("Resource\Acceso.csv", sep= ",")
    # todo: Se transforma la columna de areas en una lista
    acceso = dfAcceso.iloc[:,0].tolist()

    dfArea = pd.read_csv("Resource\AreaTutores.csv", sep= ",")
    # todo: Se transforma la columna de areas en una lista
    area = dfArea.iloc[:,0].tolist()


    dfVAE2023 = data[0]
    dfPACE2023 = data[1]
    dfSolicitudes = data[2]
    dfTutores = data[3]

    print("-----------------------------VAE-------------------------------------")
    for index, row in dfVAE2023.iterrows():
        if row["CARRERA"] not in carreras:
            print("Carrera no encontrada en la fila: ", index)
        if row["FACULTAD"] not in facultad:
            print("Facultad no encontrada en la fila: ", index)
        if row["VÍA DE ACCESO"] not in acceso:
            print("Area no encontrada en la fila: ", index)
    
    print("------------------------------PACE------------------------------------")

    for index, row in dfPACE2023.iterrows():
        if row["CARRERA"] not in carreras:
            print("Carrera no encontrada en la fila: ", index)
        if row["FACULTAD"] not in facultad:
            print("Facultad no encontrada en la fila: ", index)
        if row["VÍA DE ACCESO"] not in acceso:
            print("Area no encontrada en la fila: ", index)

    print("----------------------------Solicitudes--------------------------------------")

    for index, row in dfSolicitudes.iterrows():
        if row["CARRERA"] not in carreras:
            print("Carrera no encontrada en la fila: ", index)
        if row["FACULTAD"] not in facultad:
            print("Facultad no encontrada en la fila: ", index)
        if row["VÍA DE ACCESO"] not in acceso:
            print("Area no encontrada en la fila: ", index)

    print("--------------------------------Tutores----------------------------------")

    for index, row in dfTutores.iterrows():
        if row["CARRERA"] not in carreras:
            print("Carrera no encontrada en la fila: ", index)
        if row["FACULTAD"] not in facultad:
            print("Facultad no encontrada en la fila: ", index)
        if row["ÁREA"] not in area:
            print("Area no encontrada en la fila: ", index)

def normalizar_data(data, opcion = 0):

    dfVAE2023 = data[0]
    dfPACE2023 = data[1]
    dfSolicitudes = data[2]
    dfTutores = data[3]

    # dfPACE2023.info()
    # dfVAE2023.info()
    # dfSolicitudes.info()
    # dfTutores.info()


    # ! --------------------- Se normaliza la data --------------------- ! #

    # Se transforma las columnas carrera, facultad, via de acceso de cada df a formato utf-8 (para evitar problemas de caracteres)
    dfVAE2023["CARRERA"] = dfVAE2023["CARRERA"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfVAE2023["FACULTAD"] = dfVAE2023["FACULTAD"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfVAE2023["VÍA DE ACCESO"] = dfVAE2023["VÍA DE ACCESO"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfVAE2023["VÍA PAIEP"] = dfVAE2023["VÍA PAIEP"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfVAE2023["ÁREA TUTOR 1"] = dfVAE2023["ÁREA TUTOR 1"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfVAE2023["ÁREA TUTOR 2"] = dfVAE2023["ÁREA TUTOR 2"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfVAE2023["ÁREA TUTOR 3"] = dfVAE2023["ÁREA TUTOR 3"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfVAE2023["SUBÁREA TUTOR 1"] = dfVAE2023["SUBÁREA TUTOR 1"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfVAE2023["SUBÁREA TUTOR 2"] = dfVAE2023["SUBÁREA TUTOR 2"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfVAE2023["SUBÁREA TUTOR 3"] = dfVAE2023["SUBÁREA TUTOR 3"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfVAE2023["ESPECIALIDAD 1"] = dfVAE2023["ESPECIALIDAD 1"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfVAE2023["ESPECIALIDAD 2"] = dfVAE2023["ESPECIALIDAD 2"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfVAE2023["ESPECIALIDAD 3"] = dfVAE2023["ESPECIALIDAD 3"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfPACE2023["CARRERA"] = dfPACE2023["CARRERA"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfPACE2023["FACULTAD"] = dfPACE2023["FACULTAD"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfPACE2023["VÍA DE ACCESO"] = dfPACE2023["VÍA DE ACCESO"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfPACE2023["VÍA PAIEP"] = dfPACE2023["VÍA PAIEP"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfPACE2023["ÁREA TUTOR 1"] = dfPACE2023["ÁREA TUTOR 1"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfPACE2023["ÁREA TUTOR 2"] = dfPACE2023["ÁREA TUTOR 2"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfPACE2023["ÁREA TUTOR 3"] = dfPACE2023["ÁREA TUTOR 3"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfPACE2023["SUBÁREA TUTOR 1"] = dfPACE2023["SUBÁREA TUTOR 1"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfPACE2023["SUBÁREA TUTOR 2"] = dfPACE2023["SUBÁREA TUTOR 2"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfPACE2023["SUBÁREA TUTOR 3"] = dfPACE2023["SUBÁREA TUTOR 3"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfPACE2023["ESPECIALIDAD 1"] = dfPACE2023["ESPECIALIDAD 1"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfPACE2023["ESPECIALIDAD 2"] = dfPACE2023["ESPECIALIDAD 2"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfPACE2023["ESPECIALIDAD 3"] = dfPACE2023["ESPECIALIDAD 3"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfSolicitudes["CARRERA"] = dfSolicitudes["CARRERA"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfSolicitudes["FACULTAD"] = dfSolicitudes["FACULTAD"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfSolicitudes["VÍA DE ACCESO"] = dfSolicitudes["VÍA DE ACCESO"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfSolicitudes["VÍA PAIEP"] = dfSolicitudes["VÍA PAIEP"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfSolicitudes["ÁREA TUTOR 1"] = dfSolicitudes["ÁREA TUTOR 1"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfSolicitudes["ÁREA TUTOR 2"] = dfSolicitudes["ÁREA TUTOR 2"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfSolicitudes["ÁREA TUTOR 3"] = dfSolicitudes["ÁREA TUTOR 3"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfSolicitudes["SUBÁREA TUTOR 1"] = dfSolicitudes["SUBÁREA TUTOR 1"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfSolicitudes["SUBÁREA TUTOR 2"] = dfSolicitudes["SUBÁREA TUTOR 2"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfSolicitudes["SUBÁREA TUTOR 3"] = dfSolicitudes["SUBÁREA TUTOR 3"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfSolicitudes["ESPECIALIDAD 1"] = dfSolicitudes["ESPECIALIDAD 1"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfSolicitudes["ESPECIALIDAD 2"] = dfSolicitudes["ESPECIALIDAD 2"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfSolicitudes["ESPECIALIDAD 3"] = dfSolicitudes["ESPECIALIDAD 3"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfTutores["CARRERA"] = dfTutores["CARRERA"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfTutores["FACULTAD"] = dfTutores["FACULTAD"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfTutores["ÁREA"] = dfTutores["ÁREA"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
    dfTutores["SUB-ÁREA"] = dfTutores["SUB-ÁREA"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

    # Se transforma las columnas carrera, facultad, via de acceso de cada df a mayusculas
    dfVAE2023["CARRERA"] = dfVAE2023["CARRERA"].str.upper()
    dfVAE2023["FACULTAD"] = dfVAE2023["FACULTAD"].str.upper()
    dfVAE2023["VÍA DE ACCESO"] = dfVAE2023["VÍA DE ACCESO"].str.upper()
    dfVAE2023["VÍA PAIEP"] = dfVAE2023["VÍA PAIEP"].str.upper()
    dfVAE2023["ÁREA TUTOR 1"] = dfVAE2023["ÁREA TUTOR 1"].str.upper()
    dfVAE2023["ÁREA TUTOR 2"] = dfVAE2023["ÁREA TUTOR 2"].str.upper()
    dfVAE2023["ÁREA TUTOR 3"] = dfVAE2023["ÁREA TUTOR 3"].str.upper()
    dfVAE2023["SUBÁREA TUTOR 1"] = dfVAE2023["SUBÁREA TUTOR 1"].str.upper()
    dfVAE2023["SUBÁREA TUTOR 2"] = dfVAE2023["SUBÁREA TUTOR 2"].str.upper()
    dfVAE2023["SUBÁREA TUTOR 3"] = dfVAE2023["SUBÁREA TUTOR 3"].str.upper()
    dfVAE2023["ESPECIALIDAD 1"] = dfVAE2023["ESPECIALIDAD 1"].str.upper()
    dfVAE2023["ESPECIALIDAD 2"] = dfVAE2023["ESPECIALIDAD 2"].str.upper()
    dfVAE2023["ESPECIALIDAD 3"] = dfVAE2023["ESPECIALIDAD 3"].str.upper()
    dfPACE2023["CARRERA"] = dfPACE2023["CARRERA"].str.upper()
    dfPACE2023["FACULTAD"] = dfPACE2023["FACULTAD"].str.upper()
    dfPACE2023["VÍA DE ACCESO"] = dfPACE2023["VÍA DE ACCESO"].str.upper()
    dfPACE2023["VÍA PAIEP"] = dfPACE2023["VÍA PAIEP"].str.upper()
    dfPACE2023["ÁREA TUTOR 1"] = dfPACE2023["ÁREA TUTOR 1"].str.upper()
    dfPACE2023["ÁREA TUTOR 2"] = dfPACE2023["ÁREA TUTOR 2"].str.upper()
    dfPACE2023["ÁREA TUTOR 3"] = dfPACE2023["ÁREA TUTOR 3"].str.upper()
    dfPACE2023["SUBÁREA TUTOR 1"] = dfPACE2023["SUBÁREA TUTOR 1"].str.upper()
    dfPACE2023["SUBÁREA TUTOR 2"] = dfPACE2023["SUBÁREA TUTOR 2"].str.upper()
    dfPACE2023["SUBÁREA TUTOR 3"] = dfPACE2023["SUBÁREA TUTOR 3"].str.upper()
    dfPACE2023["ESPECIALIDAD 1"] = dfPACE2023["ESPECIALIDAD 1"].str.upper()
    dfPACE2023["ESPECIALIDAD 2"] = dfPACE2023["ESPECIALIDAD 2"].str.upper()
    dfPACE2023["ESPECIALIDAD 3"] = dfPACE2023["ESPECIALIDAD 3"].str.upper()
    dfSolicitudes["CARRERA"] = dfSolicitudes["CARRERA"].str.upper()
    dfSolicitudes["FACULTAD"] = dfSolicitudes["FACULTAD"].str.upper()
    dfSolicitudes["VÍA DE ACCESO"] = dfSolicitudes["VÍA DE ACCESO"].str.upper()
    dfSolicitudes["VÍA PAIEP"] = dfSolicitudes["VÍA PAIEP"].str.upper()
    dfSolicitudes["ÁREA TUTOR 1"] = dfSolicitudes["ÁREA TUTOR 1"].str.upper()
    dfSolicitudes["ÁREA TUTOR 2"] = dfSolicitudes["ÁREA TUTOR 2"].str.upper()
    dfSolicitudes["ÁREA TUTOR 3"] = dfSolicitudes["ÁREA TUTOR 3"].str.upper()
    dfSolicitudes["SUBÁREA TUTOR 1"] = dfSolicitudes["SUBÁREA TUTOR 1"].str.upper()
    dfSolicitudes["SUBÁREA TUTOR 2"] = dfSolicitudes["SUBÁREA TUTOR 2"].str.upper()
    dfSolicitudes["SUBÁREA TUTOR 3"] = dfSolicitudes["SUBÁREA TUTOR 3"].str.upper()
    dfSolicitudes["ESPECIALIDAD 1"] = dfSolicitudes["ESPECIALIDAD 1"].str.upper()
    dfSolicitudes["ESPECIALIDAD 2"] = dfSolicitudes["ESPECIALIDAD 2"].str.upper()
    dfSolicitudes["ESPECIALIDAD 3"] = dfSolicitudes["ESPECIALIDAD 3"].str.upper()
    dfTutores["CARRERA"] = dfTutores["CARRERA"].str.upper()
    dfTutores["FACULTAD"] = dfTutores["FACULTAD"].str.upper()
    dfTutores["ÁREA"] = dfTutores["ÁREA"].str.upper()
    dfTutores["SUB-ÁREA"] = dfTutores["SUB-ÁREA"].str.upper()


    # Transformar todos los que contengan "ING." a "INGENIERIA"
    dfVAE2023["CARRERA"] = dfVAE2023["CARRERA"].str.replace("ING.", "INGENIERIA")
    dfVAE2023["FACULTAD"] = dfVAE2023["FACULTAD"].str.replace("ING.", "INGENIERIA")
    dfVAE2023["VÍA DE ACCESO"] = dfVAE2023["VÍA DE ACCESO"].str.replace("ING.", "INGENIERIA")
    dfVAE2023["VÍA PAIEP"] = dfVAE2023["VÍA PAIEP"].str.replace("ING.", "INGENIERIA")
    dfVAE2023["ÁREA TUTOR 1"] = dfVAE2023["ÁREA TUTOR 1"].str.replace("ING.", "INGENIERIA")
    dfVAE2023["ÁREA TUTOR 2"] = dfVAE2023["ÁREA TUTOR 2"].str.replace("ING.", "INGENIERIA")
    dfVAE2023["ÁREA TUTOR 3"] = dfVAE2023["ÁREA TUTOR 3"].str.replace("ING.", "INGENIERIA")
    dfVAE2023["SUBÁREA TUTOR 1"] = dfVAE2023["SUBÁREA TUTOR 1"].str.replace("ING.", "INGENIERIA")
    dfVAE2023["SUBÁREA TUTOR 2"] = dfVAE2023["SUBÁREA TUTOR 2"].str.replace("ING.", "INGENIERIA")
    dfVAE2023["SUBÁREA TUTOR 3"] = dfVAE2023["SUBÁREA TUTOR 3"].str.replace("ING.", "INGENIERIA")
    dfVAE2023["ESPECIALIDAD 1"] = dfVAE2023["ESPECIALIDAD 1"].str.replace("ING.", "INGENIERIA")
    dfVAE2023["ESPECIALIDAD 2"] = dfVAE2023["ESPECIALIDAD 2"].str.replace("ING.", "INGENIERIA")
    dfVAE2023["ESPECIALIDAD 3"] = dfVAE2023["ESPECIALIDAD 3"].str.replace("ING.", "INGENIERIA")
    dfPACE2023["CARRERA"] = dfPACE2023["CARRERA"].str.replace("ING.", "INGENIERIA")
    dfPACE2023["FACULTAD"] = dfPACE2023["FACULTAD"].str.replace("ING.", "INGENIERIA")
    dfPACE2023["VÍA DE ACCESO"] = dfPACE2023["VÍA DE ACCESO"].str.replace("ING.", "INGENIERIA")
    dfPACE2023["VÍA PAIEP"] = dfPACE2023["VÍA PAIEP"].str.replace("ING.", "INGENIERIA")
    dfPACE2023["ÁREA TUTOR 1"] = dfPACE2023["ÁREA TUTOR 1"].str.replace("ING.", "INGENIERIA")
    dfPACE2023["ÁREA TUTOR 2"] = dfPACE2023["ÁREA TUTOR 2"].str.replace("ING.", "INGENIERIA")
    dfPACE2023["ÁREA TUTOR 3"] = dfPACE2023["ÁREA TUTOR 3"].str.replace("ING.", "INGENIERIA")
    dfPACE2023["SUBÁREA TUTOR 1"] = dfPACE2023["SUBÁREA TUTOR 1"].str.replace("ING.", "INGENIERIA")
    dfPACE2023["SUBÁREA TUTOR 2"] = dfPACE2023["SUBÁREA TUTOR 2"].str.replace("ING.", "INGENIERIA")
    dfPACE2023["SUBÁREA TUTOR 3"] = dfPACE2023["SUBÁREA TUTOR 3"].str.replace("ING.", "INGENIERIA")
    dfPACE2023["ESPECIALIDAD 1"] = dfPACE2023["ESPECIALIDAD 1"].str.replace("ING.", "INGENIERIA")
    dfPACE2023["ESPECIALIDAD 2"] = dfPACE2023["ESPECIALIDAD 2"].str.replace("ING.", "INGENIERIA")
    dfPACE2023["ESPECIALIDAD 3"] = dfPACE2023["ESPECIALIDAD 3"].str.replace("ING.", "INGENIERIA")
    dfSolicitudes["CARRERA"] = dfSolicitudes["CARRERA"].str.replace("ING.", "INGENIERIA")
    dfSolicitudes["FACULTAD"] = dfSolicitudes["FACULTAD"].str.replace("ING.", "INGENIERIA")
    dfSolicitudes["VÍA DE ACCESO"] = dfSolicitudes["VÍA DE ACCESO"].str.replace("ING.", "INGENIERIA")
    dfSolicitudes["VÍA PAIEP"] = dfSolicitudes["VÍA PAIEP"].str.replace("ING.", "INGENIERIA")
    dfSolicitudes["ÁREA TUTOR 1"] = dfSolicitudes["ÁREA TUTOR 1"].str.replace("ING.", "INGENIERIA")
    dfSolicitudes["ÁREA TUTOR 2"] = dfSolicitudes["ÁREA TUTOR 2"].str.replace("ING.", "INGENIERIA")
    dfSolicitudes["ÁREA TUTOR 3"] = dfSolicitudes["ÁREA TUTOR 3"].str.replace("ING.", "INGENIERIA")
    dfSolicitudes["SUBÁREA TUTOR 1"] = dfSolicitudes["SUBÁREA TUTOR 1"].str.replace("ING.", "INGENIERIA")
    dfSolicitudes["SUBÁREA TUTOR 2"] = dfSolicitudes["SUBÁREA TUTOR 2"].str.replace("ING.", "INGENIERIA")
    dfSolicitudes["SUBÁREA TUTOR 3"] = dfSolicitudes["SUBÁREA TUTOR 3"].str.replace("ING.", "INGENIERIA")
    dfSolicitudes["ESPECIALIDAD 1"] = dfSolicitudes["ESPECIALIDAD 1"].str.replace("ING.", "INGENIERIA")
    dfSolicitudes["ESPECIALIDAD 2"] = dfSolicitudes["ESPECIALIDAD 2"].str.replace("ING.", "INGENIERIA")
    dfSolicitudes["ESPECIALIDAD 3"] = dfSolicitudes["ESPECIALIDAD 3"].str.replace("ING.", "INGENIERIA")
    dfTutores["CARRERA"] = dfTutores["CARRERA"].str.replace("ING.", "INGENIERIA")
    dfTutores["FACULTAD"] = dfTutores["FACULTAD"].str.replace("ING.", "INGENIERIA")
    dfTutores["ÁREA"] = dfTutores["ÁREA"].str.replace("ING.", "INGENIERIA")
    dfTutores["SUB-ÁREA"] = dfTutores["SUB-ÁREA"].str.replace("ING.", "INGENIERIA")

    # Transformar todos los que contengan "INGE" a "INGENIERIA"
    # dfVAE2023["CARRERA"] = dfVAE2023["CARRERA"].str.replace("INGE", "INGENIERIA")
    # dfVAE2023["FACULTAD"] = dfVAE2023["FACULTAD"].str.replace("INGE", "INGENIERIA")
    # dfVAE2023["VÍA DE ACCESO"] = dfVAE2023["VÍA DE ACCESO"].str.replace("INGE", "INGENIERIA")
    # dfPACE2023["CARRERA"] = dfPACE2023["CARRERA"].str.replace("INGE", "INGENIERIA")
    # dfPACE2023["FACULTAD"] = dfPACE2023["FACULTAD"].str.replace("INGE", "INGENIERIA")
    # dfPACE2023["VÍA DE ACCESO"] = dfPACE2023["VÍA DE ACCESO"].str.replace("INGE", "INGENIERIA")
    # dfSolicitudes["CARRERA"] = dfSolicitudes["CARRERA"].str.replace("INGE", "INGENIERIA")
    # dfSolicitudes["FACULTAD"] = dfSolicitudes["FACULTAD"].str.replace("INGE", "INGENIERIA")
    # dfSolicitudes["VÍA DE ACCESO"] = dfSolicitudes["VÍA DE ACCESO"].str.replace("INGE", "INGENIERIA")
    # dfTutores["CARRERA"] = dfTutores["CARRERA"].str.replace("INGE", "INGENIERIA")
    # dfTutores["FACULTAD"] = dfTutores["FACULTAD"].str.replace("INGE", "INGENIERIA")
    # dfTutores["ÁREA"] = dfTutores["ÁREA"].str.replace("INGE", "INGENIERIA")


    # Quitar todos los EN de cada df
    dfVAE2023["CARRERA"] = dfVAE2023["CARRERA"].str.replace("EN ", "")
    dfVAE2023["FACULTAD"] = dfVAE2023["FACULTAD"].str.replace("EN ", "")
    dfVAE2023["VÍA DE ACCESO"] = dfVAE2023["VÍA DE ACCESO"].str.replace("EN ", "")
    dfVAE2023["VÍA PAIEP"] = dfVAE2023["VÍA PAIEP"].str.replace("EN ", "")
    dfVAE2023["ÁREA TUTOR 1"] = dfVAE2023["ÁREA TUTOR 1"].str.replace("EN ", "")
    dfVAE2023["ÁREA TUTOR 2"] = dfVAE2023["ÁREA TUTOR 2"].str.replace("EN ", "")
    dfVAE2023["ÁREA TUTOR 3"] = dfVAE2023["ÁREA TUTOR 3"].str.replace("EN ", "")
    dfVAE2023["SUBÁREA TUTOR 1"] = dfVAE2023["SUBÁREA TUTOR 1"].str.replace("EN ", "")
    dfVAE2023["SUBÁREA TUTOR 2"] = dfVAE2023["SUBÁREA TUTOR 2"].str.replace("EN ", "")
    dfVAE2023["SUBÁREA TUTOR 3"] = dfVAE2023["SUBÁREA TUTOR 3"].str.replace("EN ", "")
    dfVAE2023["ESPECIALIDAD 1"] = dfVAE2023["ESPECIALIDAD 1"].str.replace("EN ", "")
    dfVAE2023["ESPECIALIDAD 2"] = dfVAE2023["ESPECIALIDAD 2"].str.replace("EN ", "")
    dfVAE2023["ESPECIALIDAD 3"] = dfVAE2023["ESPECIALIDAD 3"].str.replace("EN ", "")
    dfPACE2023["CARRERA"] = dfPACE2023["CARRERA"].str.replace("EN ", "")
    dfPACE2023["FACULTAD"] = dfPACE2023["FACULTAD"].str.replace("EN ", "")
    dfPACE2023["VÍA DE ACCESO"] = dfPACE2023["VÍA DE ACCESO"].str.replace("EN ", "")
    dfPACE2023["VÍA PAIEP"] = dfPACE2023["VÍA PAIEP"].str.replace("EN ", "")
    dfPACE2023["ÁREA TUTOR 1"] = dfPACE2023["ÁREA TUTOR 1"].str.replace("EN ", "")
    dfPACE2023["ÁREA TUTOR 2"] = dfPACE2023["ÁREA TUTOR 2"].str.replace("EN ", "")
    dfPACE2023["ÁREA TUTOR 3"] = dfPACE2023["ÁREA TUTOR 3"].str.replace("EN ", "")
    dfPACE2023["SUBÁREA TUTOR 1"] = dfPACE2023["SUBÁREA TUTOR 1"].str.replace("EN ", "")
    dfPACE2023["SUBÁREA TUTOR 2"] = dfPACE2023["SUBÁREA TUTOR 2"].str.replace("EN ", "")
    dfPACE2023["SUBÁREA TUTOR 3"] = dfPACE2023["SUBÁREA TUTOR 3"].str.replace("EN ", "")
    dfPACE2023["ESPECIALIDAD 1"] = dfPACE2023["ESPECIALIDAD 1"].str.replace("EN ", "")
    dfPACE2023["ESPECIALIDAD 2"] = dfPACE2023["ESPECIALIDAD 2"].str.replace("EN ", "")
    dfPACE2023["ESPECIALIDAD 3"] = dfPACE2023["ESPECIALIDAD 3"].str.replace("EN ", "")
    dfSolicitudes["CARRERA"] = dfSolicitudes["CARRERA"].str.replace("EN ", "")
    dfSolicitudes["FACULTAD"] = dfSolicitudes["FACULTAD"].str.replace("EN ", "")
    dfSolicitudes["VÍA DE ACCESO"] = dfSolicitudes["VÍA DE ACCESO"].str.replace("EN ", "")
    dfSolicitudes["VÍA PAIEP"] = dfSolicitudes["VÍA PAIEP"].str.replace("EN ", "")
    dfSolicitudes["ÁREA TUTOR 1"] = dfSolicitudes["ÁREA TUTOR 1"].str.replace("EN ", "")
    dfSolicitudes["ÁREA TUTOR 2"] = dfSolicitudes["ÁREA TUTOR 2"].str.replace("EN ", "")
    dfSolicitudes["ÁREA TUTOR 3"] = dfSolicitudes["ÁREA TUTOR 3"].str.replace("EN ", "")
    dfSolicitudes["SUBÁREA TUTOR 1"] = dfSolicitudes["SUBÁREA TUTOR 1"].str.replace("EN ", "")
    dfSolicitudes["SUBÁREA TUTOR 2"] = dfSolicitudes["SUBÁREA TUTOR 2"].str.replace("EN ", "")
    dfSolicitudes["SUBÁREA TUTOR 3"] = dfSolicitudes["SUBÁREA TUTOR 3"].str.replace("EN ", "")
    dfSolicitudes["ESPECIALIDAD 1"] = dfSolicitudes["ESPECIALIDAD 1"].str.replace("EN ", "")
    dfSolicitudes["ESPECIALIDAD 2"] = dfSolicitudes["ESPECIALIDAD 2"].str.replace("EN ", "")
    dfSolicitudes["ESPECIALIDAD 3"] = dfSolicitudes["ESPECIALIDAD 3"].str.replace("EN ", "")
    dfTutores["CARRERA"] = dfTutores["CARRERA"].str.replace("EN ", "")
    dfTutores["FACULTAD"] = dfTutores["FACULTAD"].str.replace("EN ", "")
    dfTutores["ÁREA"] = dfTutores["ÁREA"].str.replace("EN ", "")
    dfTutores["SUB-ÁREA"] = dfTutores["SUB-ÁREA"].str.replace("EN ", "")

    # Reemplazar los "  " por " "
    dfVAE2023["CARRERA"] = dfVAE2023["CARRERA"].str.replace("  ", " ")
    dfVAE2023["FACULTAD"] = dfVAE2023["FACULTAD"].str.replace("  ", " ")
    dfVAE2023["VÍA DE ACCESO"] = dfVAE2023["VÍA DE ACCESO"].str.replace("  ", " ")
    dfVAE2023["VÍA PAIEP"] = dfVAE2023["VÍA PAIEP"].str.replace("  ", " ")
    dfVAE2023["ÁREA TUTOR 1"] = dfVAE2023["ÁREA TUTOR 1"].str.replace("  ", " ")
    dfVAE2023["ÁREA TUTOR 2"] = dfVAE2023["ÁREA TUTOR 2"].str.replace("  ", " ")
    dfVAE2023["ÁREA TUTOR 3"] = dfVAE2023["ÁREA TUTOR 3"].str.replace("  ", " ")
    dfVAE2023["SUBÁREA TUTOR 1"] = dfVAE2023["SUBÁREA TUTOR 1"].str.replace("  ", " ")
    dfVAE2023["SUBÁREA TUTOR 2"] = dfVAE2023["SUBÁREA TUTOR 2"].str.replace("  ", " ")
    dfVAE2023["SUBÁREA TUTOR 3"] = dfVAE2023["SUBÁREA TUTOR 3"].str.replace("  ", " ")
    dfVAE2023["ESPECIALIDAD 1"] = dfVAE2023["ESPECIALIDAD 1"].str.replace("  ", " ")
    dfVAE2023["ESPECIALIDAD 2"] = dfVAE2023["ESPECIALIDAD 2"].str.replace("  ", " ")
    dfVAE2023["ESPECIALIDAD 3"] = dfVAE2023["ESPECIALIDAD 3"].str.replace("  ", " ")
    dfPACE2023["CARRERA"] = dfPACE2023["CARRERA"].str.replace("  ", " ")
    dfPACE2023["FACULTAD"] = dfPACE2023["FACULTAD"].str.replace("  ", " ")
    dfPACE2023["VÍA DE ACCESO"] = dfPACE2023["VÍA DE ACCESO"].str.replace("  ", " ")
    dfPACE2023["VÍA PAIEP"] = dfPACE2023["VÍA PAIEP"].str.replace("  ", " ")
    dfPACE2023["ÁREA TUTOR 1"] = dfPACE2023["ÁREA TUTOR 1"].str.replace("  ", " ")
    dfPACE2023["ÁREA TUTOR 2"] = dfPACE2023["ÁREA TUTOR 2"].str.replace("  ", " ")
    dfPACE2023["ÁREA TUTOR 3"] = dfPACE2023["ÁREA TUTOR 3"].str.replace("  ", " ")
    dfPACE2023["SUBÁREA TUTOR 1"] = dfPACE2023["SUBÁREA TUTOR 1"].str.replace("  ", " ")
    dfPACE2023["SUBÁREA TUTOR 2"] = dfPACE2023["SUBÁREA TUTOR 2"].str.replace("  ", " ")
    dfPACE2023["SUBÁREA TUTOR 3"] = dfPACE2023["SUBÁREA TUTOR 3"].str.replace("  ", " ")
    dfPACE2023["ESPECIALIDAD 1"] = dfPACE2023["ESPECIALIDAD 1"].str.replace("  ", " ")
    dfPACE2023["ESPECIALIDAD 2"] = dfPACE2023["ESPECIALIDAD 2"].str.replace("  ", " ")
    dfPACE2023["ESPECIALIDAD 3"] = dfPACE2023["ESPECIALIDAD 3"].str.replace("  ", " ")
    dfSolicitudes["CARRERA"] = dfSolicitudes["CARRERA"].str.replace("  ", " ")
    dfSolicitudes["FACULTAD"] = dfSolicitudes["FACULTAD"].str.replace("  ", " ")
    dfSolicitudes["VÍA DE ACCESO"] = dfSolicitudes["VÍA DE ACCESO"].str.replace("  ", " ")
    dfSolicitudes["VÍA PAIEP"] = dfSolicitudes["VÍA PAIEP"].str.replace("  ", " ")
    dfSolicitudes["ÁREA TUTOR 1"] = dfSolicitudes["ÁREA TUTOR 1"].str.replace("  ", " ")
    dfSolicitudes["ÁREA TUTOR 2"] = dfSolicitudes["ÁREA TUTOR 2"].str.replace("  ", " ")
    dfSolicitudes["ÁREA TUTOR 3"] = dfSolicitudes["ÁREA TUTOR 3"].str.replace("  ", " ")
    dfSolicitudes["SUBÁREA TUTOR 1"] = dfSolicitudes["SUBÁREA TUTOR 1"].str.replace("  ", " ")
    dfSolicitudes["SUBÁREA TUTOR 2"] = dfSolicitudes["SUBÁREA TUTOR 2"].str.replace("  ", " ")
    dfSolicitudes["SUBÁREA TUTOR 3"] = dfSolicitudes["SUBÁREA TUTOR 3"].str.replace("  ", " ")
    dfSolicitudes["ESPECIALIDAD 1"] = dfSolicitudes["ESPECIALIDAD 1"].str.replace("  ", " ")
    dfSolicitudes["ESPECIALIDAD 2"] = dfSolicitudes["ESPECIALIDAD 2"].str.replace("  ", " ")
    dfSolicitudes["ESPECIALIDAD 3"] = dfSolicitudes["ESPECIALIDAD 3"].str.replace("  ", " ")
    dfTutores["CARRERA"] = dfTutores["CARRERA"].str.replace("  ", " ")
    dfTutores["FACULTAD"] = dfTutores["FACULTAD"].str.replace("  ", " ")
    dfTutores["ÁREA"] = dfTutores["ÁREA"].str.replace("  ", " ")
    dfTutores["SUB-ÁREA"] = dfTutores["SUB-ÁREA"].str.replace("  ", " ")

    # Se quitan todos los espacios al inicio y al final
    dfVAE2023["CARRERA"] = dfVAE2023["CARRERA"].str.strip()
    dfVAE2023["FACULTAD"] = dfVAE2023["FACULTAD"].str.strip()
    dfVAE2023["VÍA DE ACCESO"] = dfVAE2023["VÍA DE ACCESO"].str.strip()
    dfVAE2023["VÍA PAIEP"] = dfVAE2023["VÍA PAIEP"].str.strip()
    dfVAE2023["ÁREA TUTOR 1"] = dfVAE2023["ÁREA TUTOR 1"].str.strip()
    dfVAE2023["ÁREA TUTOR 2"] = dfVAE2023["ÁREA TUTOR 2"].str.strip()
    dfVAE2023["ÁREA TUTOR 3"] = dfVAE2023["ÁREA TUTOR 3"].str.strip()
    dfVAE2023["SUBÁREA TUTOR 1"] = dfVAE2023["SUBÁREA TUTOR 1"].str.strip()
    dfVAE2023["SUBÁREA TUTOR 2"] = dfVAE2023["SUBÁREA TUTOR 2"].str.strip()
    dfVAE2023["SUBÁREA TUTOR 3"] = dfVAE2023["SUBÁREA TUTOR 3"].str.strip()
    dfVAE2023["ESPECIALIDAD 1"] = dfVAE2023["ESPECIALIDAD 1"].str.strip()
    dfVAE2023["ESPECIALIDAD 2"] = dfVAE2023["ESPECIALIDAD 2"].str.strip()
    dfVAE2023["ESPECIALIDAD 3"] = dfVAE2023["ESPECIALIDAD 3"].str.strip()
    dfPACE2023["CARRERA"] = dfPACE2023["CARRERA"].str.strip()
    dfPACE2023["FACULTAD"] = dfPACE2023["FACULTAD"].str.strip()
    dfPACE2023["VÍA DE ACCESO"] = dfPACE2023["VÍA DE ACCESO"].str.strip()
    dfPACE2023["VÍA PAIEP"] = dfPACE2023["VÍA PAIEP"].str.strip()
    dfPACE2023["ÁREA TUTOR 1"] = dfPACE2023["ÁREA TUTOR 1"].str.strip()
    dfPACE2023["ÁREA TUTOR 2"] = dfPACE2023["ÁREA TUTOR 2"].str.strip()
    dfPACE2023["ÁREA TUTOR 3"] = dfPACE2023["ÁREA TUTOR 3"].str.strip()
    dfPACE2023["SUBÁREA TUTOR 1"] = dfPACE2023["SUBÁREA TUTOR 1"].str.strip()
    dfPACE2023["SUBÁREA TUTOR 2"] = dfPACE2023["SUBÁREA TUTOR 2"].str.strip()
    dfPACE2023["SUBÁREA TUTOR 3"] = dfPACE2023["SUBÁREA TUTOR 3"].str.strip()
    dfPACE2023["ESPECIALIDAD 1"] = dfPACE2023["ESPECIALIDAD 1"].str.strip()
    dfPACE2023["ESPECIALIDAD 2"] = dfPACE2023["ESPECIALIDAD 2"].str.strip()
    dfPACE2023["ESPECIALIDAD 3"] = dfPACE2023["ESPECIALIDAD 3"].str.strip()
    dfSolicitudes["CARRERA"] = dfSolicitudes["CARRERA"].str.strip()
    dfSolicitudes["FACULTAD"] = dfSolicitudes["FACULTAD"].str.strip()
    dfSolicitudes["VÍA DE ACCESO"] = dfSolicitudes["VÍA DE ACCESO"].str.strip()
    dfSolicitudes["VÍA PAIEP"] = dfSolicitudes["VÍA PAIEP"].str.strip()
    dfSolicitudes["ÁREA TUTOR 1"] = dfSolicitudes["ÁREA TUTOR 1"].str.strip()
    dfSolicitudes["ÁREA TUTOR 2"] = dfSolicitudes["ÁREA TUTOR 2"].str.strip()
    dfSolicitudes["ÁREA TUTOR 3"] = dfSolicitudes["ÁREA TUTOR 3"].str.strip()
    dfSolicitudes["SUBÁREA TUTOR 1"] = dfSolicitudes["SUBÁREA TUTOR 1"].str.strip()
    dfSolicitudes["SUBÁREA TUTOR 2"] = dfSolicitudes["SUBÁREA TUTOR 2"].str.strip()
    dfSolicitudes["SUBÁREA TUTOR 3"] = dfSolicitudes["SUBÁREA TUTOR 3"].str.strip()
    dfSolicitudes["ESPECIALIDAD 1"] = dfSolicitudes["ESPECIALIDAD 1"].str.strip()
    dfSolicitudes["ESPECIALIDAD 2"] = dfSolicitudes["ESPECIALIDAD 2"].str.strip()
    dfSolicitudes["ESPECIALIDAD 3"] = dfSolicitudes["ESPECIALIDAD 3"].str.strip()
    dfTutores["CARRERA"] = dfTutores["CARRERA"].str.strip()
    dfTutores["FACULTAD"] = dfTutores["FACULTAD"].str.strip()
    dfTutores["ÁREA"] = dfTutores["ÁREA"].str.strip()
    dfTutores["SUB-ÁREA"] = dfTutores["SUB-ÁREA"].str.strip()

    # Se cambia en sub area los que los que contengan MATEMATICAS por MATEMATICA
    dfTutores["SUB-ÁREA"] = dfTutores["SUB-ÁREA"].str.replace("MATEMATICAS", "MATEMATICA")
    
    if (opcion == 1):
        # ? ------------------------------------------------------------------------------------------
        
        #* Pasar de df carrera a un csv
        dfCarrerasVAE = dfVAE2023["CARRERA"].drop_duplicates()
        dfCarrerasPACE = dfPACE2023["CARRERA"].drop_duplicates()
        dfCarrerasSolictudes = dfSolicitudes["CARRERA"].drop_duplicates()
        dfCarrerasTutores = dfTutores["CARRERA"].drop_duplicates()

        # ! Ordenar de manera alfabetica
        dfCarrerasVAE = dfCarrerasVAE.sort_values()
        dfCarrerasPACE = dfCarrerasPACE.sort_values()
        dfCarrerasSolictudes = dfCarrerasSolictudes.sort_values()
        dfCarrerasTutores = dfCarrerasTutores.sort_values()

        dfCarrerasVAE.to_csv("Resource\VAE\Carreras.csv", index=False)
        dfCarrerasPACE.to_csv("Resource\PACE\Carreras.csv", index=False)
        dfCarrerasSolictudes.to_csv("Resource\Solicitudes\Carreras.csv", index=False)
        dfCarrerasTutores.to_csv("Resource\Tutores\Carreras.csv", index=False)

        #* Pasar de df facultad a un csv
        dfFacultadVAE = dfVAE2023["FACULTAD"].drop_duplicates()
        dfFacultadPACE = dfPACE2023["FACULTAD"].drop_duplicates()
        dfFacultadSolictudes = dfSolicitudes["FACULTAD"].drop_duplicates()
        dfFacultadTutores = dfTutores["FACULTAD"].drop_duplicates()

        # ! Ordenar de manera alfabetica
        dfFacultadVAE = dfFacultadVAE.sort_values()
        dfFacultadPACE = dfFacultadPACE.sort_values()
        dfFacultadSolictudes = dfFacultadSolictudes.sort_values()
        dfFacultadTutores = dfFacultadTutores.sort_values()

        dfFacultadVAE.to_csv("Resource\VAE\Facultad.csv", index=False)
        dfFacultadPACE.to_csv("Resource\PACE\Facultad.csv", index=False)
        dfFacultadSolictudes.to_csv("Resource\Solicitudes\Facultad.csv", index=False)
        dfFacultadTutores.to_csv("Resource\Tutores\Facultad.csv", index=False)

        #* Pasar de df via de acceso a un csv
        dfViaVAE = dfVAE2023["VÍA DE ACCESO"].drop_duplicates()
        dfViaPACE = dfPACE2023["VÍA DE ACCESO"].drop_duplicates()
        dfViaSolictudes = dfSolicitudes["VÍA DE ACCESO"].drop_duplicates()

        # ! Ordenar de manera alfabetica
        dfViaVAE = dfViaVAE.sort_values()
        dfViaPACE = dfViaPACE.sort_values()
        dfViaSolictudes = dfViaSolictudes.sort_values()

        dfViaVAE.to_csv("Resource\VAE\Acceso.csv", index=False)
        dfViaPACE.to_csv("Resource\PACE\Acceso.csv", index=False)
        dfViaSolictudes.to_csv("Resource\Solicitudes\Acceso.csv", index=False)

        #* Pasar de df area a un csv
        dfAreaTutores = dfTutores["ÁREA"].drop_duplicates()

        # ! Ordenar de manera alfabetica
        dfAreaTutores = dfAreaTutores.sort_values()

        dfAreaTutores.to_csv("Resource\Tutores\Area.csv", index=False)

        #* Pasar de df subarea a un csv
        dfSubAreaTutores = dfTutores["SUB-ÁREA"].drop_duplicates()

        # ! Ordenar de manera alfabetica
        dfSubAreaTutores = dfSubAreaTutores.sort_values()

        dfSubAreaTutores.to_csv("Resource\Tutores\SubArea.csv", index=False)

        #* Pasar de df via paiep a un csv
        dfViaPaiepVAE = dfVAE2023["VÍA PAIEP"].drop_duplicates()
        dfViaPaiepPACE = dfPACE2023["VÍA PAIEP"].drop_duplicates()
        dfViaPaiepSolictudes = dfSolicitudes["VÍA PAIEP"].drop_duplicates()

        # ! Ordenar de manera alfabetica
        dfViaPaiepVAE = dfViaPaiepVAE.sort_values()
        dfViaPaiepPACE = dfViaPaiepPACE.sort_values()
        dfViaPaiepSolictudes = dfViaPaiepSolictudes.sort_values()

        dfViaPaiepVAE.to_csv("Resource\VAE\Paiep.csv", index=False)
        dfViaPaiepPACE.to_csv("Resource\PACE\Paiep.csv", index=False)
        dfViaPaiepSolictudes.to_csv("Resource\Solicitudes\Paiep.csv", index=False)

        #* Pasar de df solicitud area a un csv
        dfSolicitudArea = pd.concat([dfVAE2023["ÁREA TUTOR 1"], dfVAE2023["ÁREA TUTOR 2"], dfVAE2023["ÁREA TUTOR 3"], dfPACE2023["ÁREA TUTOR 1"], dfPACE2023["ÁREA TUTOR 2"], dfPACE2023["ÁREA TUTOR 3"], dfSolicitudes["ÁREA TUTOR 1"], dfSolicitudes["ÁREA TUTOR 2"], dfSolicitudes["ÁREA TUTOR 3"]])
        dfSolicitudArea = dfSolicitudArea.drop_duplicates()
        
        # ! Ordenar de manera alfabetica
        dfSolicitudArea = dfSolicitudArea.sort_values()
        
        dfSolicitudArea.to_csv("Resource\SolicitudesArea.csv", index=False)

        #* Pasar de df solicitud subarea a un csv
        dfSolicitudSubArea = pd.concat([dfVAE2023["SUBÁREA TUTOR 1"], dfVAE2023["SUBÁREA TUTOR 2"], dfVAE2023["SUBÁREA TUTOR 3"], dfPACE2023["SUBÁREA TUTOR 1"], dfPACE2023["SUBÁREA TUTOR 2"], dfPACE2023["SUBÁREA TUTOR 3"], dfSolicitudes["SUBÁREA TUTOR 1"], dfSolicitudes["SUBÁREA TUTOR 2"], dfSolicitudes["SUBÁREA TUTOR 3"]])
        dfSolicitudSubArea = dfSolicitudSubArea.drop_duplicates()

        # ! Ordenar de manera alfabetica
        dfSolicitudSubArea = dfSolicitudSubArea.sort_values()

        dfSolicitudSubArea.to_csv("Resource\SolicitudesSubArea.csv", index=False)

        #* Pasar de df especialidad a un csv
        dfEspecialidad = pd.concat([dfVAE2023["ESPECIALIDAD 1"], dfVAE2023["ESPECIALIDAD 2"], dfVAE2023["ESPECIALIDAD 3"], dfPACE2023["ESPECIALIDAD 1"], dfPACE2023["ESPECIALIDAD 2"], dfPACE2023["ESPECIALIDAD 3"], dfSolicitudes["ESPECIALIDAD 1"], dfSolicitudes["ESPECIALIDAD 2"], dfSolicitudes["ESPECIALIDAD 3"]])
        dfEspecialidad = dfEspecialidad.drop_duplicates()
        
        # ! Ordenar de manera alfabetica
        dfEspecialidad = dfEspecialidad.sort_values()

        dfEspecialidad.to_csv("Resource\Especialidad.csv", index=False)


        # ? --------------------------------------------------------------------------------------------------------------
        # todo: Crear csv de carreras por facultad
        dfVAE2023[["CARRERA", "FACULTAD"]].to_csv("Resource\VAE\Carreras_Facultad.csv", index=False)
        dfPACE2023[["CARRERA", "FACULTAD"]].to_csv("Resource\PACE\Carreras_Facultad.csv", index=False)
        dfSolicitudes[["CARRERA", "FACULTAD"]].to_csv("Resource\Solicitudes\Carreras_Facultad.csv", index=False)
        dfTutores[["CARRERA", "FACULTAD"]].to_csv("Resource\Tutores\Carreras_Facultad.csv", index=False)

        result = pd.merge(dfVAE2023[['CARRERA', 'FACULTAD']], dfPACE2023[['CARRERA', 'FACULTAD']], how='outer', on=['CARRERA', 'FACULTAD'])
        result = pd.merge(result, dfSolicitudes[['CARRERA', 'FACULTAD']], how='outer', on=['CARRERA', 'FACULTAD'])
        result = pd.merge(result, dfTutores[['CARRERA', 'FACULTAD']], how='outer', on=['CARRERA', 'FACULTAD'])

        #Eliminar duplicados y ordenar
        result = result.drop_duplicates()
        result = result.sort_values(by=['CARRERA', 'FACULTAD'])
        

        result.to_csv("Resource\Carreras_Facultad.csv", index=False)

        # ? --------------------------------------------------------------------------------------------------------------
        # todo: Se crea el csv de carreras en general
        result = pd.merge(dfCarrerasVAE, dfCarrerasPACE, how='outer', on=['CARRERA'])
        result = pd.merge(result, dfCarrerasSolictudes, how='outer', on=['CARRERA'])
        result = pd.merge(result, dfCarrerasTutores, how='outer', on=['CARRERA'])

        #Eliminar duplicados y ordenar
        result = result.drop_duplicates()
        result = result.sort_values(by=['CARRERA'])

        result.to_csv("Resource\Carreras.csv", index=False)

        # ? --------------------------------------------------------------------------------------------------------------
        # todo: Se crea el csv de facultades en general
        result = pd.merge(dfFacultadVAE, dfFacultadPACE, how='outer', on=['FACULTAD'])
        result = pd.merge(result, dfFacultadSolictudes, how='outer', on=['FACULTAD'])
        result = pd.merge(result, dfFacultadTutores, how='outer', on=['FACULTAD'])

        #Eliminar duplicados y ordenar
        result = result.drop_duplicates()
        result = result.sort_values(by=['FACULTAD'])

        result.to_csv("Resource\Facultades.csv", index=False)

        # ? --------------------------------------------------------------------------------------------------------------
        # todo: Se crea el csv de vias de acceso en general
        result = pd.merge(dfViaVAE, dfViaPACE, how='outer', on=['VÍA DE ACCESO'])
        result = pd.merge(result, dfViaSolictudes, how='outer', on=['VÍA DE ACCESO'])

        #Eliminar duplicados y ordenar
        result = result.drop_duplicates()
        result = result.sort_values(by=['VÍA DE ACCESO'])

        result.to_csv("Resource\Acceso.csv", index=False)

        # ? --------------------------------------------------------------------------------------------------------------
        # todo: Se crea el csv de areas en general

        dfAreaTutores.to_csv("Resource\AreaTutores.csv", index=False)

        # ? --------------------------------------------------------------------------------------------------------------
        # todo: Se crea el csv de subareas en general

        dfSubAreaTutores.to_csv("Resource\SubAreaTutores.csv", index=False)

        # ? --------------------------------------------------------------------------------------------------------------
        # todo: Se crea el csv de vias de paiep en general
        result = pd.merge(dfViaPaiepVAE, dfViaPaiepPACE, how='outer', on=['VÍA PAIEP'])
        result = pd.merge(result, dfViaPaiepSolictudes, how='outer', on=['VÍA PAIEP'])

        #Eliminar duplicados y ordenar
        result = result.drop_duplicates()
        result = result.sort_values(by=['VÍA PAIEP'])

        result.to_csv("Resource\Paiep.csv", index=False)

    # Se transforman todos los nan en 0 de las columnas de TELÉFONO 1 y 2

    dfVAE2023["TELÉFONO 1"] = dfVAE2023["TELÉFONO 1"].str.replace("nan", "0")
    dfVAE2023["TELÉFONO 2"] = dfVAE2023["TELÉFONO 2"].str.replace("nan", "0")
    dfPACE2023["TELÉFONO 1"] = dfPACE2023["TELÉFONO 1"].str.replace("nan", "0")
    dfPACE2023["TELÉFONO 2"] = dfPACE2023["TELÉFONO 2"].str.replace("nan", "0")
    dfSolicitudes["TELÉFONO 1"] = dfSolicitudes["TELÉFONO 1"].str.replace("nan", "0")
    dfSolicitudes["TELÉFONO 2"] = dfSolicitudes["TELÉFONO 2"].str.replace("nan", "0")
    dfTutores["TELÉFONO 1"] = dfTutores["TELÉFONO 1"].str.replace("nan", "0")

    # Se transforman todos los - en 0 de las columnas de TELÉFONO 1 y 2

    dfVAE2023["TELÉFONO 1"] = dfVAE2023["TELÉFONO 1"].str.replace("-", "0")
    dfVAE2023["TELÉFONO 2"] = dfVAE2023["TELÉFONO 2"].str.replace("-", "0")
    dfPACE2023["TELÉFONO 1"] = dfPACE2023["TELÉFONO 1"].str.replace("-", "0")
    dfPACE2023["TELÉFONO 2"] = dfPACE2023["TELÉFONO 2"].str.replace("-", "0")
    dfSolicitudes["TELÉFONO 1"] = dfSolicitudes["TELÉFONO 1"].str.replace("-", "0")
    dfSolicitudes["TELÉFONO 2"] = dfSolicitudes["TELÉFONO 2"].str.replace("-", "0")
    dfTutores["TELÉFONO 1"] = dfTutores["TELÉFONO 1"].str.replace("-", "0")

    # Se quitan todos los .0 de los string de TELÉFONO 1 y 2

    dfVAE2023["TELÉFONO 1"] = dfVAE2023["TELÉFONO 1"].str.replace(".0", "")
    dfVAE2023["TELÉFONO 2"] = dfVAE2023["TELÉFONO 2"].str.replace(".0", "")
    dfPACE2023["TELÉFONO 1"] = dfPACE2023["TELÉFONO 1"].str.replace(".0", "")
    dfPACE2023["TELÉFONO 2"] = dfPACE2023["TELÉFONO 2"].str.replace(".0", "")
    dfSolicitudes["TELÉFONO 1"] = dfSolicitudes["TELÉFONO 1"].str.replace(".0", "")
    dfSolicitudes["TELÉFONO 2"] = dfSolicitudes["TELÉFONO 2"].str.replace(".0", "")
    dfTutores["TELÉFONO 1"] = dfTutores["TELÉFONO 1"].str.replace(".0", "")

    # Se quitan todos los espacios de los string de TELÉFONO 1 y 2

    dfVAE2023["TELÉFONO 1"] = dfVAE2023["TELÉFONO 1"].str.replace(" ", "")
    dfVAE2023["TELÉFONO 2"] = dfVAE2023["TELÉFONO 2"].str.replace(" ", "")
    dfPACE2023["TELÉFONO 1"] = dfPACE2023["TELÉFONO 1"].str.replace(" ", "")
    dfPACE2023["TELÉFONO 2"] = dfPACE2023["TELÉFONO 2"].str.replace(" ", "")
    dfSolicitudes["TELÉFONO 1"] = dfSolicitudes["TELÉFONO 1"].str.replace(" ", "")
    dfSolicitudes["TELÉFONO 2"] = dfSolicitudes["TELÉFONO 2"].str.replace(" ", "")
    dfTutores["TELÉFONO 1"] = dfTutores["TELÉFONO 1"].str.replace(" ", "")

    # Se transforman los TELÉFONO 1 y 2 en int long

    dfVAE2023["TELÉFONO 1"] = dfVAE2023["TELÉFONO 1"].astype('int64')
    dfVAE2023["TELÉFONO 2"] = dfVAE2023["TELÉFONO 2"].astype('int64')
    dfPACE2023["TELÉFONO 1"] = dfPACE2023["TELÉFONO 1"].astype('int64')
    dfPACE2023["TELÉFONO 2"] = dfPACE2023["TELÉFONO 2"].astype('int64')
    dfSolicitudes["TELÉFONO 1"] = dfSolicitudes["TELÉFONO 1"].astype('int64')
    dfSolicitudes["TELÉFONO 2"] = dfSolicitudes["TELÉFONO 2"].astype('int64')
    dfTutores["TELÉFONO 1"] = dfTutores["TELÉFONO 1"].astype('int64')


    return [dfVAE2023, dfPACE2023, dfSolicitudes, dfTutores]

def test():
    data = get_data("Resource\data.xlsx")
    dfVAE2023 = data[0]
    dfPACE2023 = data[1]
    dfSolicitudes = data[2]
    dfTutores = data[3]
    # print(dfVAE2023.head())
    # print(dfPACE2023.head())
    # print(dfSolicitudes.head())
    # print(dfTutores.head())

    # dfVAE2023.info()
    # dfPACE2023.info()
    # dfSolicitudes.info()
    # dfTutores.info()

    warning_data(data)

# test()