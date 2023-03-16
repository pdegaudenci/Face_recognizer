<h1 align="center">
  <p align="left">Proyecto de Computer Vision Face Recognizer</p>
  <img align="center" width="300" height="300" src="https://user-images.githubusercontent.com/108665441/217483255-1d0f97e5-25b4-4d7b-b6f6-8bbb0057a432.png">
</h1>

# Descripción del proyecto 
Software de reconocimiento facial basada en redes neuronales convolucionales pre entrenadas, adaptadas al caso de negocio planteado:

** Interfaz grafica de usuario que permite registro facial de una persona y login facial
** En función de los embeddings de los rostros generados por la Red neuronal, debe permitir la identificación en tiempo real de las personas a traves de un dispositivo de tipo webcam.

Actualmente , estoy realizando una versión 2.0 del prototipo para mejorar la interfaz gráfica , mediante la sustitucion de la libreria Tkinter con la libreria PySide6 y Qt Designer.

# :mechanical_arm:Estado del proyecto
:construction: Proyecto en construcción :construction:



## :hammer:Funcionalidades del proyecto

- `Funcionalidad 1`: registro facia.
- `Funcionalidad 2`: login facial para reconocer a los invitados en base a una base de datos de personas con credenciales de autenticación.
- `Funcionalidad 3`: reconocimiento facial en tiempo real, que identifica a personas de forma positivo (Nombre y apellido) o negativa , renderizando un bounding box en en los rostros detectados en el video de webcam.


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

# :wrench: Tecnologías usadas:

   - **Metodología Scrum:** Trello (https://trello.com/b/USt8dHnW/py-reconocimiento-facial-trello)
   - **Desarrollo:** Git ,  VSCode, OpenCV, face recognition, Tkinter, Numpy, Red Neuronal MTCNN, Pytorch, Pipeline.
   - **Presentación:** Canva (https://www.canva.com/design/DAFZ5KQejhI/0p_9DZry9B3d4tTVH8OMtQ/edit) 


## Autores
![equipo](https://user-images.githubusercontent.com/108665441/217483671-7832066e-e9ff-4156-ab51-f97c6930b749.png)

