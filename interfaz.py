
# Importamos librerías
from tkinter import *
import os
import cv2
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
import numpy as np
from webcam import iniciar_webcam
import importlib
from login import login, registro_facial

# Paso 2------------- Creamos una función que crear ficheros para guardar imágenes ---------------------
path = "imagenes"

def crear_fichero_imagenes():
    folder_name = 'imagenes'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    folder_name1 = 'imagenes_LOG'
    if not os.path.exists(folder_name1):
            os.makedirs(folder_name1)

def registro():
    global usuario
    global contra  # Globalizamos las variables para usarlas en otras funciones
    global usuario_entrada
    global pantalla1
    pantalla1 = Toplevel(pantalla)  # Esta pantalla es de un nivel superior a la principal
    pantalla1.title("Registro")
    pantalla1.geometry("300x250")  # Asignamos el tamaño de la ventana

    # --------- Empezaremos a crear las entradas ----------------------------------------

    usuario = StringVar()

    Label(pantalla1, text="Registro facial: debe de asignar un usuario:").pack()
    Label(pantalla1, text="").pack()  # Dejamos un poco de espacio
    Label(pantalla1, text="Usuario * ").pack()  # Mostramos en la pantalla 1 el usuario
    usuario_entrada = Entry(pantalla1,
                            textvariable=usuario)  # Creamos un text variable para que el usuario ingrese la info
    usuario_entrada.pack()

    # ------------ Vamos a crear el boton para hacer el registro facial --------------------
    Label(pantalla1, text="").pack()
    Button(pantalla1, text="Registro Facial", width=15, height=1, command=registro_facial_interfaz()).pack()


def registro_facial_interfaz():
    if registro_facial():
        Label(pantalla1, text="Registro Facial Exitoso", fg="green", font=("Calibri", 11)).pack()

# PASO 5------------------------Funcion que asignaremos al boton login -------------------------------------------------
def login():
    global pantalla2
    global verificacion_usuario
    global verificacion_contra
    global usuario_entrada2
    global contra_entrada2

    pantalla2 = Toplevel(pantalla)
    pantalla2.title("Login")
    pantalla2.geometry("300x250")  # Creamos la ventana
    Label(pantalla2, text="Login facial: debe de ingresar un usuario:").pack()
    Label(pantalla2, text="").pack()  # Dejamos un poco de espacio

    verificacion_usuario = StringVar()
    verificacion_contra = StringVar()

    # ---------------------------------- Ingresamos los datos --------------------------
    Label(pantalla2, text="Usuario * ").pack()
    usuario_entrada2 = Entry(pantalla2, textvariable=verificacion_usuario)
    usuario_entrada2.pack()

    # ------------ Vamos a crear el boton para hacer el login facial --------------------
    Label(pantalla2, text="").pack()
    Button(pantalla2, text="Inicio de Sesion Facial", width=20, height=1, command=login_facial).pack()

# PASO 2--------------- Funcion de nuestra pantalla principal ------------------------------------------------

def pantalla_principal():
    crear_fichero_imagenes()
    global pantalla  # Globalizamos la variable para usarla en otras funciones
    pantalla = Tk()
    pantalla.geometry("300x250")  # Asignamos el tamaño de la ventana
    pantalla.title("FacialRecognitionF5")  # Asignamos el titulo de la pantalla
    Label(text="Login Inteligente", bg="gray", width="300", height="2",
          font=("Verdana", 13)).pack()  # Asignamos caracteristicas de la ventana

    # ------------------------- Vamos a Crear los Botones ------------------------------------------------------

    Label(text="").pack()  # Creamos el espacio entre el titulo y el primer boton
    Button(text="Iniciar Sesion", height="2", width="30", command=login).pack()
    Label(text="").pack()  # Creamos el espacio entre el primer boton y el segundo boton
    Button(text="Registro", height="2", width="30", command=registro).pack()
    Label(text="").pack()  # Creamos el espacio entre el primer boton y el segundo boton
    Button(text="Iniciar detección facial", height="2", width="30", command=iniciar_webcam).pack()
    pantalla.mainloop()


pantalla_principal()
