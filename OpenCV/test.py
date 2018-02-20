import cv2
import numpy as np
 
# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture(-1)
 
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
cap_frame=0
 
# Read until video is completed
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
 
    # Display the resulting frame
    cv2.imshow('Frame',frame)
 
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      cap_frame=frame
      break
 
  # Break the loop
  else: 
    break

cv2.imshow('PIC',cap_frame)
#cv2.imwrite('image.jpg',cap_frame)
cv2.waitKey(0)

#reading source image from file
img = cv2.imread('im.jpg')
cv2.imshow('Image',img)
cv2.waitKey(0)

#converting source image to grayscale
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(img)
gray_image = h

#applying a smoothing filter to the grayscale image
blur = cv2.GaussianBlur(gray_image,(3,3),0)
cv2.imshow('Blurred-Image',blur)
cv2.waitKey(0)

#Thresholding the blurred image
#ret,thresh1 = cv2.threshold(blur,220,255,cv2.THRESH_BINARY)
ret,thresh1 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Thresholded-Image', thresh1)
cv2.waitKey(0)

#drawing contours on processed image
contours, hierarchy = cv2.findContours(thresh1.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#finding image dimensions to compute area
height, width, channels = img.shape
print height, width, channels

#finding number of contours
print('len(contours)=',len(contours))

#find the largest contour
largest_contour=0

for i in range(0, len(contours)-1):
 cimg=np.zeros_like(img)
 if((cv2.contourArea(contours[largest_contour])>cv2.contourArea(contours[i])) & (cv2.contourArea(contours[largest_contour])<(height * width * 0.9))):
  largest_contour=largest_contour
 else:
  largest_contour=i
 print('largest contour=',largest_contour)
 cv2.drawContours(cimg, contours, largest_contour, (0,255,0), cv2.cv.CV_FILLED)
 #cv2.fillPoly(img, pts = contours[a], color = (255,255,255))
 #cv2.imshow('Sid-Image', cimg)
 #cv2.waitKey(0)
 
print('largest contour=',largest_contour)
cimg=np.zeros_like(img)
cv2.drawContours(cimg, contours, largest_contour, (0,255,0), cv2.cv.CV_FILLED)
#cv2.fillPoly(img, pts = contours[a], color = (255,255,255))
cv2.imshow('Sid-Image', cimg)
cv2.waitKey(0)
 


a=largest_contour

#this check is performed to eliminate smaller shapes
#that may be contoured due to noise/ lighting
#also includes the point polygon test

x,y,w,h = cv2.boundingRect(contours[a])
 #cv2.rectangle(cimg,(x-10,y-10),(x+w+10,y+h+10),(0,0,255),2)
x=x-10
y=y-10
timg=np.zeros_like(img)
direction=1

x_st=x
x_end=x+w+20
while (y<=y+h+20):
 print(x,x+w+20)
 for i in range (x_st,x_end, direction):
  print('x:', i,'y:',y)
  a = cimg[y,i]
  if(a[1] == 255):
   timg[y,i] = [0,0,255]
   cv2.imshow('Sid-Image-copy', timg)
   cv2.waitKey(1)
  temp=x_st
  x_st=x_end
  x_end=temp
  if(direction==1):
   direction=-1
  else:
   direction=1
 y=y+1
 

 #dist = cv2.pointPolygonTest(contours[a],(34,254),True)
 #print('dist=', dist)

#display contour of shape
cv2.imshow('CONTOURS',img)
cv2.waitKey(0)
 
# When everything done, release the video capture object
cap.release()
 
# Closes all the frames
cv2.destroyAllWindows()
