import cv2
from pytesseract import pytesseract
import os

#Define path to tessaract.exe
path_to_tesseract = r'/usr/bin/tesseract'

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

#Define path to image
folder = r'./Escenas'
f = open("./results.txt", "w")


for root, dirs, file_names in os.walk(folder):
    i = 0
    for file_name in file_names:
        img_cv = Image.open(folder + file_name)

        f.write(pytesseract.image_to_string(img_cv))
        print("Writing file number " + str(i))
        i+=1

