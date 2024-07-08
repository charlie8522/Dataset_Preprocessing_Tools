# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 17:57:32 2021

@author: User
"""

import os
import random

pth = 'Annotations/'
split_pth = 'anno/'
val_percent = 0.2

img_list = os.listdir(pth)
random.shuffle(img_list)
train_count = int((1-val_percent)*len(img_list)) 
val_count = int(val_percent*len(img_list)) 

train_txt = open(os.path.join(split_pth,"train.txt"),"w",encoding='UTF-8')
t_cnt = 0
print(train_count,val_count)
for i in range(train_count):
    txt_name = img_list[i].split(".xml")[0]
    txt_name = txt_name + "\n"
    t_cnt+=1
    train_txt.write(txt_name)
train_txt.close()

val_txt = open(os.path.join(split_pth,"val.txt"),"w",encoding='UTF-8')
v_cnt = 0
for i in range(val_count):
    val_name = img_list[train_count+i].split(".xml")[0]
    val_name = val_name + "\n"
    v_cnt+=1
    val_txt.write(val_name)
val_txt.close()

    