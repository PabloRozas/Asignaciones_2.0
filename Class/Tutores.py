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
    
    def print_tutores(self):

        for tutor in self.tutores:
            print(tutor.rut, tutor.nombre_completo, tutor.carrera, tutor.facultad, tutor.correo_usach, tutor.telefono_1, tutor.correo_personal, tutor.area, tutor.subarea, tutor.horas)