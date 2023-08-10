import pandas as pd
import Alumno
import Tutor

class Alumnos_Tutores:

    def __init__(self):
        self.alumnos_tutores = []

    def add_alumno_tutor(self, alumno, tutor):
        self.alumnos_tutores.append([alumno.get_rut(), tutor.get_rut()])


    def get_alumnos_tutores(self):
        return self.alumnos_tutores
    
    def get_total(self):
        return len(self.alumnos_tutores)
    
    def to_csv(self, path):
        # Se transforma la lista de tutores a un dataframe
        df = pd.DataFrame(self.alumnos_tutores, columns=["Alumno", "Tutor"])
        # Se guarda el dataframe en un archivo csv
        df.to_csv(path, index=False)
