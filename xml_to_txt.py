# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 15:28:03 2022

@author: User
"""

import os
import os.path
import glob
import xml.etree.ElementTree as ET


class_names = ['text']

xml_path = ''
txt_path = ''

def xml_to_txt_onefiles(xml_path, txt_path):
    name_txt = 'train.txt'
    txt_file = os.path.join(txt_path, name_txt)
    f = open(txt_file, 'w')

    try:
        annotations = os.listdir(xml_path)
        annotations = glob.glob(str(xml_path) + "\\" + str(annotations) + '*.xml')
        print(annotations)
        if not annotations:
            raise FileExistsError
    except FileExistsError:
        print("No xml files, check the path!")


    for _, file in enumerate(annotations):
        xml_file = open(file, encoding = 'utf8')
        tree = ET.parse(xml_file)	
        root = tree.getroot()		


        filename = root.find('filename').text
        for obj in root.iter('object'):
            name = obj.find('name').text
            class_num = class_names.index(name)

            bndbox = obj.find('bndbox')
            x1 = bndbox.find('xmin').text
            x2 = bndbox.find('xmax').text
            y1 = bndbox.find('ymin').text
            y2 = bndbox.find('ymax').text
            f.write(' '+x1+','+y1+','+x2+','+y2+','+str(class_num))
        f.write('\n')

if __name__ == '__main__':
    xml_to_txt_onefiles(xml_path, txt_path)
    print('Finish!!')