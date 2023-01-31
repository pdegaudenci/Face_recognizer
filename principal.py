from detector_MTCNN import crear_diccionario_referencias,pipeline_deteccion_webcam

from PIL import Image
import cv2
import matplotlib.pyplot as plt
import torch
from facenet_pytorch import MTCNN
import numpy as np
import cv2
import numpy as np
import os
import imutils
from tkinter import *
from PIL import Image
from PIL import ImageTk
from imutils.video import VideoStream
import time
import numpy as np
import cv2
import matplotlib.pyplot as plt
import torch
import warnings
import typing
import logging
import os
import platform
import glob
import PIL
import facenet_pytorch
from typing import Union, Dict
from PIL import Image
from facenet_pytorch import MTCNN
from facenet_pytorch import InceptionResnetV1
from urllib.request import urlretrieve
from tqdm import tqdm 
from scipy.spatial.distance import euclidean
from scipy.spatial.distance import cosine

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
print(F'Running on device: {device}')

dict_referencias = crear_diccionario_referencias(
                    folder_path    = './imagenes_raw',
                    min_face_size  = 40,
                    min_confidence = 0.9,
                    device         = device,
                    verbose        = True
                  )
pipeline_deteccion_webcam(
    dic_referencia        = dict_referencias,
   threshold_similaridad = 0.4, )