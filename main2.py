from Interface.gui import MiInterfaz
from PyQt5 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    interfaz = MiInterfaz()
    interfaz.show()
    app.exec_()