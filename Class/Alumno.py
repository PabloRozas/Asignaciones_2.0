class Alumno:
    def __init__(self, rut, nombre_completo, carrera, facultad, via_paiep, ies_acompañamiento, correo_usach, correo_personal, telefono_1, telefono_2, matriculados2023):
        DISPONIBLE = 0
        ASIGNADO = 1
        ESPERA = 2
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
        self.estado = DISPONIBLE

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
    
    def set_estado(self, estado):
        self.estado = estado
    
    def print_alumno(self):
        print(self.rut, self.nombre_completo, self.carrera, self.facultad,  self.via_paiep, self.ies_acompañamiento, self.correo_usach, self.correo_personal, self.telefono_1, self.telefono_2, self.matriculados2023)


