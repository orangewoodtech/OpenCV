import numpy as np
import cv2


img = cv2.imread('/home/pi/Downloads/1.jpg')
cv2.imshow('Image',img)
cv2.waitKey(0)

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray_image,(3,3),0)
cv2.imshow('Blurred-Image',blur)
cv2.waitKey(0)

ret,thresh1 = cv2.threshold(blur,220,255,cv2.THRESH_BINARY)
cv2.imshow('Thresholded-Image', thresh1)
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(thresh1.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


height, width, channels = img.shape
print height, width, channels

print('len(contours)=',len(contours))

print(hierarchy)
a = hierarchy[0,0,2]
print ('a=', a)
b = hierarchy[0,a,0]
print  ('b=', b)

if (cv2.contourArea(contours[a])>cv2.contourArea(contours[b])):

 cv2.drawContours(img, contours, a, (0,255,0), 5)

else:
 cv2.drawContours(img, contours, b, (0,255,0), 5)
 
cv2.imshow('CONTOURS',img)
 
cv2.waitKey(0)



cv2.destroyAllWindows