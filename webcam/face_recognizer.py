
from datetime import datetime
import cv2
import numpy as np
import face_recognition as fr
import random
import os



# GENERACION DE EMBEDDINGS DE LAS CARAS : VECTORIZACION DE ROSTROS
def codificar_caras(imagenes):
    # Creo lista que contiene los embedings
    lista_cod=[]
    for img in imagenes:
        # Normalizar color al sistema RGB
        img= cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        # Codificar la foto de la cara : embedding
        cod=fr.face_encodings(img)[0]
        #Agrego lista
        lista_cod.append(cod)
    return lista_cod

#REGISTRO HORARIO (Estructura del archivo: nombre ,fecha, hora)
def registrar_horario(nombre):
    with open('registro_horario.txt','r+') as file:
        data= file.readline()
        #Lista con nombre de personas
        lista_nombres=[]
        # Itera lineas del archivo
        for linea in data:
            # Dividir cada linea en funcion del delimitador ","
            campos = linea.split(',').strip()
            lista_nombres.append(campos[0])

# Si el nombre no esta incluida en el archivo
    if nombre not in lista_nombres:
        #Informacion del instante actual
        registro_temporal=datetime.now()
        fecha=registro_temporal.strftime('%Y:%m:%d')
        hora=registro_temporal.strftime('%H:%M:%S')
        # Escribe datos de registro en archivo 
        file.writelines(["\n",nombre,fecha,hora])



def webcam_recognizer():
    path='imagenes'
    images=[]
    clases=[]
    ruta_actual=os.getcwd()
    os.chdir("./")
    lista=os.listdir(path)
    #os.chdir(ruta_actual)


    comp1=100

#LEER LAS IMAGENES DE CARPETA CON FOTOS DE ROSTROS Y AGREGARLO A LISTA
#iterar lista con imagenes
    for lis in lista:
 
        imgdb=cv2.imread(f'{path}/{lis}')
    # Se agrega imagen 
        images.append(imgdb)
    # Agrego nombre del archivo como nombre del rostro
        clases.append(os.path.splitext(lis)[0])
    #Codifico imagenes de la lista
    embeddings_faces= codificar_caras(images)

# Inicio videocamara
    captura = cv2.VideoCapture(0)
    while True:
        #Lectura de FPS
        ret,frame=captura.read()

        #Normalizar dimensionalidad de imagen
        frame2=cv2.resize(frame,(0,0),None,0.25,0.25)

        # Normalizar formato de color (OpenCv devuelve imagen en formato BGR)
        rgb=cv2.cvtColor(frame2,cv2.COLOR_BGR2RGB)

        #Deteccion de rostros con modulo face recognition
        rostros_coord=fr.face_locations(rgb)
        facescod = fr.face_encodings(rgb,rostros_coord)
      
        # Se itera sobre los rostros codificados de la imagen.
        for facecod,(top, right, bottom, left) in zip(facescod,rostros_coord):
                nombre="Desconocido"
                # Compara los embedding almacenados en la lista cargada de las imagenes con los 
                #embeddings de los rostros detectados en cada FPS
                coincidencia=fr.compare_faces(embeddings_faces,facecod)
                
                # Se calcula similitud de rostros en base a la distancia entre sus vectores representativos
                similitud =fr.face_distance(embeddings_faces,facecod)

                # Vector cuya distancia es minima (rostro similar)
                vector_min_index=np.argmin(similitud)
                
                if coincidencia[vector_min_index]:
                    nombre=clases[vector_min_index].upper()

                    #Coordenadas de los rostros
                    #yi,xf,yf,xi=faceloc

                    #Escalar
                    #yi,xf,yf,xi=yi*4,xf*4,yf*4,xi*4
                left*=4
                right*=4
                top*=4
                bottom*=4
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, nombre, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                    
            #Mostrar los frames o FPS por pantalla
        cv2.imshow("Reconocimiento facial ",frame)

            # Lectura de eventos del teclado
        key=cv2.waitKey(5)
            # Si el usuario presiona tecla de escape se sale de la aplicacion
        if key==27: 
                break
        captura.release()