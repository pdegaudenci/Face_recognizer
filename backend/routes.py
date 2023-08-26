from models.Usuario import Usuario, LoginResponse
from fastapi import APIRouter, UploadFile,File, Depends, Form,Response, status
from pydantic import BaseModel, Json
from service_auth import *
from skimage import io, color
from typing import Annotated
from os import getcwd
from services import existe_usuario, generar_encoder
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse, FileResponse
from facenet_pytorch import MTCNN
from facenet_pytorch import InceptionResnetV1


# Modulo APIRouter permite crear sistemas de rutas y endpoints para solicitudes de entradas
api_router = APIRouter()

## TODO refactorizar codigo : extraer codigo duplicado en metodos de services
## TODO Gestion de excepciones y codigos de estado HTTP
@api_router.post("/registro/{user}")
async def registrar_usuario(user:str,imagen: UploadFile = None):
    with open(user+imagen.filename,"wb") as my_img:
        contenido = await imagen.read()
        my_img.write(contenido)
        my_img.close()
        ## TODO Verificar si usuario existe 
        return True

@api_router.post("/login/{user}",response_model=LoginResponse)
async def login_usuario(user:str,response: Response,imagen: UploadFile = None):
    with open("temp_"+imagen.filename,"wb") as my_img:
        contenido = await imagen.read()
        my_img.write(contenido)
        my_img.close()
    existe, similitud= existe_usuario("temp_"+imagen.filename,user)
    if  similitud!= None :
            response.status_code = status.HTTP_202_ACCEPTED
    else:
        response.status_code = status.HTTP_404_NOT_FOUND 
    json_compatible_item_data = jsonable_encoder({"usuario":user,"similitud":similitud,"existe":existe})
    return JSONResponse(content=json_compatible_item_data)

## TODO : Verificar si encoder existe y enviar data adicional
@api_router.get("/encoder")
async def obtener_encoder(response: Response):
    size, encoder_name_file= generar_encoder()
    response.status_code = status.HTTP_200_OK
    #json_compatible_item_data = jsonable_encoder({"encoder":encoder,"size":str(size)+" bytes"})
    dirname = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__))))
    return FileResponse(f"{dirname}/{encoder_name_file}")
