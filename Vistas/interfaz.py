
# Importamos librerías
from tkinter import *
import os
import importlib


#-------------------------------------------------------------------------------------------
# 
#                   IMPORTACION DE PAQUETES Y SUBMODULOS DE LA APLICACION
# -------------------------------------------------------------------------------------------
loader_service_auth=importlib.import_module('.service_auth',package='services')
loader_webcam=importlib.import_module('.webcam',package='services')

#-------------------------------------------------------------------------------------------
# 
#                   DEFINICION DE METODOS DE LA INTERFAZ GRAFICA CONSTRUIDA CON TKINTER
# -------------------------------------------------------------------------------------------


def login():
    #Declaracion de variables globales que seran accesibles por el resto de los metodos de este submodulo
    global pantalla2
    global verificacion_usuario
    global usuario_entrada2
    
    # Creacion pantalla login y atributos de configuracion
    pantalla2 = Toplevel(pantalla)
    pantalla2.title("Login facial")
    # Asignamos el tamaño de la ventana
    pantalla2.geometry("300x250")  
    Label(pantalla2, text="Login facial: debe de ingresar un usuario:").pack()
    Label(pantalla2, text="").pack()  # Dejamos un poco de espacio

    verificacion_usuario = StringVar()


    # ---------------------------------- InputText para que usuario ingrese datos --------------------------
    Label(pantalla2, text="Usuario * ").pack()
    usuario_entrada2 = Entry(pantalla2, textvariable=verificacion_usuario)
    usuario_entrada2.pack()

    # ------------ Boton para hacer el login facial --------------------
    Label(pantalla2, text="").pack()
    Button(pantalla2, text="Inicio de Sesion Facial", width=20, height=1, command=verificar_usuario).pack()

# Metodo que invoca a metodo login_facial del submodulo de auth_service y en funcion de su retorno, mostrara elemento visual de tipo Label con diferente contenido
def verificar_usuario():
    usuario_login,similitud=loader_service_auth.login_facial(verificacion_usuario,pantalla2)
    if usuario_login!=None:
        Label(pantalla2, text="Inicio de Sesión Exitoso", fg="green", font=("Calibri", 11)).pack()
        print("Bienvenido al sistema usuario: ", usuario_login)
        print("Compatibilidad con la foto del registro: ", similitud)
    elif similitud!=None:
        print("Rostro incorrecto, Certifique su usuario")
        print("Compatibilidad con la foto del registro: ", similitud)
        Label(pantalla2, text="Incompatibilidad de rostros", fg="red", font=("Calibri", 11)).pack()
    else:
        print("Usuario no encontrado")
        Label(pantalla2, text="Usuario no encontrado", fg="red", font=("Calibri", 11)).pack()
    usuario_entrada2.delete(0, END)  # Limpiamos los text variables

# ------------ Creamos una función que crear ficheros para guardar imágenes ---------------------
path = "./imagenes"

def crear_fichero_imagenes():
    folder_name = 'imagenes'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    folder_name1 = 'imagenes_LOG'
    if not os.path.exists(folder_name1):
            os.makedirs(folder_name1)

# Creacion de pantalla de registro
def registro():
    global usuario
    global usuario_entrada
    global pantalla1
    pantalla1 = Toplevel(pantalla)  # Esta pantalla es de un nivel superior a la principal
    pantalla1.title("Registro")
    pantalla1.geometry("300x250")  

    # Variable que almacena usuario ingresado
    usuario = StringVar()

    Label(pantalla1, text="Registro facial: debe de asignar un usuario:").pack()
    Label(pantalla1, text="").pack()  # Dejamos un poco de espacio
    Label(pantalla1, text="Usuario * ").pack()  # Mostramos en la pantalla 1 el usuario
    usuario_entrada = Entry(pantalla1,
                            textvariable=usuario)  # Creamos un text variable para que el usuario ingrese la info
    usuario_entrada.pack()

    # ------------ Boton que invoca a funcion registro_facial_interfaz --------------------
    Label(pantalla1, text="").pack()
    Button(pantalla1, text="Registro Facial", width=15, height=1, command=registro_facial_interfaz).pack()


# Metodo que invoca a a metodo resgistro facial del submodulo service_auth, y en funcion del resultado muestra un label 
def registro_facial_interfaz():
    if loader_service_auth.registro_facial(usuario):
        usuario_entrada.delete(0, END)  # Limpiamos los text variables
        Label(pantalla1, text="Registro Facial Exitoso", fg="green", font=("Calibri", 11)).pack()
    else:
        Label(pantalla1, text="Registro Facial -erroneo", fg="red", font=("Calibri", 11)).pack()



# --------------- DEclaracion de la pantalla principal , que dará acceso a todas las funcionalidades de la aplicacion ------------------------------------------------

def pantalla_principal():
    crear_fichero_imagenes()
    # Globalizamos la variable para usarla en otras funciones
    global pantalla  
    pantalla = Tk()
    pantalla.geometry("300x250")  # Asignamos el tamaño de la ventana
    pantalla.title("FacialRecognitionF5")  # Asignamos el titulo de la pantalla
    Label(text="Login Inteligente", bg="gray", width="300", height="2",
          font=("Verdana", 13)).pack()  # Asignamos caracteristicas de la ventana

    # -------------------------  Botones , que al ejecutarse un evento click invocarán a las distintas funcionalidades del programa ------------------------------------------------------

    Label(text="").pack()  # Creamos el espacio entre el titulo y el primer boton
    Button(text="Iniciar Sesion", height="2", width="30", command=login).pack()
    Label(text="").pack()  # Creamos el espacio entre el primer boton y el segundo boton
    Button(text="Registro", height="2", width="30", command=registro).pack()
    Label(text="").pack()  # Creamos el espacio entre el primer boton y el segundo boton
    Button(text="Iniciar detección facial", height="2", width="30", command=loader_webcam.iniciar_webcam).pack()
    pantalla.mainloop()


pantalla_principal()
