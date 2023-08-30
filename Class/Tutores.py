import pandas as pd

class Tutores:
    def __init__(self):
        self.tutores = []

    def add_tutor(self, tutor):
        self.tutores.append(tutor)

    def get_tutores(self):  
        return self.tutores
    
    def get_tutor(self, rut):
        for tutor in self.tutores:
            if tutor.rut == rut:
                return tutor
        return None
    
    def get_total(self):
        return len(self.tutores)
    
    def print_tutores(self):

        for tutor in self.tutores:
            print(tutor.rut, tutor.nombre_completo, tutor.carrera, tutor.facultad, tutor.correo_usach, tutor.telefono_1, tutor.correo_personal, tutor.area, tutor.subarea, tutor.horas)

    def get_AMate(self):
        tutores = []
        for tutor in self.tutores:
            if tutor.area == "MATEMATICAS":
                tutores.append(tutor)
        return tutores
    
    def get_ACien(self):
        tutores = []
        for tutor in self.tutores:
            if tutor.area == "CIENCIAS":
                tutores.append(tutor)
        return tutores
    
    def get_AHum(self):
        tutores = []
        for tutor in self.tutores:
            if tutor.area == "HUMANIDADES Y CIENCIAS SOCIALES":
                tutores.append(tutor)
        return tutores
    
    def get_AIdio(self):
        tutores = []
        for tutor in self.tutores:
            if tutor.area == "IDIOMAS":
                tutores.append(tutor)
        return tutores
    
    def get_TutoresBH(self):
        # Se obtiene una lista de tutores ordenados de mayor a menor según su nivel + horas reservadas
        tutores = self.tutores
        tutores.sort(key=lambda x: x.level + x.horasReservadas)
    
    def sort_tutores(self):
        self.tutores.sort(key=lambda x: len(x.subarea))

    
    def to_csv(self, path):
        # Se transforma la lista de tutores a un dataframe
        df = pd.DataFrame(columns=['rut', 'nombre_completo', 'carrera', 'facultad', 'correo_usach', 'telefono_1', 'correo_personal', 'area', 'subarea', 'horas', 'nivel', 'horas_reservadas'])
        for tutor in self.tutores:
            new = pd.DataFrame({'rut': [tutor.rut], 'nombre_completo': [tutor.nombre_completo], 'carrera': [tutor.carrera], 'facultad': [tutor.facultad], 'correo_usach': [tutor.correo_usach], 'telefono_1': [tutor.telefono_1], 'correo_personal': [tutor.correo_personal], 'area': [tutor.area], 'subarea': [tutor.subarea], 'horas': [tutor.horas], 'nivel': [tutor.level], 'horas_reservadas': [tutor.horasReservadas]})
            df = pd.concat([df, new], ignore_index=True)

        # Se guarda el dataframe en un archivo csv
        df.to_csv(path, index=False, header=True)
