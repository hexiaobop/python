from pytesser import *
image = Image.open('a.jpg')  # Open image object using PIL
print image_to_string(image)     # Run tesseract.exe on image

print image_file_to_string('aa.jpg')
