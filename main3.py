import dearpygui.dearpygui as dpg
import os
from Utils.tree import tree
from Utils.rw_data import get_data, asiganacion_to_excel

dpg.create_context() # Se crea el contexto de DearPyGui


#  BLOQUE PRINCIPAL
width1, height1 = 500, 400 # Se establece el tamaño del viewport
opcionSolicitudes = False
opcionCSV = False
opcionWarning = False
nombre = ""

def button_callback3(sender, app_data):
    dpg.set_value(item= "Estado", value= "Estado: Procesando")    
    salida = tree(dpg.get_value(item= "Tolerrancia"), opcionSolicitudes, opcionCSV, opcionWarning, dpg.get_value(item= "Ruta"))
    if salida[2] != "":
        dpg.set_value(item= "Error", value= salida[2])
    global nombre
    nombre = salida[1]
    if opcionWarning:
        dpg.set_value(item= "Salida", value= salida[0])
    if not opcionWarning:
        dpg.set_value(item= "Salida", value= "")
    dpg.set_value(item= "Estado", value= "Estado: Completado - Listo para recibir nuevas opciones")

def button_callback2(sender, app_data):
    # Se abre el archivo Resource\Asignaciones.xlsx
    global nombre
    os.startfile(nombre)

def button_callback(sender, app_data):
    dpg.set_value(item= "Estado", value= "Estado: Procesando")    
    salida = tree(dpg.get_value(item= "Tolerrancia"), opcionSolicitudes, opcionCSV, opcionWarning, dpg.get_value(item= "Ruta"))
    if salida[2] != "":
        dpg.set_value(item= "Error", value= salida[2])
    global nombre
    nombre = salida[1]
    if opcionWarning:
        dpg.set_value(item= "Salida", value= salida[0])
    dpg.set_value(item= "Estado", value= "Estado: Completado - Listo para recibir nuevas opciones")
    # Se cierra la ventana principal y se abre la ventana secundaria
    dpg.delete_item("Ventana Principal")
    
    with dpg.window(tag= "Ventana Secundaria"): # Se crea una ventana
        dpg.add_text("Asignaciones PAIEP", tag= "Titulo", color= [255, 255, 255])
        with dpg.group():
            dpg.add_input_text(tag= "Ruta", default_value= "Resource\data.xlsx", width= 200, label= "Ruta del archivo")
            dpg.add_input_float(tag= "Tolerrancia", default_value= 0.1, width= 200, step= 0.1, min_value= 0.0, max_value= 1.0, min_clamped= True, max_clamped= True, label= "Tolerancia", format= "%.1f") 
            dpg.add_checkbox(label= "Asignar a Solicitudes", tag= "asignarSol", default_value= False, callback= checkbox_callback)
            dpg.add_checkbox(label= "Escribir data en CSV", tag= "escribirCsv", default_value= False, callback= checkbox_callback2)
            dpg.add_checkbox(label= "Visualizar Warning de datos", tag= "verWarning", default_value= False, callback= checkbox_callback3)
            dpg.add_button(label= "Aceptar", width= 200, callback= button_callback3)
            dpg.add_text("Estado: Esperando ingreso de opciones", tag= "Estado")
            dpg.add_button(label= "Abrir Asignaciones.xlsx", width= 200, callback= button_callback2)
            dpg.add_text("", tag= "Error")
            dpg.add_text("", tag= "Salida")
    
    if not opcionWarning:
        dpg.set_value(item= "Salida", value= "")
    dpg.set_primary_window("Ventana Secundaria", True)

def checkbox_callback(sender, app_data):
    global opcionSolicitudes
    opcionSolicitudes = dpg.get_value(item= "asignarSol")

def checkbox_callback2(sender, app_data):
    global opcionCSV
    opcionCSV = dpg.get_value(item= "escribirCsv")

def checkbox_callback3(sender, app_data):
    global opcionWarning
    opcionWarning = dpg.get_value(item= "verWarning")

with dpg.window(tag= "Ventana Principal"): # Se crea una ventana
    dpg.add_text("Asignaciones PAIEP", tag= "Titulo", color= [255, 255, 255])
    with dpg.group():
        dpg.add_input_text(tag= "Ruta", default_value= "Resource\data.xlsx", width= 200, label= "Ruta del archivo")
        dpg.add_input_float(tag= "Tolerrancia", default_value= 0.1, width= 200, step= 0.1, min_value= 0.0, max_value= 1.0, min_clamped= True, max_clamped= True, label= "Tolerancia", format= "%.1f")   
        dpg.add_checkbox(label= "Asignar a Solicitudes", tag= "asignarSol", default_value= False, callback= checkbox_callback)
        dpg.add_checkbox(label= "Escribir data en CSV", tag= "escribirCsv", default_value= False, callback= checkbox_callback2)
        dpg.add_checkbox(label= "Visualizar Warning de datos", tag= "verWarning", default_value= False, callback= checkbox_callback3)
        dpg.add_button(label= "Aceptar", width= 200, callback= button_callback)
        dpg.add_text("Estado: Esperando ingreso de opciones", tag= "Estado")
        dpg.add_text("", tag= "Error")
        dpg.add_text("", tag= "Salida")



dpg.create_viewport(title= "Asignaciones PAIEP", width= width1, height= height1) # Se crea el viewport
dpg.setup_dearpygui() # Se configura DearPyGui
dpg.show_viewport() # Se muestra el viewport

dpg.set_primary_window("Ventana Principal", True) # Se establece la ventana principal

dpg.start_dearpygui() # Se inicia DearPyGui

dpg.destroy_context() # Se destruye el contexto de DearPyGui