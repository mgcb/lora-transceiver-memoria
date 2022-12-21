import cv2
from pytesseract import pytesseract
import os

#Define path to tessaract.exe
path_to_tesseract = r'/usr/bin/tesseract'

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

#Define path to image
folder = r'./'
f = open("./results", "w")


for root, dirs, file_names in os.walk(folder):
    for file_name in file_names:
        i = 0
        img_cv = cv2.imread(folder + file_name)

        img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
        f.write(pytesseract.image_to_string(img_rgb))
        print("Writing file number " + str(i))
        i+=1

