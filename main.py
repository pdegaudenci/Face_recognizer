from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile
from Gui.VentanaPrincipal1 import Ventana
#from Gui.VentanaPrincipal import Ui_MainWindow
#from Vistas import interfaz


if __name__ == "__main__":

    app = QApplication([])
    myWidget = Ventana()
    myWidget.show()
    app.exec()



#interfaz.pantalla_principal()