from models.Usuario import Usuario
from fastapi import FastAPI, UploadFile,File, Depends, Form
from pydantic import BaseModel, Json
from service_auth import *
from skimage import io, color
from typing import Annotated
from os import getcwd
from services import existe_usuario

app = FastAPI()


@app.post("/registro/{user}")
async def registrar_usuario(imagen: UploadFile = None):
    with open(getcwd()+imagen.filename,"wb") as my_img:
        contenido = await imagen.read()
        my_img.write(contenido)
        my_img.close()
        return True

@app.post("/login/{user}")
async def login_usuario(user:str,imagen: UploadFile = None):
    with open(getcwd()+"temp_"+imagen.filename,"wb") as my_img:
        contenido = await imagen.read()
        my_img.write(contenido)
        existe, similitud= existe_usuario(my_img,user)
        if  existe!= None :
            existe = True
        my_img.close()
        return {"existe":existe, "similitud":similitud}
    
def encoder():
    return None
