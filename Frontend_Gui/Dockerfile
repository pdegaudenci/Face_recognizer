FROM python:3.9 
# Or any preferred Python version.

RUN mkdir /face_recognizer-GUI

# Se crea un volume con el contenido de la aplicacion
VOLUME /face_recognizer-GUI

COPY requeriments.txt /
RUN apt-get update && apt-get install libgl1
RUN  pip install  -r  /requeriments.txt


# Se crea un usuario para arrancar uWSGI
RUN useradd -ms /bin/bash admin
# Cambia a usuario admin para ejecucion de procesos
USER admin
 
# Se copia el contenido de la aplicacion
COPY . /face_recognizer-GUI
 
# Se establece el directorio de trabajo
WORKDIR /face_recognizer-GUI
 
# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8080

ENTRYPOINT [ "python3", "/face_recognizer-GUI/interfaz.py" ]


 