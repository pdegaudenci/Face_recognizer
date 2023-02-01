#from embedding import generarembedding
import json
import cv2
from services.detector_MTCNN import *




def iniciar_webcam():
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    print(F'Running on device: {device}')
    dict_referencias = crear_diccionario_referencias(
                    folder_path    = './imagenes',
                    min_face_size  = 40,
                    min_confidence = 0.9,
                    device         = device,
                    verbose        = True
                  )
#tf = open("embeddings.json", "w")
#json.dump(dict_referencias,tf)


    with open('embeddings.json', 'r') as j:
        contents = json.loads(j.read())
     
    pipeline_deteccion_webcam(
        dic_referencia   = dict_referencias,
    threshold_similaridad = 0.4 )