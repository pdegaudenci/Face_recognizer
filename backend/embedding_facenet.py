#Un embbeding (vector de características) para la cara detectada en la imagen.
#Este embbeding puede ser utilizado para tareas como comparación facial o clasificación facial.
#Extraer las características de una imagen y crear un embbeding:
import cv2
import numpy as np
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
import os
#Cargar el modelo MTCNN:
from mtcnn.mtcnn import MTCNN
detector = MTCNN()
from keras_facenet import FaceNet
import json



# cargar imagen
path = "imagenes_embbeding"

#creación del diccionario de referencia
def generarembedding_facenet(filename, path):
    os.chdir(path)
    embedder = FaceNet()
    pixels = load_img(filename, target_size=(160, 160))

# convertir imagen a array numpy
    pixels = img_to_array(pixels)

# detectar rostros en la imagen
    faces = detector.detect_faces(pixels)

# extraer la primera cara encontrada
    x1, y1, width, height = faces[0]["box"]
    x2, y2 = x1 + width, y1 + height
    face = pixels[y1:y2, x1:x2]

# cargar la imagen de la cara y preprocesar para que tenga el mismo formato que las imágenes usadas durante el entrenamiento
    face = cv2.resize(face, (160, 160))
    face = face.astype("float32")
    mean, std = face.mean(), face.std()
    face = (face - mean) / std

# expandir el tamaño de la imagen para ser adecuado para el modelo
    face = np.expand_dims(face, axis=0)

# extraer las características de la cara
    #features = model.predict(face)

# crear un embbeding a partir de las características
    #embedding = features[0]
    embeddings = embedder.embeddings(face)
    return embeddings


# Guardar diccionario de referencia
def guardar_embedding_facenet(path_input,path_output):
    directorio_actual= os.getcwd()
    lista = os.listdir(path_input)
    dic={}
    os.chdir(path_input)
    for filename in lista:
        embedding=generarembedding_facenet(filename,path_input)
        name=filename.split(".")[0]
        dic[name]=embedding.tolist()
    os.chdir(directorio_actual)
    os.chdir(path_output)
    tf = open("embeddings.json", "w")
    json.dump(dic,tf)
    tf.close()