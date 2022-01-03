# Importing some libraries:
import os
import cv2
import yaml
import torch
import shutil
import argparse
from enum import Enum
from os.path import exists
from yoloAntUtils import *

# Image counter
image_count = 1

# Image Folder Path
train_images_folder = "../data/images/train/"
val_images_folder = "../data/images/val/"
test_images_folder = "../data/images/test/"

# Label Folder Path
train_labels_folder = "../data/labels/train/"
val_labels_folder = "../data/labels/val/"
test_labels_folder = "../data/labels/test/"

# Deleting (clearing directories) and then recreating them
shutil.rmtree(train_images_folder)
shutil.rmtree(val_images_folder)
shutil.rmtree(test_images_folder)

shutil.rmtree(train_labels_folder)
shutil.rmtree(val_labels_folder)
shutil.rmtree(test_labels_folder)

os.makedirs(train_images_folder)
os.makedirs(val_images_folder)
os.makedirs(test_images_folder)

os.makedirs(train_labels_folder)
os.makedirs(val_labels_folder)
os.makedirs(test_labels_folder)

# Constructing cmd line arguments
ap = argparse.ArgumentParser()

ap.add_argument("-i", "--images", required = True,
                help="Path to the folder containing the images to be annotated ")

args = vars(ap.parse_args())

# Reading in image folder path 
rawImageFolder = args["images"]

# Reading in configuration  
with open(r'../data/config.yaml') as file:

    config = yaml.load(file, Loader=yaml.FullLoader)

    trainR = config['train']
    validationR = config['validation']
    testR = config['test']
    weights = config['weights']
    conf = config['conf']
    numberOfAnnotations =  config['numberOfAnnotations']
    classesToDetect = config['classes']

# Reading in the storing in the images:
imageCollection = loadImagesFromFolder(rawImageFolder)

imageCollectionResult = [] # stores the resulting images from the annotation stage below

cntr = 0 # counter 

# initialising the model with confidence threshold
model = torch.hub.load('ultralytics/yolov5', 'custom', path = weights)
model.conf = conf

# Performing image thresholding over the collection
for image in imageCollection:

    # get cones from image as well as acceptance score
    cones, acceptance = inferAndAnnotate(model, image, cntr)

    # if acceptance is '1' add image to collection
    if acceptance == 1:
        
        imageCollectionResult.append([image, cones])
        cntr = cntr + 1
        
        # if set number of annotations - check if we have exceeded this number
        if numberOfAnnotations != -1:

            if cntr == numberOfAnnotations:
                break
    if acceptance == -1:
        break

for image in imageCollectionResult:

    if image_count <= len(imageCollectionResult) * trainR:

        cv2.imwrite(train_images_folder + str(image_count) + '.jpg', image[0])
        
        # Clear the file it is exists
        open(train_labels_folder + str(image_count) + ".txt", 'w').close()

        file = open(train_labels_folder + str(image_count) + ".txt", "w")

        for cone in image[1]:
            if cone[0] == 'blue':
                file.write(str(Classes.blue.value) + ' ' + str(cone[3]) + ' ' + str(cone[4]) + ' ' + str(cone[1]) + ' ' + str(cone[2]) + '\n')

            if cone[0] == 'yellow':
                file.write(str(Classes.yellow.value) + ' ' + str(cone[3]) + ' ' + str(cone[4]) + ' ' + str(cone[1]) + ' ' + str(cone[2]) + '\n')

            if cone[0] == 'orange':
                file.write(str(Classes.orange.value) + ' ' + str(cone[3]) + ' ' + str(cone[4]) + ' ' + str(cone[1]) + ' ' + str(cone[2]) + '\n')

        file.close()

    elif image_count <= (len(imageCollectionResult) - (len(imageCollectionResult) * testR)):
        cv2.imwrite(val_images_folder + str(image_count) + '.jpg', image[0])

        # Clear the file it is exists
        open(val_labels_folder + str(image_count) + ".txt", 'w').close()

        file = open(val_labels_folder + str(image_count) + ".txt", "w")

        for cone in image[1]:
            if cone[0] == 'blue':
                file.write(
                    str(Classes.blue.value) + ' ' + str(cone[3]) + ' ' + str(cone[4]) + ' ' + str(cone[1]) + ' ' + str(
                        cone[2]) + '\n')

            if cone[0] == 'yellow':
                file.write(str(Classes.yellow.value) + ' ' + str(cone[3]) + ' ' + str(cone[4]) + ' ' + str(
                    cone[1]) + ' ' + str(cone[2]) + '\n')

            if cone[0] == 'orange':
                file.write(str(Classes.orange.value) + ' ' + str(cone[3]) + ' ' + str(cone[4]) + ' ' + str(
                    cone[1]) + ' ' + str(cone[2]) + '\n')

        file.close()

    elif image_count <= len(imageCollectionResult):
        cv2.imwrite(test_images_folder + str(image_count) + '.jpg', image[0])

        # Clear the file it is exists
        open(test_labels_folder + str(image_count) + ".txt", 'w').close()

        file = open(test_labels_folder + str(image_count) + ".txt", "w")

        for cone in image[1]:
            if cone[0] == 'blue':
                file.write(
                    str(Classes.blue.value) + ' ' + str(cone[3]) + ' ' + str(cone[4]) + ' ' + str(cone[1]) + ' ' + str(
                        cone[2]) + '\n')

            if cone[0] == 'yellow':
                file.write(str(Classes.yellow.value) + ' ' + str(cone[3]) + ' ' + str(cone[4]) + ' ' + str(
                    cone[1]) + ' ' + str(cone[2]) + '\n')

            if cone[0] == 'orange':
                file.write(str(Classes.orange.value) + ' ' + str(cone[3]) + ' ' + str(cone[4]) + ' ' + str(
                    cone[1]) + ' ' + str(cone[2]) + '\n')

        file.close()

    image_count = image_count + 1

print('Images and Labels Successfully outputted')



