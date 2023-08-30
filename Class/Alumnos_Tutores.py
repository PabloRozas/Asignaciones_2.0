import pandas as pd
from Class.Alumno import Alumno
from Class.Tutor import Tutor
from Class.Alumnos import Alumnos
from Class.Tutores import Tutores

class Alumnos_Tutores:

    def __init__(self):
        self.alumnos_tutores = []

    def add_alumno_tutor(self, alumno, tutor):
        self.alumnos_tutores.append([alumno, tutor])

    def add_alumno(self, alumno):
        self.alumnos_tutores.append([alumno, None])


    def get_alumnos_tutores(self):
        return self.alumnos_tutores
    
    def get_total(self):
        return len(self.alumnos_tutores)
    
    def to_csv(self, path):
        # Se transforma la lista de alumntos_tutores a una lista que contenga el rut del alumno y el rut del tutor
        lista = []
        for alumno_tutor in self.alumnos_tutores:
            try:
                lista.append([alumno_tutor[0].get_rut(), alumno_tutor[1].get_rut()])
            except:
                lista.append([alumno_tutor[0].get_rut(), ""])
        # Se crea un dataframe con la lista
        df = pd.DataFrame(lista, columns=["Alumno", "Tutor"])
        # Se guarda el dataframe en un archivo csv
        df.to_csv(path, index=False)