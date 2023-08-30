class Tutor:
    def __init__(self, rut, nombre_completo, carrera, facultad, correo_usach, telefono_1, correo_personal, area, subarea, horas, horasReservadas, observacion):
        
        
        
        try:
            self.asignado = int(observacion) # Cantidad de alumnos que tiene asignado
        except:
            self.asignado = 0
        
        
        self.rut = rut
        self.nombre_completo = nombre_completo
        self.carrera = carrera
        self.facultad = facultad
        self.correo_usach = correo_usach
        self.telefono_1 = telefono_1
        self.correo_personal = correo_personal
        self.area = area
        self.primSubarea = subarea
        self.subarea = [subarea]
        self.horas = int(horas - horasReservadas)
        self.cant_tutorados = 0
        self.level = 0
        self.ramosAsignados = []
        self.horasReservadas = int(horasReservadas)

        if(self.horas == "nan"):
            self.horas = 0
        elif (int(self.horas) == 25):
            self.cant_tutorados = 5
        elif (int(self.horas) == 29):
            self.cant_tutorados = 6
        elif (int(self.horas) == 33):
            self.cant_tutorados = 7
        elif (int(self.horas) == 37):
            self.cant_tutorados = 8
        elif (int(self.horas) == 41):
            self.cant_tutorados = 9

        if ("CALCULO III" in self.subarea):
            self.subarea.append("ALGEBRA II Y CALCULO II")
            self.subarea.append("ALGEBRA I Y CALCULO I")
            self.subarea.append("MATEMATICA I")
            self.subarea.append("MATEMATICA II")
            self.subarea.append("MATEMATICA III")
            self.subarea.append("PENSAMIENTO MATEMATICO")
            self.level = 5
        elif ("ECUACIONES DIFERENCIALES" in self.subarea):
            self.subarea.append("ALGEBRA II Y CALCULO II")
            self.subarea.append("ALGEBRA I Y CALCULO I")
            self.subarea.append("MATEMATICA I")
            self.subarea.append("MATEMATICA II")
            self.subarea.append("MATEMATICA III")
            self.subarea.append("PENSAMIENTO MATEMATICO")
            self.level = 5
        elif ("CALCULO II" in self.subarea):
            self.subarea.append("ALGEBRA I Y CALCULO I")
            self.subarea.append("ALGEBRA II Y CALCULO II")
            self.subarea.append("MATEMATICA II")
            self.subarea.append("MATEMATICA I")
            self.subarea.append("PENSAMIENTO MATEMATICO")
            self.level = 4
        elif ("CALCULO I" in self.subarea):
            self.subarea.append("ALGEBRA I Y CALCULO I")
            self.subarea.append("MATEMATICA I")
            self.subarea.append("PENSAMIENTO MATEMATICO")
            self.level = 3
        elif ("ALGEBRA II Y CALCULO II" in self.subarea):
            self.subarea.append("ALGEBRA I Y CALCULO I")
            self.subarea.append("MATEMATICA II")
            self.subarea.append("MATEMATICA I")
            self.subarea.append("PENSAMIENTO MATEMATICO")
            self.level = 4
        elif ("ALGEBRA I Y CALCULO I" in self.subarea):
            self.subarea.append("MATEMATICA I")
            self.subarea.append("PENSAMIENTO MATEMATICO")
            self.level = 3
        elif ("MATEMATICA III" in self.subarea):
            self.subarea.append("MATEMATICA II")
            self.subarea.append("MATEMATICA I")
            self.subarea.append("PENSAMIENTO MATEMATICO")
            self.level = 4
        elif ("MATEMATICA II" in self.subarea):
            self.subarea.append("MATEMATICA I")
            self.subarea.append("PENSAMIENTO MATEMATICO")
            self.level = 3
        elif ("MATEMATICA I" in self.subarea):
            self.subarea.append("PENSAMIENTO MATEMATICO")
            self.level = 2
        elif ("PENSAMIENTO MATEMATICO" in self.subarea):
            self.level = 1
        if ("ESTADISTICA Y PROBABILIDAD" in self.subarea):
            self.subarea.append("ESTADISTICA")
            




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
    
    def get_primSubarea(self):
        return self.primSubarea
    
    def get_cantTutorados(self):
        return self.cant_tutorados

    def get_ramosAsignados(self):
        return self.ramosAsignados
    
    def get_horasReservadas(self):
        return self.horasReservadas
    
    def get_asign(self):
        return self.asignado

    def set_horas(self, horas):
        self.horas = horas

    def set_cantTutorados(self, cant_tutorados):
        self.cant_tutorados = cant_tutorados
    
    def agregar_ramo(self, ramo):
        self.ramosAsignados.append(ramo)

    def print_tutor(self):
        print(self.rut, self.nombre_completo, self.carrera, self.facultad, self.correo_usach, self.telefono_1, self.correo_personal, self.area, self.subarea, self.horas, self.asignado, self.cant_tutorados, self.level)

    def asign(self):
        self.asignado += 1
