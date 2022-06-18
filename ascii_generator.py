#Importing required libraries

import cv2
import numpy as np

#Reading the image using computer vision

img = cv2.imread("116.jpg")
im2 = img

#Changing image color scheme

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Extracting height and width from Image


width,height = img.shape
aspect_ratio = height/width

#Resizing image

resized_width = 175
resized_height = aspect_ratio*resized_width 
img = cv2.resize(img,(int(resized_width),int(resized_height)))

#Characters to generate ASCII art


chars = ['@','#','S','?','*','+',';',':',',','.','$',']','[','!','W','&']
pixels = []


for i in range(img.shape[0]):
  for j in range(img.shape[1]):
    pixels.append(img[i][j])

#Generating ASCII art

final_pixels = [chars[pixel//25] for pixel in pixels]
final_pixels =  ''.join(final_pixels)

#Finding number of pixels

pixel_count = len(final_pixels)
ascii_art = [final_pixels[index:index + resized_width] for index in range(0, pixel_count, resized_width)]
ascii_art = "\n".join(ascii_art)

#Writing generated art to text file

with open("final_ascii_art.txt", "w") as f:
 f.write(ascii_art)

#Creating pencil sketch

grey_img = cv2.cvtColor(im2,cv2.COLOR_BGR2GRAY)
inverted_image = cv2.bitwise_not(grey_img)
blurred_image=cv2.GaussianBlur(inverted_image,(81,81),0)
inverted_blur  = cv2.bitwise_not(blurred_image)
pencil_sketch = cv2.divide(grey_img,inverted_blur,scale = 256.00)
cv2.imwrite("pencil_sketch.png",pencil_sketch)