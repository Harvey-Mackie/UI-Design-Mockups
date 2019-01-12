import numpy as np
import cv2
import random

def CreateMockup(img,colour,size,device):
    image = cv2.imread(img, cv2.IMREAD_UNCHANGED)
    #Image Height and Width
    width = 900
    height = 900
    if(device=="iPhone"):
        width = 660
        height = 330
        PixelWidthStart = 24
        PixelWidthEnd = 307
        PixelHeightStart = 78
        PixelHeightEnd = 582
        MockupImageHeight = 504
        MockupImageWidth = 283
    elif(device=="iPad"):
        width = 546
        height = 425
        PixelWidthStart = 45
        PixelWidthEnd = 380
        PixelHeightStart = 50
        PixelHeightEnd = 490
        MockupImageHeight = 440
        MockupImageWidth =  335
    elif(device=="Mac"):
        width =  290 
        height = 491  
        PixelWidthStart = 62
        PixelWidthEnd = 428
        PixelHeightStart = 25
        PixelHeightEnd = 254
        MockupImageHeight = 229 
        MockupImageWidth =  366
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
            ImageProperties[7] += 1
    elif(size=="x-large"):
        for i in range(0,len(ImageProperties)):
            ImageProperties[i] = ImageProperties[i] * 2
            ImageProperties[i] = int(ImageProperties[i])
 
    image = cv2.resize(image,(ImageProperties[7],ImageProperties[6]))

    #Background Image
    imageLink = "Devices/"+device+"-"+colour+".png"

    device_img = cv2.imread(imageLink,  cv2.IMREAD_UNCHANGED)
    device_img= cv2.resize(device_img,(ImageProperties[1],ImageProperties[0]))
    try:
        device_img[ImageProperties[4]:ImageProperties[5], ImageProperties[2]:ImageProperties[3]] = image
    except ValueError:
        print("Required Step - Add Alpha channel")
        b, g, r = cv2.split(image)
        alpha_channel = np.ones(b.shape, dtype=b.dtype) * 255
        print(alpha_channel)#creating a dummy alpha channel image.
        image = cv2.merge((b, g, r, alpha_channel))
        device_img[ImageProperties[4]:ImageProperties[5], ImageProperties[2]:ImageProperties[3]] = image
        
        
    cv2.imshow("Device", device_img)

    cv2.imwrite("Exports/"+size+device+"Mockup"+str(random.randint(1,21)*5)+".png",device_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Alter 'img' and 'deviceColour' to create your own Mockup
img = "Mockup/Cruyff-Mac.PNG"
deviceColour = "White" #Only White Images are imported currentley
size = "small" #Only applies for Monitor
device = "iPhone"

#CreateMockup("Mockup/Cruyff.PNG",deviceColour,size,device)
#CreateMockup(img,deviceColour,size,"Mac")
#CreateMockup("Mockup/Cruyff-Monitor.PNG",deviceColour,size,"Monitor")
#CreateMockup(img,deviceColour,size,"Mac")

#iPadMockup("Mockup/Cruyff-Mac.PNG", deviceColour,"small")
