# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 16:13:38 2021

@author: User
"""

import os
import glob
from PIL import Image


outDir1 = os.path.abspath('C:/Users/User/Desktop/out1') 
outDir2 = os.path.abspath('C:/Users/User/Desktop/out2') 
imageDir1 = os.path.abspath('C:/Users/User/Desktop/JPEGImages')


image1 = [] 
imgname1 = [] 

#Find all '.jpg' files
imageList1 = glob.glob(os.path.join(imageDir1, '*.png'))

#Traverse and extract file names
for item in imageList1:
    image1.append(os.path.basename(item))

#Traverse file names and remove the suffix, keeping only the name
for item in image1:
    (temp1, temp2) = os.path.splitext(item)
    imgname1.append(temp1)

imageDir2 = os.path.abspath('C:/Users/User/Desktop/Annotations')
image2 = []
imgname2 = []
imageList2 = glob.glob(os.path.join(imageDir2, '*.xml'))

for item in imageList2:
    image2.append(os.path.basename(item))

for item in image2:
    (temp1, temp2) = os.path.splitext(item)
    imgname2.append(temp1)

#By traversing, get the files in the first folder whose names (excluding suffixes) match the files in the second folder, and save them in the outDir folder.
#The file names should be the same as those in the first folder, and the suffix format should remain unchanged.
for item1 in imgname1:
    for item2 in imgname2:
        if item1 == item2:
            dir = imageList1[imgname1.index(item1)]
            img = Image.open(dir)
            name = os.path.basename(dir)
            img.save(os.path.join(outDir1, name))
