# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 12:40:30 2022

@author: User
"""


import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
 
sets = []
classes = ["text"]
 

def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
 
def convert_annotation(image_add):
    image_add = os.path.split(image_add)[1]        
    image_add = image_add[0:image_add.find('.',1)] 
    in_file = open('1233/' + image_add + '.xml', encoding = 'utf8')        
    out_file = open('1235/%s.txt'%(image_add), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    
    if root.find('size'):
        size = root.find('size')
        w = int(size.find('width').text)    
        h = int(size.find('height').text)   
        '''if w==0:
            print("出错！ width或height为0:  "+image_add)
            os.remove("G:/set/"+image_add+".jpg")
            os.remove("G:/set/"+image_add+".xml")
            return
        '''
        for obj in root.iter('object'):
            difficult = obj.find('difficult').text
            cls = obj.find('name').text
            if cls not in classes or int(difficult)==1:
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
            bb = convert((w,h), b)
            out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
    else:
        print("出错！xml缺少size:  "+image_add)     
        os.remove("1233/"+image_add+".jpg")
        os.remove("1234/"+image_add+".xml")
 
 
image_adds = open("1233/val.txt")        
for image_add in image_adds:
    #print(image_add)
    #image_add = image_add.strip()
    #print (image_add)
    convert_annotation(image_add)
