class Alumnos:
    def __init__(self):
        self.alumnos = []

    def add_alumno(self, alumno):
        self.alumnos.append(alumno)

    def get_alumnos(self):
        return self.alumnos

    def get_alumno(self, rut):
        for alumno in self.alumnos:
            if alumno.rut == rut:
                return alumno
        return None
    
    def print_alumnos(self):
        for alumno in self.alumnos:
            print(alumno.rut, alumno.nombre_completo, alumno.carrera, alumno.facultad, alumno.via_acceso, alumno.via_paiep, alumno.ies_acompañamiento, alumno.correo_usach, alumno.correo_personal, alumno.telefono_1, alumno.telefono_2, alumno.matriculados2023)