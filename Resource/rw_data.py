import pandas as pd



""" get_data """
""" 
Descripción: Función que lee los datos de los alumnos y los tutrores de un archivo excel y estos son almacenados en una lista que es retornada, donde 
el index 0 es para VAE, 1 para PACE, 3 Solicitudes y 4 para los tutores
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

    dfVAE2023 = pd.read_excel(name, sheet_name= 1) # Se lee la primera hoja del excel que contiene a los alumnos VAE 2023
    dfVAE2023 = dfVAE2023.iloc[:, 0:14] # Se eliminan las columnas de los tutores que tienen asigandos los datos
    dfVAE2023.drop("NOMBRE SOCIAL", axis=1, inplace=True) # Se elimina la columna de nombre social
    dfVAE2023["RUT"] = dfVAE2023["RUT_USACH"].astype(str).str.cat(dfVAE2023["DV"].astype(str), sep="-") # Se crea la columna RUT con el rut y el digito verificador
    dfVAE2023.insert(0, "RUT", dfVAE2023.pop("RUT")) # Se mueve al inicio del dataframe
    dfVAE2023.drop("RUT_USACH", axis=1, inplace=True) # Se elimina la columna de rut usach
    dfVAE2023.drop("DV", axis=1, inplace=True) # Se elimina la columna de digito verificador

    dfVAE2023.columns = cambio_alumnos

    # print("VAE 2023")
    # dfVAE2023.info()
    # print(dfVAE2023.head())

    data.append(dfVAE2023) # Se agrega a la lista de datos

    dfPACE2023 = pd.read_excel(name, sheet_name= 2) # Se lee la segunda hoja del excel que contiene a los alumnos PACE 2023
    dfPACE2023 = dfPACE2023.iloc[:, 0:14] # Se eliminan las columnas de los tutores que tienen asigandos los datos
    dfPACE2023.drop("NOMBRE SOCIAL", axis=1, inplace=True) # Se elimina la columna de nombre social
    dfPACE2023["RUT"] = dfPACE2023["RUT_USACH"].astype(str).str.cat(dfPACE2023["DV"].astype(str), sep="-") # Se crea la columna RUT con el rut y el digito verificador
    dfPACE2023.insert(0, "RUT", dfPACE2023.pop("RUT")) # Se mueve al inicio del dataframe
    dfPACE2023.drop("RUT_USACH", axis=1, inplace=True) # Se elimina la columna de rut usach
    dfPACE2023.drop("DV", axis=1, inplace=True) # Se elimina la columna de digito verificador

    dfPACE2023.columns = cambio_alumnos


    # print("PACE 2023")
    # dfPACE2023.info()
    # print(dfPACE2023.head())
    data.append(dfPACE2023) # Se agrega a la lista de datos

    dfSolicitudes = pd.read_excel(name, sheet_name= 3) # Se lee la tercera hoja del excel que contiene a los alumnos que solicitaron tutor
    dfSolicitudes = dfSolicitudes.iloc[:, 0:14] # Se eliminan las columnas de los tutores que tienen asigandos los datos
    dfSolicitudes.drop("NOMBRE SOCIAL", axis=1, inplace=True) # Se elimina la columna de nombre social
    dfSolicitudes["RUT"] = dfSolicitudes["RUT_USACH"].astype(str).str.cat(dfSolicitudes["DV"].astype(str), sep="-") # Se crea la columna RUT con el rut y el digito verificador
    dfSolicitudes.insert(0, "RUT", dfSolicitudes.pop("RUT")) # Se mueve al inicio del dataframe
    dfSolicitudes.drop("RUT_USACH", axis=1, inplace=True) # Se elimina la columna de rut usach
    dfSolicitudes.drop("DV", axis=1, inplace=True) # Se elimina la columna de digito verificador

    dfSolicitudes.columns = cambio_alumnos


    # print("Solicitudes")
    # dfSolicitudes.info()

    data.append(dfSolicitudes) # Se agrega a la lista de datos

    dfTutores = pd.read_excel(name, sheet_name= 4) # Se lee la cuarta hoja del excel que contiene a los tutores
    #concatenar dfTutores.iloc[:, 0:9] con dfTutores.iloc[:, 11]
    dfTutores = pd.concat([dfTutores.iloc[:, 0:9], dfTutores.iloc[:, 11]], axis=1) # Se concatenan las columnas de los tutores que tienen asigandos los datos
    
    print("Tutores")
    dfTutores.info()

    dfTutores.columns = cambio_tutores

    print("Tutores")
    dfTutores.info()


    data.append(dfTutores) # Se agrega a la lista de datos

    return data

""" transform_data_class """
"""

"""










def test():
    get_data("Resource\data.xlsx")

test()

