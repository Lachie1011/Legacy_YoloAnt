import sys
import os
import cv2
import glob
from PIL import Image

cntr = 0

for img in glob.glob("C:/Users/lachl/OneDrive/Desktop/l4/*.jpg"):
    
    image = cv2.imread(img)

    image = image[0:720, 200:250+720]

    name = str(cntr) + ".jpg"

    cv2.imwrite(name, image)

    cntr = cntr + 1

    #image.save(os.path.join("C:/Users/lachl/OneDrive/Desktop/cropped/", name + '_cropped.jpg'))