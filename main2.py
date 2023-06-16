from Interface.gui import MiInterfaz
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    # app = QApplication([])

    # Se configura el icono de la aplicación
    # pixmap = QPixmap("Resource/Images/Logo.png")

    app_icon = QtGui.QIcon("Resource/Images/Logo.png")
    app.setWindowIcon(app_icon)
    
    
    interfaz = MiInterfaz()
    interfaz.show()
    app.exec_()