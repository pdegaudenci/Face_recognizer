#from embedding import generarembedding
import json
import cv2
from detector_MTCNN import pipeline_deteccion_webcam

diccionario={}
with open("./embeddings.json","r") as file:
    diccionario =json.load(file)



pipeline_deteccion_webcam(
    dic_referencia   = diccionario,
   threshold_similaridad = 0.4 )