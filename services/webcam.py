#Importacion de librerias
import json
import  torch
from .detector_MTCNN import pipeline_deteccion_webcam,crear_diccionario_referencias




def iniciar_webcam():
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    print(F'Running on device: {device}')

    # Obtengo diccionario de referencia de embeddings de las imagenes almacenadas en carpeta imagenes
    dict_referencias = crear_diccionario_referencias(
                    folder_path    ='imagenes',
                    min_face_size  = 40,
                    min_confidence = 0.9,
                    device         = device,
                    verbose        = True
                  )
#tf = open("embeddings.json", "w")
#json.dump(dict_referencias,tf)


    # Inicia proceso de deteccion de caras , abriendo una nueva ventana
    pipeline_deteccion_webcam(
        dic_referencia   = dict_referencias,
        output_device="Fiesta Factoria F5",
        threshold_similaridad = 0.4 )
