import pandas as pd

class Alumnos:
    cantidad = 0
    def __init__(self):
        self.alumnos = []
        self.index = self.cantidad + 1
        self.cantidad += 1

    def add_alumno(self, alumno):
        self.alumnos.append(alumno)

    def get_alumnos(self):
        return self.alumnos

    def get_alumno(self, rut):
        for alumno in self.alumnos:
            if alumno.rut == rut:
                return alumno
        return None
    
    def get_total(self):
        return len(self.alumnos)
    
    def set_alumnos(self, alumnos):
        self.alumnos = alumnos
    
    def print_alumnos(self):
        for alumno in self.alumnos:
            print(alumno.rut, alumno.nombre_completo, alumno.carrera, alumno.facultad, alumno.via_paiep, alumno.ies_acompañamiento, alumno.correo_usach, alumno.correo_personal, alumno.telefono_1, alumno.telefono_2, alumno.matriculados2023)
            print("Estado: ", alumno.estado)
            print("Solicitud: ", alumno.solicitud_area, alumno.solicitud_subarea, alumno.solicitud_esp)

    def get_PACE(self):
        alumnos = []
        for alumno in self.alumnos:
            if "PACE" in alumno.via_paiep:
                alumnos.append(alumno)
        return alumnos
    

    def to_csv(self, path):
        # Se transforma la lista de alumnos a un dataframe
        df = pd.DataFrame(columns=['rut', 'nombre_completo', 'carrera', 'facultad', 'via_paiep', 'ies_acompañamiento', 'correo_usach', 'correo_personal', 'telefono_1', 'telefono_2', 'matriculados2023', 'estado', 'solicitud_area', 'solicitud_subarea', 'solicitud_esp'])
        for alumno in self.alumnos:
            new = pd.DataFrame({'rut': [alumno.rut], 'nombre_completo': [alumno.nombre_completo], 'carrera': [alumno.carrera], 'facultad': [alumno.facultad], 'via_paiep': [alumno.via_paiep], 'ies_acompañamiento': [alumno.ies_acompañamiento], 'correo_usach': [alumno.correo_usach], 'correo_personal': [alumno.correo_personal], 'telefono_1': [alumno.telefono_1], 'telefono_2': [alumno.telefono_2], 'matriculados2023': [alumno.matriculados2023], 'estado': [alumno.estado], 'solicitud_area': [alumno.solicitud_area], 'solicitud_subarea': [alumno.solicitud_subarea], 'solicitud_esp': [alumno.solicitud_esp]})
            df = pd.concat([df, new], ignore_index=True)

        # Se guarda el dataframe en un archivo csv
        df.to_csv(path, index=False)
    