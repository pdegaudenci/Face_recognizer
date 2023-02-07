# --------------------------------------Importamos librerías--------------------------------------------

from tkinter import *
import os
import cv2
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN





# VAriable que contiene ruta de la carpeta donde se guardarán las imagenes resultantes del login facial
path = "./imagenes"
SIMILITUD_BASE=0.90

# --------------------------- Metodo que abre la camara para realiar captura de rostro y guarda imagen en carpeta correspondiente--------------------------------------
def registro_facial(usuario):
     # Elegimos la camara con la que vamos a hacer la deteccion
     cap = cv2.VideoCapture(0) 

     while (True):
        # LEctura de frames de la camara
        ret, frame = cap.read()  
         # Mostramos el video en pantalla
        cv2.imshow('Registro Facial', frame) 
        # Tecla Escpame para salir y hacer captura
        if cv2.waitKey(1) == 27:  
             break
     usuario_img = usuario.get()
     #Cambiar a directorio donde se guardara la imagen
     directorio_ppal=os.getcwd()
     os.chdir(path)
     # Guardamos la ultima caputra del video como imagen y asignamos el nombre del usuario
     cv2.imwrite(usuario_img + ".jpg", frame)  
     os.chdir(directorio_ppal)
     print(os.getcwd())
     cap.release()  # Cerramos
     cv2.destroyAllWindows()

     return True


# ---------- Metodo para realizar login facial , es decir, capturar imagen de la persona
# , guardarla y compararla con las imagenes alamacenadas correspondiente a usuarios registradas --------------------------------------------------------
def login_facial(verificacion_usuario,pantalla):
    # ------------------------------Vamos a capturar el rostro-----------------------------------------------------
    global pantalla2
    pantalla2=pantalla
    cap = cv2.VideoCapture(0)  # Elegimos la camara con la que vamos a hacer la deteccion
    while (True):
        ret, frame = cap.read()  # Leemos el video
        cv2.imshow('Login Facial', frame)  # Mostramos el video en pantalla
        if cv2.waitKey(1) == 27:  # Cuando oprimamos "Escape" rompe el video
            break
    usuario_login = verificacion_usuario.get()  # Con esta variable vamos a guardar la foto pero con otro nombre para no sobreescribir
    directorio = os.getcwd()
    os.chdir("./imagenes_LOG")
    cv2.imwrite(usuario_login + "LOG.jpg",
                frame)  # Guardamos la ultima captura del video como imagen y asignamos el nombre del usuario
    os.chdir(directorio)
    cap.release()  # Cerramos
    cv2.destroyAllWindows()



    # ----------------- Funcion para guardar el rostro --------------------------

    def log_rostro(img, lista_resultados):
        directorio_ppal=os.getcwd()
        os.chdir("./imagenes_LOG")
        data = pyplot.imread(img)
        os.chdir(directorio_ppal)
        for i in range(len(lista_resultados)):
            x1, y1, ancho, alto = lista_resultados[i]['box']
            x2, y2 = x1 + ancho, y1 + alto
            pyplot.subplot(1, len(lista_resultados), i + 1)
            pyplot.axis('off')
            cara_reg = data[y1:y2, x1:x2]
            cara_reg = cv2.resize(cara_reg, (150, 200), interpolation=cv2.INTER_CUBIC)  # Guardamos la imagen 150x200
            os.chdir("./imagenes_LOG")
            cv2.imwrite(usuario_login + "LOG.jpg", cara_reg)
            os.chdir(directorio_ppal)
            return pyplot.imshow(data[y1:y2, x1:x2])
        pyplot.show()

    # -------------------------- Detectamos el rostro-------------------------------------------------------

    os.chdir("./imagenes_LOG")
    img = usuario_login + "LOG.jpg"
    pixeles = pyplot.imread(img)
    os.chdir(directorio)
    detector = MTCNN()
    caras = detector.detect_faces(pixeles)
    log_rostro(img, caras)

    # -------------------------- Funcion para comparar similitud de los rostros usando la libreria opencv--------------------------------------------
    def orb_sim(img1, img2):
        orb = cv2.ORB_create()  # Creamos el objeto de comparacion

        kpa, descr_a = orb.detectAndCompute(img1, None)  # Creamos descriptor 1 y extraemos puntos claves
        kpb, descr_b = orb.detectAndCompute(img2, None)  # Creamos descriptor 2 y extraemos puntos claves

        comp = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)  # Creamos comparador de fuerza

        matches = comp.match(descr_a, descr_b)  # Aplicamos el comparador a los descriptores

        regiones_similares = [i for i in matches if
                              i.distance < 70]  # Extraemos las regiones similares en base a los puntos claves
        if len(matches) == 0:
            return 0
        return len(regiones_similares) / len(matches)  # Exportamos el porcentaje de similitud

    # ---------------------------- Importamos las imagenes y llamamos la funcion de comparacion ---------------------------------

    im_archivos = os.listdir(path)  # Vamos a importar la lista de archivos con la libreria os
    if usuario_login + ".jpg" in im_archivos:  # Comparamos los archivos con el que nos interesa
        # os.chdir(path)
        directorio_ppal = os.getcwd()
        os.chdir(path)
        ## Ejecutar función
        rostro_reg = cv2.imread(usuario_login + ".jpg", 0)  # Importamos el rostro del registro
        os.chdir(directorio_ppal)
        os.chdir("./imagenes_LOG")
        rostro_log = cv2.imread(usuario_login + "LOG.jpg", 0)  # Importamos el rostro del inicio de sesion
        os.chdir(directorio_ppal)
        similitud = orb_sim(rostro_reg, rostro_log)
        # Defino que la similutud debe ser mayor a 0,90
        if similitud >= SIMILITUD_BASE:
            return usuario_login,similitud
        else:
           return None,similitud
    else:
        return None,None
