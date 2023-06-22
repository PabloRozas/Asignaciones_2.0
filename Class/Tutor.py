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
        self.subarea = [subarea]
        self.horas = horas   
        self.asignado = False 
        self.cant_tutorados = 0

        if(self.horas == "nan"):
            self.horas = 0
        elif (int(self.horas) == 25):
            self.cant_tutorados = 4
        elif (int(self.horas) == 29):
            self.cant_tutorados = 5
        elif (int(self.horas) == 33):
            self.cant_tutorados = 6
        elif (int(self.horas) == 37):
            self.cant_tutorados = 7
        elif (int(self.horas) == 41):
            self.cant_tutorados = 8

        if ("CALCULO III" in self.subarea):
            self.subarea.append("ALGEBRA II Y CALCULO II")
            self.subarea.append("ALGEBRA I Y CALCULO I")
            self.subarea.append("MATEMATICA I")
            self.subarea.append("MATEMATICA II")
            self.subarea.append("MATEMATICA III")
            self.subarea.append("PENSAMIENTO MATEMATICO")
        elif ("ECUACIONES DIFERENCIALES" in self.subarea):
            self.subarea.append("ALGEBRA II Y CALCULO II")
            self.subarea.append("ALGEBRA I Y CALCULO I")
            self.subarea.append("MATEMATICA I")
            self.subarea.append("MATEMATICA II")
            self.subarea.append("MATEMATICA III")
            self.subarea.append("PENSAMIENTO MATEMATICO")
        elif ("CALCULO II" in self.subarea):
            self.subarea.append("ALGEBRA I Y CALCULO I")
            self.subarea.append("ALGEBRA II Y CALCULO II")
            self.subarea.append("MATEMATICA II")
            self.subarea.append("MATEMATICA I")
            self.subarea.append("PENSAMIENTO MATEMATICO")
        elif ("CALCULO I" in self.subarea):
            self.subarea.append("ALGEBRA I Y CALCULO I")
            self.subarea.append("MATEMATICA I")
            self.subarea.append("PENSAMIENTO MATEMATICO")
        elif ("ALGEBRA II Y CALCULO II" in self.subarea):
            self.subarea.append("ALGEBRA I Y CALCULO I")
            self.subarea.append("MATEMATICA II")
            self.subarea.append("MATEMATICA I")
            self.subarea.append("PENSAMIENTO MATEMATICO")
        elif ("ALGEBRA I Y CALCULO I" in self.subarea):
            self.subarea.append("MATEMATICA I")
            self.subarea.append("PENSAMIENTO MATEMATICO")
        elif ("MATEMATICA III" in self.subarea):
            self.subarea.append("MATEMATICA II")
            self.subarea.append("MATEMATICA I")
            self.subarea.append("PENSAMIENTO MATEMATICO")
        elif ("MATEMATICA II" in self.subarea):
            self.subarea.append("MATEMATICA I")
            self.subarea.append("PENSAMIENTO MATEMATICO")
        elif ("MATEMATICA I" in self.subarea):
            self.subarea.append("PENSAMIENTO MATEMATICO")



        # # Se asigna un nivel de prioridad a cada tutor
        # self.level = 0
        # if (self.area == "MATEMATICAS" and self.subarea == ""):


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
        print(self.rut, self.nombre_completo, self.carrera, self.facultad, self.correo_usach, self.telefono_1, self.correo_personal, self.area, self.subarea, self.horas, self.asignado)

    def is_asign(self):
        self.asignado = True
