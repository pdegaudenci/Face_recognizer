from fastapi import FastAPI
from routes import api_router
from services import crear_diccionario_referencias, guardar_archivo
from os import getcwd, path
import torch

app = FastAPI(
    title= "Face recognizer API Rest",
    description= "",
    openapi_tags=[{
    "name": "Face recognizer API Rest",
    "description":""
    }])

# Creo diccionario de embeddings sino existe 
if not path.exists('Data/embeddings.json'):
    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
    print(F'Running on device: {device}')

    # Obtengo diccionario de referencia de embeddings de las imagenes almacenadas en carpeta imagenes
    dict_referencias = crear_diccionario_referencias(
                    folder_path    =getcwd()+"/Data/imagenes",
                    min_face_size  = 40,
                    min_confidence = 0.9,
                    device         = device,
                    verbose        = True
                  )
    guardar_archivo(dict_referencias,"/Data/embeddings","json")
# CREO SISTEMA DE ENRUTADO DE LA API
# Agrego a la aplicacion enrutamiento 
app.include_router(api_router)
