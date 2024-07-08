# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 13:22:13 2021

@author: User
"""
import os
import glob
import xml.etree.ElementTree as ET

xmlDir = os.path.abspath('C:/Users/User/Desktop/20210824/Annotations/')
xmlList = glob.glob(os.path.join(xmlDir, '*.xml'))


for xml in xmlList:
    #print(xml)
    tree = ET.parse(xml)
    root = tree.getroot()
    #for node in root.findall('object'):
        #if(node.find('type')) is not None and (node.find('type').text) == "robndbox": os.remove(xml); break;
    '''
    for node in root.findall('object'):
        if (node.find('name').text == "Header"): node.find('name').text = "0"
        elif (node.find('name').text == "Footer"): node.find('name').text = "1"
        elif (node.find('name').text == "Form"): node.find('name').text = "2"
        elif (node.find('name').text == "Memory Address"): node.find('name').text = "2,1"
        elif (node.find('name').text == "Drawings"): node.find('name').text = "3,0"
        elif (node.find('name').text == "Circuit"): node.find('name').text = "3,1"
        elif (node.find('name').text == "IC Diagram"): node.find('name').text = "3,2"
        elif (node.find('name').text == "Module"): node.find('name').text = "3,3"
        elif (node.find('name').text == "E-characteristics"): node.find('name').text = "3,4"
        elif (node.find('name').text == "Timing Diagram"): node.find('name').text = "3,5"
        elif (node.find('name').text == "Packaging"): node.find('name').text = "3,6"
        elif (node.find('name').text == "Naming"): node.find('name').text = "4"
    '''
    

    for node in root.findall('filename'):
        print(node.text)
        '''
        flag = 0
        if(node.text[-4:] != '.jpg' and node.text[-4:] != '.png'): flag = 1;
        
        if(flag == 1):
            imgpth1 = 'C:/Users/User/Desktop/20210824/JPEGImages/' + node.text + '.jpg'
            imgpth2 = 'C:/Users/User/Desktop/20210824/JPEGImages/' + node.text + '.png'
            xmlname1 = node.text + '.jpg'  
            xmlname2 = node.text + '.png'
            if(os.path.isfile(imgpth1)): node.text = xmlname1;print('1');
            if(os.path.isfile(imgpth2)): node.text = xmlname2;print('2');
       
        
        
        imgpth1 = 'C:/Users/User/Desktop/20210824/JPEGImages/' + node.text[:-4] + '.jpg'
        imgpth2 = 'C:/Users/User/Desktop/20210824/JPEGImages/' + node.text[:-4] + '.png'
        xmlname1 = node.text[:-4] + '.jpg'  
        xmlname2 = node.text[:-4] + '.png'
        
        if(os.path.isfile(imgpth1)): node.text = xmlname1
        if(os.path.isfile(imgpth2)): node.text = xmlname2
        '''
        #node.text = node.text + '.png
    
    '''
    for node in root.findall('size'):
        if(node.find('height')!=None):node.find('height').tag = 'hight'
    '''

    #tree.write(xml, encoding='UTF-8')

