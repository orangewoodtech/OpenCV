# OpenCV
This repository contains code for OpenCV 3.1.0 on Python 2.7.x
It is used for developing the painting robotic arm

Description of Code files in repo - 
  imtest.py : Used for finding contours of the shape - converts image to grayscale, applies threshold filter, detects contours, 
  eliminates outermost contour of image by determining and comparing area
  
  video_stream_camera.py : simple video streaming example via webcam.
Note: for some reason the pi connects webcam to -1, if this does not work try 0 or 1 also.
  draw_filled_contour.py : used for isolating the shape from the rest of the image and creating a filled contour on the shape. The effect is very similar to creating a mask and applying it on the image.
  
