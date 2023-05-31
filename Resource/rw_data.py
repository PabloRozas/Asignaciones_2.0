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
    dfVAE2023 = dfVAE2023.iloc[:, 0:14] # Se eliminan las columnas de los tutores que tienen asigandos los datos
    dfVAE2023.drop("NOMBRE SOCIAL", axis=1, inplace=True) # Se elimina la columna de nombre social
    dfVAE2023.drop("DV", axis=1, inplace=True) # Se elimina la columna de digito verificador
    
    dfVAE2023.columns = cambio_alumnos

    #Se dejan todas las columnas como tipo object
    for col in dfVAE2023.columns:
        dfVAE2023[col] = dfVAE2023[col].astype(str)

    data.append(dfVAE2023) # Se agrega a la lista de datos

    # ? ----------------------------------------------------------------------------

    dfPACE2023 = pd.read_excel(name, sheet_name= 1) # Se lee la segunda hoja del excel que contiene a los alumnos PACE 2023
    dfPACE2023 = dfPACE2023.iloc[:, 0:14] # Se eliminan las columnas de los tutores que tienen asigandos los datos
    dfPACE2023.drop("NOMBRE SOCIAL", axis=1, inplace=True) # Se elimina la columna de nombre social
    dfPACE2023.drop("DV", axis=1, inplace=True) # Se elimina la columna de digito verificador

    dfPACE2023.columns = cambio_alumnos

    #Se dejan todas las columnas como tipo object
    for col in dfPACE2023.columns:
        dfPACE2023[col] = dfPACE2023[col].astype(str)

    data.append(dfPACE2023) # Se agrega a la lista de datos

    # ? ----------------------------------------------------------------------------

    dfSolicitudes = pd.read_excel(name, sheet_name= 2) # Se lee la tercera hoja del excel que contiene a los alumnos que solicitaron tutor
    dfSolicitudes = dfSolicitudes.iloc[:, 0:14] # Se eliminan las columnas de los tutores que tienen asigandos los datos
    dfSolicitudes.drop("NOMBRE SOCIAL", axis=1, inplace=True) # Se elimina la columna de nombre social
    dfSolicitudes.drop("DV", axis=1, inplace=True) # Se elimina la columna de digito verificador

    dfSolicitudes.columns = cambio_alumnos

    #Se dejan todas las columnas como tipo object
    for col in dfSolicitudes.columns:
        dfSolicitudes[col] = dfSolicitudes[col].astype(str)

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

    return data


def warning_data(data):

    # ! --------- Se lee el archivo de carrera, facultad y areas ---------- ! #

    dfCarreras = pd.read_csv("Resource\VAE\Carreras.csv", sep= ",")
    # todo: Se transforma la columna de carreras en una lista
    carreras = dfCarreras.iloc[:,0].tolist()
    
    dfFacultad = pd.read_csv("Resource\VAE\Facultad.csv", sep= ",")
    # todo: Se transforma la columna de facultad en una lista
    facultad = dfFacultad.iloc[:,0].tolist()

    dfAreas = pd.read_csv("Resource\VAE\Acceso.csv", sep= ",")
    # todo: Se transforma la columna de areas en una lista
    areas = dfAreas.iloc[:,0].tolist()

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
        if row["VÍA DE ACCESO"] not in areas:
            print("Area no encontrada en la fila: ", index)
    
    print("------------------------------PACE------------------------------------")

    for index, row in dfPACE2023.iterrows():
        if row["CARRERA"] not in carreras:
            print("Carrera no encontrada en la fila: ", index)
        if row["FACULTAD"] not in facultad:
            print("Facultad no encontrada en la fila: ", index)
        if row["VÍA DE ACCESO"] not in areas:
            print("Area no encontrada en la fila: ", index)

    print("----------------------------Solicitudes--------------------------------------")

    for index, row in dfSolicitudes.iterrows():
        if row["CARRERA"] not in carreras:
            print("Carrera no encontrada en la fila: ", index)
        if row["FACULTAD"] not in facultad:
            print("Facultad no encontrada en la fila: ", index)
        if row["VÍA DE ACCESO"] not in areas:
            print("Area no encontrada en la fila: ", index)

    print("--------------------------------Tutores----------------------------------")

    for index, row in dfTutores.iterrows():
        if row["CARRERA"] not in carreras:
            print("Carrera no encontrada en la fila: ", index)
        if row["FACULTAD"] not in facultad:
            print("Facultad no encontrada en la fila: ", index)





def normalizar_data(data):
    
        dfVAE2023 = data[0]
        dfPACE2023 = data[1]
        dfSolicitudes = data[2]
        dfTutores = data[3]

        dfPACE2023.info()
        dfVAE2023.info()
        dfSolicitudes.info()
        dfTutores.info()


        # ! --------------------- Se normaliza la data --------------------- ! #

        # Se transforma las columnas carrera, facultad, via de acceso de cada df a formato utf-8 (para evitar problemas de caracteres)
        dfVAE2023["CARRERA"] = dfVAE2023["CARRERA"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        dfVAE2023["FACULTAD"] = dfVAE2023["FACULTAD"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        dfVAE2023["VÍA DE ACCESO"] = dfVAE2023["VÍA DE ACCESO"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        dfPACE2023["CARRERA"] = dfPACE2023["CARRERA"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        dfPACE2023["FACULTAD"] = dfPACE2023["FACULTAD"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        dfPACE2023["VÍA DE ACCESO"] = dfPACE2023["VÍA DE ACCESO"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        dfSolicitudes["CARRERA"] = dfSolicitudes["CARRERA"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        dfSolicitudes["FACULTAD"] = dfSolicitudes["FACULTAD"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        dfSolicitudes["VÍA DE ACCESO"] = dfSolicitudes["VÍA DE ACCESO"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        dfTutores["CARRERA"] = dfTutores["CARRERA"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        dfTutores["FACULTAD"] = dfTutores["FACULTAD"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
        dfTutores["ÁREA"] = dfTutores["ÁREA"].str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

        # Se transforma las columnas carrera, facultad, via de acceso de cada df a mayusculas
        dfVAE2023["CARRERA"] = dfVAE2023["CARRERA"].str.upper()
        dfVAE2023["FACULTAD"] = dfVAE2023["FACULTAD"].str.upper()
        dfVAE2023["VÍA DE ACCESO"] = dfVAE2023["VÍA DE ACCESO"].str.upper()
        dfPACE2023["CARRERA"] = dfPACE2023["CARRERA"].str.upper()
        dfPACE2023["FACULTAD"] = dfPACE2023["FACULTAD"].str.upper()
        dfPACE2023["VÍA DE ACCESO"] = dfPACE2023["VÍA DE ACCESO"].str.upper()
        dfSolicitudes["CARRERA"] = dfSolicitudes["CARRERA"].str.upper()
        dfSolicitudes["FACULTAD"] = dfSolicitudes["FACULTAD"].str.upper()
        dfSolicitudes["VÍA DE ACCESO"] = dfSolicitudes["VÍA DE ACCESO"].str.upper()
        dfTutores["CARRERA"] = dfTutores["CARRERA"].str.upper()
        dfTutores["FACULTAD"] = dfTutores["FACULTAD"].str.upper()
        dfTutores["ÁREA"] = dfTutores["ÁREA"].str.upper()


        # Transformar todos los que contengan "ING." a "INGENIERIA"
        dfVAE2023["CARRERA"] = dfVAE2023["CARRERA"].str.replace("ING.", "INGENIERIA")
        dfVAE2023["FACULTAD"] = dfVAE2023["FACULTAD"].str.replace("ING.", "INGENIERIA")
        dfVAE2023["VÍA DE ACCESO"] = dfVAE2023["VÍA DE ACCESO"].str.replace("ING.", "INGENIERIA")
        dfPACE2023["CARRERA"] = dfPACE2023["CARRERA"].str.replace("ING.", "INGENIERIA")
        dfPACE2023["FACULTAD"] = dfPACE2023["FACULTAD"].str.replace("ING.", "INGENIERIA")
        dfPACE2023["VÍA DE ACCESO"] = dfPACE2023["VÍA DE ACCESO"].str.replace("ING.", "INGENIERIA")
        dfSolicitudes["CARRERA"] = dfSolicitudes["CARRERA"].str.replace("ING.", "INGENIERIA")
        dfSolicitudes["FACULTAD"] = dfSolicitudes["FACULTAD"].str.replace("ING.", "INGENIERIA")
        dfSolicitudes["VÍA DE ACCESO"] = dfSolicitudes["VÍA DE ACCESO"].str.replace("ING.", "INGENIERIA")
        dfTutores["CARRERA"] = dfTutores["CARRERA"].str.replace("ING.", "INGENIERIA")
        dfTutores["FACULTAD"] = dfTutores["FACULTAD"].str.replace("ING.", "INGENIERIA")
        dfTutores["ÁREA"] = dfTutores["ÁREA"].str.replace("ING.", "INGENIERIA")


        # Quitar todos los EN de cada df
        dfVAE2023["CARRERA"] = dfVAE2023["CARRERA"].str.replace("EN ", "")
        dfVAE2023["FACULTAD"] = dfVAE2023["FACULTAD"].str.replace("EN ", "")
        dfVAE2023["VÍA DE ACCESO"] = dfVAE2023["VÍA DE ACCESO"].str.replace("EN ", "")
        dfPACE2023["CARRERA"] = dfPACE2023["CARRERA"].str.replace("EN ", "")
        dfPACE2023["FACULTAD"] = dfPACE2023["FACULTAD"].str.replace("EN ", "")
        dfPACE2023["VÍA DE ACCESO"] = dfPACE2023["VÍA DE ACCESO"].str.replace("EN ", "")
        dfSolicitudes["CARRERA"] = dfSolicitudes["CARRERA"].str.replace("EN ", "")
        dfSolicitudes["FACULTAD"] = dfSolicitudes["FACULTAD"].str.replace("EN ", "")
        dfSolicitudes["VÍA DE ACCESO"] = dfSolicitudes["VÍA DE ACCESO"].str.replace("EN ", "")
        dfTutores["CARRERA"] = dfTutores["CARRERA"].str.replace("EN ", "")
        dfTutores["FACULTAD"] = dfTutores["FACULTAD"].str.replace("EN ", "")
        dfTutores["ÁREA"] = dfTutores["ÁREA"].str.replace("EN ", "")

        # Reemplazar los "  " por " "
        dfVAE2023["CARRERA"] = dfVAE2023["CARRERA"].str.replace("  ", " ")
        dfVAE2023["FACULTAD"] = dfVAE2023["FACULTAD"].str.replace("  ", " ")
        dfVAE2023["VÍA DE ACCESO"] = dfVAE2023["VÍA DE ACCESO"].str.replace("  ", " ")
        dfPACE2023["CARRERA"] = dfPACE2023["CARRERA"].str.replace("  ", " ")
        dfPACE2023["FACULTAD"] = dfPACE2023["FACULTAD"].str.replace("  ", " ")
        dfPACE2023["VÍA DE ACCESO"] = dfPACE2023["VÍA DE ACCESO"].str.replace("  ", " ")
        dfSolicitudes["CARRERA"] = dfSolicitudes["CARRERA"].str.replace("  ", " ")
        dfSolicitudes["FACULTAD"] = dfSolicitudes["FACULTAD"].str.replace("  ", " ")
        dfSolicitudes["VÍA DE ACCESO"] = dfSolicitudes["VÍA DE ACCESO"].str.replace("  ", " ")
        dfTutores["CARRERA"] = dfTutores["CARRERA"].str.replace("  ", " ")
        dfTutores["FACULTAD"] = dfTutores["FACULTAD"].str.replace("  ", " ")
        dfTutores["ÁREA"] = dfTutores["ÁREA"].str.replace("  ", " ")

        # Se quitan todos los espacios al inicio y al final
        dfVAE2023["CARRERA"] = dfVAE2023["CARRERA"].str.strip()
        dfVAE2023["FACULTAD"] = dfVAE2023["FACULTAD"].str.strip()
        dfVAE2023["VÍA DE ACCESO"] = dfVAE2023["VÍA DE ACCESO"].str.strip()
        dfPACE2023["CARRERA"] = dfPACE2023["CARRERA"].str.strip()
        dfPACE2023["FACULTAD"] = dfPACE2023["FACULTAD"].str.strip()
        dfPACE2023["VÍA DE ACCESO"] = dfPACE2023["VÍA DE ACCESO"].str.strip()
        dfSolicitudes["CARRERA"] = dfSolicitudes["CARRERA"].str.strip()
        dfSolicitudes["FACULTAD"] = dfSolicitudes["FACULTAD"].str.strip()
        dfSolicitudes["VÍA DE ACCESO"] = dfSolicitudes["VÍA DE ACCESO"].str.strip()
        dfTutores["CARRERA"] = dfTutores["CARRERA"].str.strip()
        dfTutores["FACULTAD"] = dfTutores["FACULTAD"].str.strip()
        dfTutores["ÁREA"] = dfTutores["ÁREA"].str.strip()
        

        # Pasar de df carrera a un csv
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

        # Pasar de df facultad a un csv
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

        # Pasar de df via de acceso a un csv
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

        # Pasar de df area a un csv
        dfAreaTutores = dfTutores["ÁREA"].drop_duplicates()

        # ! Ordenar de manera alfabetica
        dfAreaTutores = dfAreaTutores.sort_values()

        dfAreaTutores.to_csv("Resource\Tutores\Area.csv", index=False)



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





        print(dfVAE2023.head())
        print(dfPACE2023.head())
        print(dfSolicitudes.head())
        print(dfTutores.head())



def test():
    data = get_data("Resource\data.xlsx")
    # print(data[0].head())
    # print(data[1].head())
    # print(data[2].head())
    # print(data[3].head())
    # data[0].info()

    # warning_data(data)

    normalizar_data(data)

test()