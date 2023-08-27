<h1 align="center">
  <p align="left">Proyecto de Computer Vision Face Recognizer</p>
</h1>

# Descripción del proyecto 
Software de reconocimiento facial basada en redes neuronales convolucionales pre entrenadas, adaptadas al caso de uso planteado:

- **Interfaz grafica de usuario que permite registro facial de una persona y login facial**
- **En función de los embeddings de los rostros generados por la Red neuronal, debe permitir la identificación en tiempo real de las personas a traves de un dispositivo de tipo webcam.**

Actualmente , estoy realizando una versión 2.0 del prototipo para mejorar la interfaz gráfica , mediante la sustitucion de la libreria Tkinter con la libreria PySide6 y Qt Designer.

# :mechanical_arm:Estado del proyecto
:construction: Proyecto en construcción :construction:



## :hammer:Funcionalidades del proyecto

- `Funcionalidad 1`: registro facia.
- `Funcionalidad 2`: login facial para reconocer a los invitados en base a una base de datos de personas con credenciales de autenticación.
- `Funcionalidad 3`: reconocimiento facial en tiempo real, que identifica a personas de forma positivo (Nombre y apellido) o negativa , renderizando un bounding box en en los rostros detectados en el video de webcam.

### Prerequisites

* Docker engine, docker cli y docker-compose
  ```windows
        choco install docker-engine docker-cli docker-compose
     sh
     sudo apt update -y && sudo apt install docker-ce docker-ce-cli containerd.io
  ```

## 🛠️ Abre y ejecuta el proyecto

1. Crea un entorno específicamente para este proyecto. Por ejemplo: 
```
conda create -n nombreEntorno
```
3. Dentro de este entorno debes instalar todas las librerías necesarias con la siguiente línea de comando:
```
pip install requirements.txt
```
3. Situate en la carpeta raiz del proyecto y desde allí ejecute:
```
python3 main.py
```

## Despliegue 📦
_Despliegue de microservicios en contenedores (En construccion)_
 - Run `docker-compose up -d`
 - Rutas permitidas en http://localhost:9000 
# :wrench: Tecnologías usadas:

   - **Metodología Scrum**
   - **CI/CD** : Jenkins y sonarqube (Analisis de de calidad del codigo)
   - **Deployment**: Docker (orquestador : docker compose)
   - **Servidores ligeros**: ngrok y uvicorn
   - **Desarrollo**: Git y VSCode
   - **Libreria para tratamiento de imagenes:** matplotlib , PIL , OpenCV y tensorflow.keras.utils
   - **Redes neuronales:** FaceNet, MTCNN, face recognition, keras-Tensorflow y Pytorch 
   - **Libreria para tratamientos numericos:** Numpy
   - **Librerías para construccion de GUIs:** TKinter y PySide6


