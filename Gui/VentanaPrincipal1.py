from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QApplication

class Ventana(QMainWindow):
      def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Face Recognizer")
        self.resize(901, 762)
        icon = QIcon("./icono_ventana.png")
        
        self.layoutPrincipal = QHBoxLayout()
        self.botonLogin= QPushButton("Login")
        self.botonRegistro= QPushButton("Registro")
        self.botonRegistro.hide()

        self.layoutPrincipal.addWidget(self.botonLogin)
        self.layoutPrincipal.addWidget(self.botonRegistro)
        self.widget = QFrame()
        self.widget.setStyleSheet(".QFrame {background-image:url(fondo.jpg)}")
      
        self.widget.setLayout(self.layoutPrincipal)
        self.setCentralWidget(self.widget)

        # Señales y ranuras o listeners
        self.botonLogin.clicked.connect(self.login)
      
      def login(self):
         self.botonRegistro.show()
        
