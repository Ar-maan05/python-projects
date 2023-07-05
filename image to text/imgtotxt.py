from PIL import Image
import pytesseract

image = 'C:/Users/armaa/Downloads/504f9d64-21d1-4d4e-bff1-bbf13014b405.jpeg'
text = pytesseract.image_to_string(Image.open(image), lang="eng")
print(text)
