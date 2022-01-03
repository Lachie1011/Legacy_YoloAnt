# a utilities library to assist yoloAnt.py

# import python libraries
import os
import cv2
import ctypes
import random
import numpy as np
from enum import Enum
from os.path import exists

# Screen size
#user32 = ctypes.windll.user32
#screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

# Enum to contain colour class relationships
class Classes(Enum):
    blue = 0
    yellow = 1
    orange = 2

# A function to load images from a folder       
def loadImagesFromFolder(folder):

    images = []

    for filename in os.listdir(folder):

        img = cv2.imread(os.path.join(folder, filename))

        if img is not None:

            images.append(img)

    return images

# A function to provide inference over an image and return respective labels
def inferAndAnnotate(model, image, cntr):

    # inference
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # converting to RGB for inferencing stage (v5 requires RGB)
    results = model(image) # inferencing over image

    # labelling/annotating 
    color = (0,0,0) # color value (RGB)
    Class = '' # class value
    cones = list() # a list of cone locations

    h, w, _ = image.shape # getting height and width of image

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)# converting image back to BGR (cv2 likes BGR because cv2 is bad)

    # iterating over detected cones and assigning class and color
    for cone in results.xyxy[0]:

        if int(cone[5]) == Classes.blue.value:
            color = (255, 0, 0)
            Class = 'blue'

        if int(cone[5]) == Classes.yellow.value:
            color = (0, 255, 255)
            Class = 'yellow'

        if int(cone[5]) == Classes.orange.value:
            color = (0, 165, 255)
            Class = 'orange'

        image = cv2.rectangle(image, (int(cone[0]), int(cone[1])), (int(cone[2]), int(cone[3])), color, 2) # drawing rectangle over image

        # getting height and width of cone
        width = int(cone[2]) - int(cone[0])
        height = int(cone[3]) - int(cone[1])
        
        # appending to cones list
        cones.append([Class, width / w, height / h, (int(cone[0]) + width/2) / w, (int(cone[1]) + height/2) / h])

    # displaying image
    window = "Images Annotated: " + str(cntr)
    cv2.namedWindow(window)
    # cv2.moveWindow(window, 40, 30)

    #if h > screensize[0] or w > screensize[1]:
    #    print("yes")

    cv2.imshow(window, image)

    while(True):

        # get user feedback from image/ detection
        key = cv2.waitKey(33)

        # key 'o' image is accepted
        if key == ord('o'):

            cv2.destroyAllWindows()
            return cones, 1

        # key 'p' image is rejected
        elif key == ord('p'):

            cv2.destroyAllWindows()
            return cones, 2

         # key 'q' quit the program
        elif key == ord('q'):

            cv2.destroyAllWindows()
            return cones, -1






