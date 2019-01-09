import numpy as np
import cv2
import random
import imutils

#Users Image

#def MakeWhiteBlack(device_img):
def RotateDevice(img,angle):
    img = cv2.imread(img)
    (h, w) = img.shape[:2] #get height and width
    # calculate the center of the image
    center = (w / 2, h / 2)
    scale = 1.8
    #erform the counter clockwise rotation holding at the center
    # 90 degrees
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated90  = cv2.warpAffine(img, M, (h, w))
     
    cv2.imshow('Image rotated by 90 degrees',rotated90)
    cv2.waitKey(0) # waits until a key is pressed
    cv2.destroyAllWindows() # destroys the window showing image


#Create iPhone Mockup function
def iPhoneMockup(img,colour):
    
    image = cv2.imread(img, cv2.IMREAD_UNCHANGED)
    
    image = cv2.resize(image,(360,614))
    device = "iPhone"
    #Background Image
    imageLink = "Devices/"+device+"-"+colour+".png"

    device_img = cv2.imread(imageLink,  cv2.IMREAD_UNCHANGED)
    device_img= cv2.resize(device_img,(900,900))
    
    device_img[143:757, 270:630] = image
    
    cv2.imshow("Device", device_img)

    cv2.imwrite("Exports/iPhoneMockup"+str(random.randint(1,21)*5)+".png",device_img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def iPadMockup(img,colour):
    image = cv2.imread(img, cv2.IMREAD_UNCHANGED)
    
    image = cv2.resize(image,(405,535))
    device = "iPad"
    #Background Image
    imageLink = "Devices/"+device+"-"+colour+".png"

    device_img = cv2.imread(imageLink,  cv2.IMREAD_UNCHANGED)
    device_img= cv2.resize(device_img,(900,900))
    #print (image)
    device_img[175:710, 245:650] = image
    cv2.imshow("Device", device_img)

    cv2.imwrite("Exports/iPadMockup"+str(random.randint(1,21)*5)+".png",device_img)
    iPadMockup
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def macMockup(img,colour):
    image = cv2.imread(img, cv2.IMREAD_UNCHANGED)
    
    image = cv2.resize(image,(514,427))
    device = "Mac"
    #Background Image
    imageLink = "Devices/"+device+"-"+colour+".png"

    device_img = cv2.imread(imageLink,  cv2.IMREAD_UNCHANGED)
    device_img= cv2.resize(device_img,(900,900))
    #print (image)
    device_img[243:670, 193:707] = image
    cv2.imshow("Device", device_img)

    cv2.imwrite("Exports/"+device+"Mockup"+str(random.randint(1,21)*5)+".png",device_img)
    iPadMockup
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def monitorMockup(img,colour,size):
    image = cv2.imread(img, cv2.IMREAD_UNCHANGED)
    
    #Image Properties - Declare Variables
    width = 900
    height = 900
    PixelWidthStart=35
    PixelWidthEnd=863
    PixelHeightStart = 40
    PixelHeightEnd = 625
    MockupImageHeight  =  585
    MockupImageWidth  =  828
    ImageProperties = [width, height, PixelWidthStart, PixelWidthEnd, PixelHeightStart,PixelHeightEnd,MockupImageHeight, MockupImageWidth] 
    if(size=="small"):
        for i in range(0,len(ImageProperties)):
            ImageProperties[i] = ImageProperties[i] / 2
            ImageProperties[i] = int(ImageProperties[i])
    
    image = cv2.resize(image,(ImageProperties[7],ImageProperties[6]))
    device = "Monitor"
    #Background Image
    imageLink = "Devices/"+device+"-"+colour+".png"

    device_img = cv2.imread(imageLink,  cv2.IMREAD_UNCHANGED)
    device_img= cv2.resize(device_img,(ImageProperties[1],ImageProperties[0]))

    device_img[ImageProperties[4]:ImageProperties[5], ImageProperties[2]:ImageProperties[3]] = image
    cv2.imshow("Device", device_img)

    cv2.imwrite("Exports/"+size+device+"Mockup"+str(random.randint(1,21)*5)+".png",device_img)
    iPadMockup
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Alter 'img' and 'deviceColour' to create your own Mockup
img = "Mockup/Cruyff-Monitor.PNG"
deviceColour = "White" #Only White Images are imported currentley
size = "small" #Only applies for Monitor 
iPhoneMockup("Mockup/Cruyff.PNG",deviceColour)
iPadMockup("Mockup/Cruyff-iPad.PNG",deviceColour)
macMockup(img,deviceColour)
monitorMockup(img,deviceColour,size)
monitorMockup("Mockup/Cruyff-Monitor-large.PNG",deviceColour,"large")

