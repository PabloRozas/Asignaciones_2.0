import pandas as pd



""" get_data """
""" 
Descripción: Función que lee los datos de los alumnos y los tutrores de un archivo excel y estos son almacenados en una lista que es retornada, donde 
el index 0 es para VAE, 1 para PACE, 3 Solicitudes y 4 para los tutores
Entrada: name (nombre en string del archivo excel)
Salida: data (lista con los datos de los alumnos y tutores)
"""
def get_data(name):
    data = []
    dfVAE2023 = pd.read_excel(name, sheet_name= 1) # Se lee la primera hoja del excel que contiene a los alumnos VAE 2023
    dfVAE2023 = dfVAE2023.iloc[:, 0:13] # Se eliminan las columnas de los tutores que tienen asigandos los datos
    dfVAE2023.drop("NOMBRE SOCIAL", axis=1, inplace=True) # Se elimina la columna de nombre social
    #df.info()
    data.append(dfVAE2023) # Se agrega a la lista de datos

    dfPACE2023 = pd.read_excel(name, sheet_name= 2) # Se lee la segunda hoja del excel que contiene a los alumnos PACE 2023
    dfPACE2023 = dfPACE2023.iloc[:, 0:13] # Se eliminan las columnas de los tutores que tienen asigandos los datos
    dfPACE2023.drop("NOMBRE SOCIAL", axis=1, inplace=True) # Se elimina la columna de nombre social
    #dfPACE2023.info()

    data.append(dfPACE2023) # Se agrega a la lista de datos

    dfSolicitudes = pd.read_excel(name, sheet_name= 3) # Se lee la tercera hoja del excel que contiene a los alumnos que solicitaron tutor
    dfSolicitudes = dfSolicitudes.iloc[:, 0:13] # Se eliminan las columnas de los tutores que tienen asigandos los datos
    dfSolicitudes.drop("NOMBRE SOCIAL", axis=1, inplace=True) # Se elimina la columna de nombre social
    #dfSolicitudes.info()

    data.append(dfSolicitudes) # Se agrega a la lista de datos

    dfTutores = pd.read_excel(name, sheet_name= 4) # Se lee la cuarta hoja del excel que contiene a los tutores
    dfTutores = dfTutores.iloc[:, 0:9] # Se cortan los datos hasta donde se encuentra información 
    dfTutores.info()

    data.append(dfTutores) # Se agrega a la lista de datos

    return data

""" transform_data_class """
"""

"""










def test():
    get_data("Resource\data.xlsx")

test()

