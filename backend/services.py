import os
import cv2
from matplotlib import pyplot
from mtcnn.mtcnn import MTCNN
from os import getcwd
import numpy as np

TIPO_ARCHIVOS_IMG ="jpg"
SIMILITUD_BASE= 0.9

def orb_sim(img1, img2):
        orb = cv2.ORB_create()  # Creamos el objeto de comparacion
        kpa, descr_a = orb.detectAndCompute(img1, None)  # Creamos descriptor 1 y extraemos puntos claves
        kpb, descr_b = orb.detectAndCompute(img2, None)  # Creamos descriptor 2 y extraemos puntos claves

        comp = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)  # Creamos comparador de fuerza

        matches = comp.match(descr_a, descr_b)  # Aplicamos el comparador a los descriptores
        print(matches)
        regiones_similares = [i for i in matches if
                              i.distance < 70]  # Extraemos las regiones similares en base a los puntos claves
        if len(matches) == 0:
            return 0
        return len(regiones_similares) / len(matches)  # Exportamos el porcentaje de similitud

def existe_usuario(img, usuario):
    im_archivos = os.listdir(getcwd())
    for file  in im_archivos:
         global TIPO_ARCHIVOS_IMG 
         if  "." in file and TIPO_ARCHIVOS_IMG in file.split(".")[1]:
              print(file)
              #rostro_log = cv2.imdecode(np.fromstring(img, np.uint8), cv2.IMREAD_UNCHANGED)
              rostro_reg = cv2.imread(file, 0)  # Importamos el rostro del registro
              rostro_log = cv2.imread(img, 0)  # Importamos el rostro del inicio de sesion
              similitud = orb_sim(rostro_reg, rostro_log)
             # Defino que la similutud debe ser mayor a 0,90
              global SIMILITUD_BASE
              if similitud >= SIMILITUD_BASE:
                return usuario,similitud
              else:
                   
               return None,similitud
         else:
             return None,None
