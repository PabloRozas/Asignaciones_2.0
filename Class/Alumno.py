class Alumno:
    def __init__(self, rut, nombre_completo, carrera, facultad, via_paiep, ies_acompañamiento, correo_usach, correo_personal, telefono_1, telefono_2, matriculados2023, solicitud_area, solicitud_subarea, solicitud_esp):
        # Constantes de estado
        # DISPONIBLE = 0
        # ASIGNADO = 1
        # ESPERA = 2
        # PARCIAL = 3
        self.rut = rut
        self.nombre_completo = nombre_completo
        self.carrera = carrera
        self.facultad = facultad
        self.via_paiep = via_paiep
        self.ies_acompañamiento = ies_acompañamiento
        self.correo_usach = correo_usach
        self.correo_personal = correo_personal
        self.telefono_1 = telefono_1
        self.telefono_2 = telefono_2
        self.matriculados2023 = matriculados2023
        self.estado = 0
        self.solicitud_area = solicitud_area
        self.solicitud_subarea = solicitud_subarea
        self.solicitud_esp = solicitud_esp

        # Nivel de estudiante
        # Corresponde al semestre en el que se encuentra el estudiante (en evaluación si se mantiene)
        self.nivel = 0

    def get_rut(self):
        return self.rut
    
    def get_nombre_completo(self):
        return self.nombre_completo
    
    def get_carrera(self):
        return self.carrera
    
    def get_facultad(self):
        return self.facultad
    
    def get_via_paiep(self):
        return self.via_paiep
    
    def get_ies_acompañamiento(self):
        return self.ies_acompañamiento
    
    def get_correo_usach(self):
        return self.correo_usach
    
    def get_correo_personal(self):
        return self.correo_personal
    
    def get_telefono_1(self):
        return self.telefono_1
    
    def get_telefono_2(self):
        return self.telefono_2
    
    def get_matriculados2023(self):
        return self.matriculados2023
    
    def get_estado(self):
        return self.estado
    
    def get_solicitud_area(self):
        return self.solicitud_area
    
    def get_solicitud_subarea(self):
        return self.solicitud_subarea
    
    def get_solicitud_esp(self):
        return self.solicitud_esp
    
    def change_asignado(self):
        self.estado = 1
    
    def change_espera(self):
        self.estado = 2

    def change_parcial(self):
        self.estado = 3

    def change_nivel(self, nivel):
        self.nivel = nivel

    def print_alumno(self):
        print("---------------------------------------------------------------------")
        print("Alumno: ")
        print("Nivel: ", self.nivel)
        print(self.rut, self.nombre_completo, self.carrera, self.facultad,  self.via_paiep, self.ies_acompañamiento, self.correo_usach, self.correo_personal, self.telefono_1, self.telefono_2, self.matriculados2023)
        print("Estado: ", self.estado)
        print("Solicitud: ", self.solicitud_area, self.solicitud_subarea, self.solicitud_esp)


