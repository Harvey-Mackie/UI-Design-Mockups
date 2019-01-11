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

def CreateMockup(img,colour,size,device):
    image = cv2.imread(img, cv2.IMREAD_UNCHANGED)
    #Image Height and Width
    width = 900
    height = 900
    if(device=="iPhone"):
        PixelWidthStart = 270
        PixelWidthEnd = 630
        PixelHeightStart = 143
        PixelHeightEnd = 757
        MockupImageHeight = 614
        MockupImageWidth = 360
    elif(device=="iPad"):
        PixelWidthStart = 245
        PixelWidthEnd = 650
        PixelHeightStart = 175
        PixelHeightEnd = 710
        MockupImageHeight = 535
        MockupImageWidth = 405
    elif(device=="Mac"):
        PixelWidthStart = 193
        PixelWidthEnd = 707
        PixelHeightStart = 243
        PixelHeightEnd = 670
        MockupImageHeight = 427
        MockupImageWidth = 514
    elif(device=="Monitor"):
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
        if(device=="Mac"):
            ImageProperties[5] += -1
        elif(device=="iPad"):
            ImageProperties[6] += 1
            ImageProperties[7] += 1
 
    image = cv2.resize(image,(ImageProperties[7],ImageProperties[6]))

    #Background Image
    imageLink = "Devices/"+device+"-"+colour+".png"

    device_img = cv2.imread(imageLink,  cv2.IMREAD_UNCHANGED)
    device_img= cv2.resize(device_img,(ImageProperties[1],ImageProperties[0]))
    try:
        device_img[ImageProperties[4]:ImageProperties[5], ImageProperties[2]:ImageProperties[3]] = image
    except ValueError:
        print("Fail - Add Alpha channel")
        b, g, r = cv2.split(image)
        alpha_channel = np.ones(b.shape, dtype=b.dtype) * 50 #creating a dummy alpha channel image.
        image = cv2.merge((b, g, r, alpha_channel))
        device_img[ImageProperties[4]:ImageProperties[5], ImageProperties[2]:ImageProperties[3]] = image
        
    cv2.imshow("Device", device_img)

    cv2.imwrite("Exports/"+size+device+"Mockup"+str(random.randint(1,21)*5)+".png",device_img)
    iPadMockup
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#Create iPhone Mockup function
def iPhoneMockup(img,colour,size):
    
    image = cv2.imread(img, cv2.IMREAD_UNCHANGED)
    
    width = 900
    height = 900
    PixelWidthStart = 270
    PixelWidthEnd = 630
    PixelHeightStart = 143
    PixelHeightEnd = 757
    MockupImageHeight = 614
    MockupImageWidth = 360
    ImageProperties = [width, height, PixelWidthStart, PixelWidthEnd, PixelHeightStart,PixelHeightEnd,MockupImageHeight, MockupImageWidth]
    
    if(size=="small"):
        for i in range(0,len(ImageProperties)):
            ImageProperties[i] = ImageProperties[i] / 2
            ImageProperties[i] = int(ImageProperties[i])
    
    image = cv2.resize(image,(ImageProperties[7],ImageProperties[6]))
    device = "iPhone"
    #Background Image
    imageLink = "Devices/"+device+"-"+colour+".png"

    device_img = cv2.imread(imageLink,  cv2.IMREAD_UNCHANGED)
    device_img= cv2.resize(device_img,(ImageProperties[1],ImageProperties[0]))
    
    device_img[ImageProperties[4]:ImageProperties[5], ImageProperties[2]:ImageProperties[3]] = image
    
    cv2.imshow("Device", device_img)

    cv2.imwrite("Exports/iPhoneMockup"+str(random.randint(1,21)*5)+".png",device_img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def iPadMockup(img,colour,size):
    image = cv2.imread(img, cv2.IMREAD_UNCHANGED)
    
    width = 900
    height = 900
    PixelWidthStart = 245
    PixelWidthEnd = 650
    PixelHeightStart = 175
    PixelHeightEnd = 710
    MockupImageHeight = 535
    MockupImageWidth = 405
    ImageProperties = [width, height, PixelWidthStart, PixelWidthEnd, PixelHeightStart,PixelHeightEnd,MockupImageHeight, MockupImageWidth]
    
    if(size=="small"):
        for i in range(0,len(ImageProperties)):
            ImageProperties[i] = ImageProperties[i] / 2
            ImageProperties[i] = int(ImageProperties[i])
        ImageProperties[6] += 1
        ImageProperties[7] += 1
    
    
    image = cv2.resize(image,(ImageProperties[7],ImageProperties[6]))
    device = "iPad"
    #Background Image
    imageLink = "Devices/"+device+"-"+colour+".png"

    device_img = cv2.imread(imageLink,  cv2.IMREAD_UNCHANGED)
    device_img= cv2.resize(device_img,(ImageProperties[1],ImageProperties[0]))

    device_img[ImageProperties[4]:ImageProperties[5],ImageProperties[2]:ImageProperties[3]] = image
    cv2.imshow("Device", device_img)

    cv2.imwrite("Exports/iPadMockup"+str(random.randint(1,21)*5)+".png",device_img)
    iPadMockup
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def macMockup(img,colour,size):
    image = cv2.imread(img, cv2.IMREAD_UNCHANGED)
    
    width = 900
    height = 900
    PixelWidthStart = 193
    PixelWidthEnd = 707
    PixelHeightStart = 243
    PixelHeightEnd = 670
    MockupImageHeight = 427
    MockupImageWidth = 514
    ImageProperties = [width, height, PixelWidthStart, PixelWidthEnd, PixelHeightStart,PixelHeightEnd,MockupImageHeight, MockupImageWidth]
    
    if(size=="small"):
        for i in range(0,len(ImageProperties)):
            ImageProperties[i] = ImageProperties[i] / 2
            ImageProperties[i] = int(ImageProperties[i])
        ImageProperties[5] += -1    
    
    image = cv2.resize(image,(ImageProperties[7],ImageProperties[6]))
    device = "Mac"
    #Background Image
    imageLink = "Devices/"+device+"-"+colour+".png"

    device_img = cv2.imread(imageLink,  cv2.IMREAD_UNCHANGED)
    device_img= cv2.resize(device_img,(ImageProperties[1],ImageProperties[0]))
    #print (image)
    device_img[ImageProperties[4]:ImageProperties[5], ImageProperties[2]:ImageProperties[3]] = image
    cv2.imshow("Device", device_img)

    cv2.imwrite("Exports/"+size+device+"Mockup"+str(random.randint(1,21)*5)+".png",device_img)
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
img = "Mockup/Cruyff-Mac.PNG"
deviceColour = "White" #Only White Images are imported currentley
size = "smalla" #Only applies for Monitor
device = "iPhone"

#CreateMockup("Mockup/Cruyff.PNG",deviceColour,size,device)
#CreateMockup("Mockup/Cruyff-iPad.PNG",deviceColour,size,"iPad")
#CreateMockup("Mockup/Cruyff-Monitor.PNG",deviceColour,size,"Monitor")
#CreateMockup(img,deviceColour,size,"Mac")

#iPadMockup("Mockup/Cruyff-Mac.PNG", deviceColour,"small")
