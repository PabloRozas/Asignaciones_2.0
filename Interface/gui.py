import sys
import os
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog

# Obtiene la ruta absoluta de la carpeta actual
current_folder = os.path.dirname(os.path.abspath(__file__))
# print(current_folder)
# Construye la ruta de la carpeta Class
class_folder = os.path.abspath(os.path.join(current_folder, '..', 'Utils'))
# print(class_folder)
# Agrega la ruta de la carpeta Class al sistema de búsqueda de módulos
sys.path.append(class_folder)

from rw_data import get_data
from change_data import transform_data_class
from tree import tree


# Obtiene la ruta absoluta de la carpeta actual
current_folder = os.path.dirname(os.path.abspath(__file__))
# print(current_folder)
# Construye la ruta de la carpeta Class
class_folder = os.path.abspath(os.path.join(current_folder, '..', 'Resources'))
# print(class_folder)
# Agrega la ruta de la carpeta Class al sistema de búsqueda de módulos
sys.path.append(class_folder)

class MiInterfaz(QtWidgets.QMainWindow): # Hereda de QMainWindow
    def __init__(self):
        super().__init__() # Llama al constructor de QMainWindow
        self.init_ui() # Llama al método que inicializa la interfaz (Configuración del diseño)

    def init_ui(self):
        # Configura los componentes de tu interfaz aquí
        self.setWindowTitle("Asignación de tutores")
        self.setGeometry(100, 100, 400, 300)
        self.central_widget = QtWidgets.QWidget(self) 
        # self.showMaximized()
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QtWidgets.QGridLayout(self.central_widget)
        self.grid_layout.setAlignment(QtCore.Qt.AlignCenter)




        
        # Crea un label en el centro
        self.input_text = QtWidgets.QLineEdit(self)
        self.grid_layout.addWidget(self.input_text, 2, 0)
        


        
        # Crear un label debajo del botón con el resultado y que se ajuste al tamaño del texto
        self.resultado_label = QtWidgets.QLabel(self.central_widget)
        self.grid_layout.addWidget(self.resultado_label, 1, 0)
        self.resultado_label.setGeometry(QtCore.QRect(150, 200, 100, 30))
        self.resultado_label.setAlignment(QtCore.Qt.AlignCenter)
        self.resultado_label.setWordWrap(True)
        self.resultado_label.adjustSize()



        # Crea un botón en el centro
        self.button = QtWidgets.QPushButton("Ejecutar función", self.central_widget)
        self.grid_layout.addWidget(self.button, 0, 0)
        self.button.clicked.connect(self.ejecutar_funcion)

    def ejecutar_funcion(self):
        # Aquí puedes llamar a tu función específica de Python

        texto = self.input_text.text()
        if texto == "":
            texto = "0.1"
        float_texto = float(texto)
        resultado = tree(float_texto)  # Llama a tu función y obtén el resultado
        self.resultado_label.setText(str(resultado))
        self.resultado_label.adjustSize()

        
        texto = self.get_texto_actual()
        # Llama a la función con el texto actual

    def get_texto_actual(self):
        # Aquí puedes implementar la lógica para obtener el texto más reciente
        return "Texto actual"

