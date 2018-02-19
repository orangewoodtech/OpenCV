#importing required packages
import numpy as np
import cv2

#reading source image from file
img = cv2.imread('/home/pi/Downloads/1.jpg')
cv2.imshow('Image',img)
cv2.waitKey(0)

#converting source image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#applying a smoothing filter to the grayscale image
blur = cv2.GaussianBlur(gray_image,(3,3),0)
cv2.imshow('Blurred-Image',blur)
cv2.waitKey(0)

#Thresholding the blurred image
ret,thresh1 = cv2.threshold(blur,220,255,cv2.THRESH_BINARY)
cv2.imshow('Thresholded-Image', thresh1)
cv2.waitKey(0)

#drawing contours on processed image
contours, hierarchy = cv2.findContours(thresh1.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#finding image dimensions to compute area
height, width, channels = img.shape
print height, width, channels

#finding number of contours
print('len(contours)=',len(contours))

#locating child contours
print(hierarchy)
a = hierarchy[0,0,2]
print ('a=', a)
b = hierarchy[0,a,0]
print  ('b=', b)

#this check is performed to eliminate smaller shapes
#that may be contoured due to noise/ lighting
#also includes the point polygon test
if (cv2.contourArea(contours[a])>cv2.contourArea(contours[b])):
 cimg=np.zeros_like(img)
 cv2.drawContours(cimg, contours, a, (0,255,0), cv2.cv.CV_FILLED)
 #cv2.fillPoly(img, pts = contours[a], color = (255,255,255))
 cv2.imshow('Sid-Image', cimg)
 cv2.waitKey(0)
 dist = cv2.pointPolygonTest(contours[a],(34,254),True)
 print('dist=', dist)
else:
 cv2.drawContours(img, contours, b, (0,255,0), 5)
 dist = cv2.pointPolygonTest(contours[b],(50,50),True)
 print('dist=', dist)

#display contour of shape
cv2.imshow('CONTOURS',img)
cv2.waitKey(0)


cv2.destroyAllWindows