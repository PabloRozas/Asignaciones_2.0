class Tutor:
    def __init__(self, rut, nombre_completo, carrera, facultad, correo_usach, telefono_1, correo_personal, area, subarea, horas):
        self.rut = rut
        self.nombre_completo = nombre_completo
        self.carrera = carrera
        self.facultad = facultad
        self.correo_usach = correo_usach
        self.telefono_1 = telefono_1
        self.correo_personal = correo_personal
        self.area = area
        self.subarea = subarea
        self.horas = horas   

    def get_rut(self):
        return self.rut
    
    def get_nombre_completo(self):
        return self.nombre_completo
    
    def get_carrera(self):
        return self.carrera
    
    def get_facultad(self):
        return self.facultad
    
    def get_correo_usach(self):
        return self.correo_usach
    
    def get_telefono_1(self):
        return self.telefono_1
    
    def get_correo_personal(self):
        return self.correo_personal

    def get_area(self):
        return self.area
    
    def get_subarea(self):
        return self.subarea
    
    def get_horas(self):
        return self.horas
    
    def print_tutor(self):
        print(self.rut, self.nombre_completo, self.carrera, self.facultad, self.correo_usach, self.telefono_1, self.correo_personal, self.area, self.subarea, self.horas)