from PIL import Image
from pytesseract import pytesseract

#Define path to tessaract.exe
path_to_tesseract = r'/usr/bin/tesseract'

#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract

#Define path to image
img_cv = cv2.imread(r'./frame293.jpg')

#Extract text from image
img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img_rgb))