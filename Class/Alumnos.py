class Alumnos:
    def __init__(self):
        self.alumnos = []

    def add_alumno(self, alumno):
        self.alumnos.append(alumno)

    def get_alumnos(self):
        return self.alumnos
