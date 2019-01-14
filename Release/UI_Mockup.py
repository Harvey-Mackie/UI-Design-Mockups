import numpy as np
import cv2
import random

def CreateMockup(img,colour,size,device,rotation):
    image = cv2.imread(img, cv2.IMREAD_UNCHANGED)
    #Image Height and Width
    if(device=="iPhone"):
        if(rotation == "Landscape"):
            width = 334
            height = 659
            PixelWidthStart =  76
            PixelHeightStart = 24
            if(colour=="White"):
                PixelWidthEnd =  582
                PixelHeightEnd = 310
                MockupImageHeight =  286
                MockupImageWidth = 506
            if(colour=="Black"):
                PixelWidthEnd =  584
                PixelHeightStart = 22
                PixelHeightEnd = 313
                MockupImageHeight = 291
                MockupImageWidth = 508           
            colour = colour + "-" + rotation
        else:
            width = 660
            height = 330
            PixelWidthStart = 24
            PixelHeightStart = 78
            if(colour=="White"):
                PixelHeightEnd = 582
                PixelWidthEnd = 307
                MockupImageHeight = 504
                MockupImageWidth = 283
            if(colour=="Black"):
                PixelWidthEnd = 300
                PixelHeightEnd = 570
                MockupImageHeight = 492
                MockupImageWidth = 276
            

    elif(device=="iPad"):
        if(rotation == "Landscape"):
            width = 334
            height = 659
            if(colour=="White"):
                PixelWidthStart =  62
                PixelWidthEnd =  597
                PixelHeightStart = 35
                PixelHeightEnd = 299
                MockupImageHeight =  264
                MockupImageWidth = 535
            elif(colour=="Black"):
                PixelWidthStart =  60
                PixelWidthEnd =  599
                PixelHeightStart = 33
                PixelHeightEnd = 301
                MockupImageHeight =  268
                MockupImageWidth = 539
            colour = colour + "-" + rotation
        else:    
            width = 546
            height = 425
            if(colour=="White"):
                PixelWidthStart = 45
                PixelWidthEnd = 380
                PixelHeightStart = 50
                PixelHeightEnd = 490
                MockupImageHeight = 440
                MockupImageWidth =  335
            if(colour=="Black"):
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
        if(device=="Mac"):
            ImageProperties[5] += -1
        elif(device=="iPad" and rotation != "Landscape"):
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
    #device_img[ImageProperties[4]:ImageProperties[5], ImageProperties[2]:ImageProperties[3]] = image
    try:
        device_img[ImageProperties[4]:ImageProperties[5], ImageProperties[2]:ImageProperties[3]] = image
    except ValueError:
        print("Required Step - Add Alpha channel")
        b, g, r = cv2.split(image)
        alpha_channel = np.ones(b.shape, dtype=b.dtype) * 255
        image = cv2.merge((b, g, r, alpha_channel))
        device_img[ImageProperties[4]:ImageProperties[5], ImageProperties[2]:ImageProperties[3]] = image 
        
    cv2.imshow("Device", device_img)

    cv2.imwrite("Exports/"+size+device+"Mockup"+str(random.randint(1,21)*5)+".png",device_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#Alter 'img' and 'deviceColour' to create your own Mockup
img = "Mockup/Cruyff-Landscape.PNG"
deviceColour = "White" #Only White Images are imported currentley
size = "White" #Only applies for Monitor
device = "iPhone"
rotation = "Landscapae"

CreateMockup(img,deviceColour,size,device,rotation)

