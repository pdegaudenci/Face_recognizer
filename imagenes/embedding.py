#Un embbeding (vector de características) para la cara detectada en la imagen.
#Este embbeding puede ser utilizado para tareas como comparación facial o clasificación facial.

#Cargar el modelo MTCNN:
from mtcnn.mtcnn import MTCNN
detector = MTCNN()

#Cargar una red neuronal pre-entrenada para la extracción de características:
from keras.models import load_model
model = load_model("path/to/feature_extraction_model.h5")

#Extraer las características de una imagen y crear un embbeding:
import numpy as np
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

# cargar imagen
filename = "path/to/image.jpg"
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
features = model.predict(face)

# crear un embbeding a partir de las características
embedding = features[0]


