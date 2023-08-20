
from pydantic import BaseModel
import pydantic_numpy.typing as pnd
from fastapi import FastAPI, UploadFile,File, Form

class Usuario(BaseModel):
   usuario: str 
   
