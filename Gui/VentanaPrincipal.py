# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUIPrincipal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtWidgets import QApplication

import resources

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(901, 762)
        icon = QIcon()
        icon.addFile(u":/images/Icono ventana.png", QSize(), QIcon.Normal, QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
       
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, -20, 871, 871))
        self.frame.setStyleSheet(u"background-image: url(:/images/fondo.jpg)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget = QWidget(self.frame)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(280, 190, 361, 341))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.iniciar_sesion = QPushButton(self.verticalLayoutWidget)
        self.iniciar_sesion.setObjectName(u"iniciar_sesion")
        self.iniciar_sesion.setStyleSheet(u"color:rgb(240, 240, 240)")

        self.verticalLayout.addWidget(self.iniciar_sesion)

        self.registro = QPushButton(self.verticalLayoutWidget)
        self.registro.setObjectName(u"registro")
        self.registro.setStyleSheet(u"color:rgb(240, 240, 240)")

        self.verticalLayout.addWidget(self.registro)

        self.deteccion_facial = QPushButton(self.verticalLayoutWidget)
        self.deteccion_facial.setObjectName(u"deteccion_facial")
        self.deteccion_facial.setStyleSheet(u"color:rgb(240, 240, 240)")

        self.verticalLayout.addWidget(self.deteccion_facial)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 901, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Face Recognizer ", None))
        self.iniciar_sesion.setText(QCoreApplication.translate("MainWindow", u"Iniciar Sesion", None))
        self.registro.setText(QCoreApplication.translate("MainWindow", u"Registro", None))
        self.deteccion_facial.setText(QCoreApplication.translate("MainWindow", u"Iniciar deteccion facial", None))
    # retranslateUi

if __name__ == "__main__":

    app = QApplication([])
    ventana = Ui_MainWindow()
    ventana.show()
    app.exec()
