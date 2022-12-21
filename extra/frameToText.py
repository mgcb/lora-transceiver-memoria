import cv2
from pytesseract import pytesseract
import os

#Define path to tessaract.exe
path_to_tesseract = r'/usr/bin/tesseract'

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

#Define path to image
folder = r'./'

for root, dirs, file_names in os.walk(folder):
    for file_name in file_names:
        cv2.imread(folder + file_name)

        img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
        print(pytesseract.image_to_string(img_rgb))

