#from embedding import generarembedding
import json
import  torch
from .detector_MTCNN import pipeline_deteccion_webcam,crear_diccionario_referencias




def iniciar_webcam():
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    print(F'Running on device: {device}')
    dict_referencias = crear_diccionario_referencias(
                    folder_path    ='imagenes',
                    min_face_size  = 40,
                    min_confidence = 0.9,
                    device         = device,
                    verbose        = True
                  )
#tf = open("embeddings.json", "w")
#json.dump(dict_referencias,tf)



     
    pipeline_deteccion_webcam(
        dic_referencia   = dict_referencias,
        threshold_similaridad = 0.4 )