# ASCII-ART
With ASCII art generator we can convert any image to pencil art as well as text art using ASCII characters.

# Dependencies

The libraries used for this project are numpy and Computer Vision

# How to Run

Simply paste the image you want to convert in the same folder as the main file or paste the local path of the image inside double quotations in imread and run the code. Both pencil sketch as well as text art will be generated in the same folder as the main file.

# Theory 

First,I imported the libraries required. Next,I converted the colored image to grayscale. Next, the image was resized to appropriate dimensions. The characters to be used to generate the art were then selected. Next pixels were extracted from the resized image and were mapped to the characters we selected earlier. These were then written to a text file.

To generate the pencil sketch,the original grayscaled image was blurred and then inverted. The grayscaled image was then divided by the inverted and blurred image using computer vision and the generated image was then written to a png file.

# What I Learned

Using Computer Vision
Writing more elegant python code
Extracting pixels from an image and mapping data onto it.

# Additional feature/task

Additionally,my project generates a pencil sketch of the image which looks cool :)

# Video Demo


https://user-images.githubusercontent.com/79641239/174442625-90307f43-5fae-48a5-9c89-8cbf778c8793.mp4

