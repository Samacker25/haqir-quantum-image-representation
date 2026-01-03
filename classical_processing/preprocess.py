import cv2
import numpy as np

def load_and_resize(uploaded_file, size=(8, 8)):
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, size)
    return img / 255.0