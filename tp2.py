import os
from PIL import Image
import numpy as np

def cargar_imagen(ruta):
    img = Image.open(ruta).convert("RGB")
    return np.array(img, dtype=np.uint8)