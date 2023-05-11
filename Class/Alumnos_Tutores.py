class Alumnos_Tutores:
    def __init__(self):
        self.alumnos_tutores = []

    def add_alumno_tutor(self, alumno, tutor):
        self.alumnos_tutores.append([alumno, tutor])