FROM python:3.9 
# Or any preferred Python version.

RUN mkdir /face_recognizer-backend
WORKDIR /face_recognizer-backend

RUN mkdir /conf
VOLUME /face_recognizer 
COPY requeriments.txt /
RUN pip install uvicorn && pip install  -r  /requeriments.txt

 
# Se crea un usuario para arrancar uWSGI
RUN useradd -ms /bin/bash admin
# Cambia a usuario admin para ejecucion de procesos
USER admin
 
# Se copia el contenido de la aplicacion
COPY ./services /face_recognizer-backend
 
# Se establece el directorio de trabajo
WORKDIR /face_recognizer
 
# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Se crea un volume con el contenido de la aplicacion
VOLUME /face_recognizer
 
CMD [“python”, “./main.py”] 
