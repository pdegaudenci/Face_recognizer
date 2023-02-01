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
embedder = FaceNet()
#Cargar una red neuronal pre-entrenada para la extracción de características:
#from keras.models import load_model
#model = load_model("model.h5")


# cargar imagen
path = "imagenes_embbeding"
lista = os.listdir(path)
print(lista)

os.chdir(path)

def generarembedding(filename):
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
#creación del diccionario de referencia
dic={}
for filename in lista:
    embedding=generarembedding(filename)
    name=filename.split(".")[0]
    dic[name]=embedding.tolist()

tf = open("embeddings.json", "w")
json.dump(dic,tf)
tf.close()