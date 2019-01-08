import numpy as np
import cv2
import random

#Users Image

#def MakeWhiteBlack(device_img):
    

#Create iPhone Mockup function
def iPhoneMockup(img,colour):
    
    image = cv2.imread(img)
    image = cv2.resize(image,(360,614))
    
    #Background Image
    imageLink = "Devices/iPhone-"+colour+".png"
    device_img = cv2.imread(imageLink,cv2.IMREAD_COLOR)
    device_img= cv2.resize(device_img,(900,900))
    #print (image)
    
    device_img[143:757, 270:630] = image
    
    cv2.imshow("Device", device_img)
    
    
    b =  device_img[:,:,0]
    g =  device_img[:,:,1]
    r =  device_img[:,:,2]
    
    rgba = cv2.merge((b,g,r,g))
    cv2.imwrite("Exports/iPhoneMockup"+str(random.randint(1,21)*5)+".png",device_img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Alter 'img' and 'deviceColour' to create your own Mockup
img = "Mockup/Cruyff.PNG"
deviceColour = "White"
iPhoneMockup(img,deviceColour)

#MakeWhiteBlack("iPhone-White.png")